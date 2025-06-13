#  PicoCalc Micropython Setup

I find setting up the MicroPython build infuriating and I'm just not getting it correct.  Thankfully, the amazing community has a built MicroPython build.  

## References:

* [zenodante/PicoCalc-micropython-driver](https://github.com/zenodante/PicoCalc-micropython-driver/tree/main)

## Pre-Setup Notes:

* I chose to not use `zenodante`'s approach to compile the core APIs as frozen files.  This makes it impossible to edit them.   

* I instead only transfer the `boot.py` and `main.py` for the filesystem variant. 

* I have copies of the files, latest as of 6/13/2025, in my repo.  I modified them a bit, as a few minor parts if his APIs are non-functional. 

* <span style="color:red"><b><u>TODO: Submit PR to his repo!</u></b></span>


## Setup Pico

I duplicated the effort by doing the following:

### 1. Create a folder to hold the workspace

```bash
mkdir workspace
pushd workspace
```

### 2. Clone `PicoCalc-micropython-driver` repo into workspace folder. 

```bash
git clone git@github.com:zenodante/PicoCalc-micropython-driver.git
pushd PicoCalc-micropython-driver
git remote update --init --recursive
popd
```

### 3. Clone Micropython repo into workspace folder

```bash
git clone git@github.com:micropython/micropython.git
pushd micropython
git remote update --init --recursive
popd
```

### 4. Clone Eigenmath Repo into workspace folder

```bash
git clone git@github.com:zenodante/eigenmath_micropython.git
pushd eigenmath_micropython
git remote update --init --recursive
popd
```

### 5. Setup Micropython build

```bash

```

### 6. Connect Pico 2W to Thonny

### 7. Create /lib folder

On the terminal, run the following shell command on the repl:

```python
import os
os.makedirs('/lib')
```

### 8. Copy Project files

**Note:** I have the `os-path` project in this folder.   You can skip this if you want ot use Micropython's PIP API in Thonny instead.

**Process:** Copy `./lib` to `/lib` on the Pico.

---

## Utilities

### `keyboard_tester.py`

This is a simple script to log the values of keys pressed.  This can be clutch when you are writing an app and you want to know what a particular key is.  This will print values to the terminal until you press Escape. The escape value will be printed, and the application will exit.

```python
import keyboard_tester as kt
kt.run()
```



