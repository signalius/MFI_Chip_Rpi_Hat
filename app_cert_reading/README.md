
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

## LICENSE
GNU General Public License v3.0

