
## MFI Raspberry Pi Hat
This Raspberry Pi HAT allows you to work with MFI chips with the symbols MFI343S00177 and MFI337S3959. 
Additionally, it has a USB C power in connector because USB C from Raspberry Pi may be needed as a USB OTG port.

* Tested on: Raspberry 5 and Zero 2W
* Interface: I2C

## Sample cert

Convert string hex to binary file
```bash
echo "3082025b06092a86...." | xxd -r -p > cert.bin
```

Decode it
```bash
openssl pkcs7 -inform DER -in cert.bin -print_certs -text -noout
```

Result
```bash
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            22:22:aa:15:08:17:aa:06:aa:90:07:aa:16:78:09
        Signature Algorithm: sha1WithRSAEncryption
        Issuer: C=US, O=Apple Inc., OU=Apple Certification Authority, CN=Apple iPod Accessories Certification Authority
        Validity
            Not Before: Aug 17 20:46:29 2015 GMT
            Not After : Feb 14 22:18:08 2022 GMT
        Subject: C=US, O=Apple Inc., OU=Apple iPod Accessories, CN=IPA_2222AA150817AA06AA9007AA167809
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (1024 bit)
                Modulus:
                    00:b7:dd:d3:81:e7:38:97:7c:06:72:91:3d:6c:4a:
                    cf:d0:01:d1:af:30:06:9c:05:67:84:76:da:bc:d5:
                    ee:94:8d:c4:63:11:3c:95:67:17:ff:a9:48:85:b8:
                    34:02:6e:8c:54:71:13:a7:c0:ad:11:39:86:4a:a1:
                    df:f3:45:d5:27:d5:e4:b2:b4:d0:61:ab:fb:31:7d:
                    f2:7c:c8:27:45:cd:d6:61:8d:88:d3:9f:43:a6:91:
                    3c:ad:ad:c5:1e:62:cc:61:1b:49:27:1a:10:26:a1:
                    20:14:a3:6b:58:62:ad:6a:bc:95:13:ac:72:38:73:
                    b2:84:e8:b6:51:a1:fa:39:2b
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Subject Key Identifier: 
                D6:2B:D0:95:57:59:86:81:DB:D7:A0:32:75:2D:B9:A3:6E:5B:8A:38
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 Authority Key Identifier: 
                FF:4B:1A:43:9A:F5:19:96:AB:18:00:2B:61:C9:EE:40:9D:8E:C7:04
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment, Data Encipherment, Key Agreement
    Signature Algorithm: sha1WithRSAEncryption
    Signature Value:
        62:01:2d:2e:1b:39:ce:41:81:ea:a8:f3:07:e7:01:ee:d0:26:
```

## Schematic

![schematic](https://raw.githubusercontent.com/signalius/MFI_Chip_Rpi_Hat/master/electronic/RevA/Output/Schematic.png)

# PCB view

![pcb](https://raw.githubusercontent.com/signalius/MFI_Chip_Rpi_Hat/master/electronic/RevA/Output/pcb_3959.jpg)
![pcb](https://raw.githubusercontent.com/signalius/MFI_Chip_Rpi_Hat/master/electronic/RevA/Output/pcb_00177.jpg)

## LICENSE
GNU General Public License v3.0

