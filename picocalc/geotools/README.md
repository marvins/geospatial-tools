#  PicoCalc Micropython Setup

I find setting up the MicroPython build infuriating and I'm just not getting it correct.  Thankfully, the amazing community has a built MicroPython build.  

Some References:

* [zenodante/PicoCalc-micropython-driver](https://github.com/zenodante/PicoCalc-micropython-driver/tree/main)

My solution is to write a bunch of tools you can copy to an SD card, then "install" to the local folder. 

## Installing Libraries

### Very First Time

When booting the PicoCalc, manually type the following commands

```python
import os
os.chdir('/sd/geotools')
run('install.py')
```

