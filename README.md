Terminus Calculator Geospatial Tools
====================================

This repo contains a bunch of handy scripts for various applications.  I've focused most of these for Micropython, for either the PicoCalc, or the TI Nspire.

## Nspire Design Notes

Much of this code is designed for Micropython, where many, if not most, of the standard libraries are not included.  This also assumes many standard packages such as Matplotlib, Pandas, and others do not exist.

## Testing on Unix-Based Systems

Using a Unix build of Micropython, it's easy to test the NSpire variant.

### Step 1:  Copy Contents to Micropython Library Path

This will copy all contents of `./nspire/` to `~/.micropython/lib`.  For Micropython, this is usually the library path.

* If you want to purge your Micropython library path first, you can add `-c` to purge the contents.
* If you are developing and testing, you can add `-s` flag to use ***symlinks*** rather than file copies.

In this example, we setup symlinks and 
```bash
./scripts/copy-unix-micropython.sh -c -s
```


Update the path to Micropython.  Since I've built it manually, it's located here:
```bash
MPY_PATH="${HOME}/Desktop/Projects/workspace/micropython/ports/unix/build-standard"
```

### Step 2:  Run `./scripts/run-unix-micropython.sh`



