#!/usr/bin/env python3
import time
from struct import Struct
import smbus2

# --- Setup ---
I2C_DEV = "/dev/i2c-1"
DEV_ADDR = 0x11


REG_STATUS        = 0x10
REG_CHAL_LEN      = 0x20
REG_CHAL_DATA     = 0x21
REG_RESP_LEN      = 0x11
REG_RESP_DATA     = 0x12
REG_CERT_LEN      = 0x30
REG_CERT_DATA     = 0x31

STATUS_BIT_SUCCESS = 0x10  
WORD_BE = Struct(">H")
CHUNK = 32                 
PAUSE_SHORT = 0.002
PAUSE_MED   = 0.02

bus = smbus2.SMBus(I2C_DEV)

def _rd(addr: int, n: int) -> bytes:
    # write pointer
    for _ in range(5):
        try:
            bus.write_byte(DEV_ADDR, addr)
            break
        except OSError:
            time.sleep(0.005)
    else:
        raise Exception(f"timeout: set pointer 0x{addr:02x}")

    time.sleep(0.005)
    for _ in range(50):
        try:
            read_msg = smbus2.i2c_msg.read(DEV_ADDR, n)
            bus.i2c_rdwr(read_msg)
            return bytes(read_msg)
        except OSError:
            time.sleep(0.01)
    raise Exception(f"timeout: read 0x{addr:02x}")

def _rd1(addr: int) -> int:
    return _rd(addr, 1)[0]

def _wr_raw(reg: int, data: bytes, pause=PAUSE_SHORT) -> None:
    for _ in range(10):
        try:
            msg = smbus2.i2c_msg.write(DEV_ADDR, bytes([reg]) + bytes(data))
            bus.i2c_rdwr(msg)
            if pause:
                time.sleep(pause)
            return
        except OSError:
            time.sleep(0.005)
    raise Exception(f"timeout: write 0x{reg:02x}")

def _wr_status(v: int) -> None:
    _wr_raw(REG_STATUS, bytes([v]))

def read_certificate() -> bytes:
    size = WORD_BE.unpack(_rd(REG_CERT_LEN, 2))[0]
    return _rd(REG_CERT_DATA, size)

def generate_challenge_response(challenge: bytes, poll_timeout_s=5.0) -> bytes:
    try:
        _wr_status(0x00)
    except Exception:
        pass
    time.sleep(PAUSE_MED)

    # len of  challenge (BE)
    _wr_raw(REG_CHAL_LEN, WORD_BE.pack(len(challenge)), pause=PAUSE_MED)

    # data if challenge – write in one transaction 
    _wr_raw(REG_CHAL_DATA, challenge, pause=PAUSE_MED)

    time.sleep(PAUSE_MED)

    # Start
    _wr_status(0x01)

    # poll status
    t0 = time.time()
    last = None
    while time.time() - t0 < poll_timeout_s:
        try:
            s = _rd1(REG_STATUS)
        except Exception:
            s = None
        if s != last:
            print("status:", hex(s) if s is not None else None)
            last = s
        if s is not None and (s & STATUS_BIT_SUCCESS):
            break
        time.sleep(0.02)
    else:
        raise Exception("timeout waiting for signature")

    # read the answer
    resp_len = WORD_BE.unpack(_rd(REG_RESP_LEN, 2))[0]
    return _rd(REG_RESP_DATA, resp_len)

if __name__ == "__main__":
    print("I2C bus:", I2C_DEV )
    print("I2C addr:", hex(DEV_ADDR) )

    cert = read_certificate()
    print("CERT", cert.hex())

    chal20 = b"12211213131231231231"  # 20 bytes for 3959
    chal32 = b"12211213131231231231456784567845"  # 32 bytes for 00177

    resp = ""

    print("Trying 20 bytes Challenge response...")
    try:
        resp = generate_challenge_response(chal20)
    except Exception as e:
        print("20 bytes challenge error: ", e)
        print("Trying 32 bytes Challenge response...")
        resp = generate_challenge_response(chal32)

    print("RESP: ", resp.hex())


	
