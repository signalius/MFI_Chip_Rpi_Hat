
## Application to read cert from MFI chip

First you have to enable i2c
```bash
raspi-config
```

To check if MFI chip is visible in RPi:
```bash
# List all i2c interfaces
i2cdetect -l 
# Check interface number 1
i2cdetect -y 1 
```

Before using, set the appropriate i2c interface and I2c address. 
The address is usually 0x10 or 0x11 and the interface is /dev/i2c-1.
Then:
```bash
python3 auth.py
```

## LICENSE
GNU General Public License v3.0

