import time
from i2c import vl6180x


vl = vl6180x.VL6180X()

print("Test and setup the sensor!")
if not vl.setup():
    print("Faled to find sensor")
    while True:
        pass


while True:
    lux = vl.readLux(vl6180x.VL6180X_ALS_GAIN_5)

    print("Lux: " + lux)

    range = vl.readRange()
    status = vl.readRangeStatus()

    if status == vl6180x.VL6180X_ERROR_NONE:
        print("Range: " + range)

    if (status >= vl6180x.VL6180X_ERROR_SYSERR_1) and (status <= vl6180x.VL6180X_ERROR_SYSERR_5):
        print("System error");
    elif status == vl6180x.VL6180X_ERROR_ECEFAIL:
        print("ECE failure");
    elif status == vl6180x.VL6180X_ERROR_NOCONVERGE:
        print("No convergence");
    elif status == vl6180x.VL6180X_ERROR_RANGEIGNORE:
        print("Ignoring range");
    elif status == vl6180x.VL6180X_ERROR_SNR:
        print("Signal/Noise error");
    elif status == vl6180x.VL6180X_ERROR_RAWUFLOW:
        print("Raw reading underflow");
    elif status == vl6180x.VL6180X_ERROR_RAWOFLOW:
        print("Raw reading overflow");
    elif status == vl6180x.VL6180X_ERROR_RANGEUFLOW:
        print("Range reading underflow");
    elif status == vl6180x.VL6180X_ERROR_RANGEOFLOW:
        print("Range reading overflow");
    time.sleep(50);

