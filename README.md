
# midisynctools
Menu script for aconnect/MIDI Host functions + more on a Raspberry Pi. Not exclusive to Teenage Engineering devices, but useful for them in particular. 
This script is essentially a GUI wrapper to run commands via a simple organised menu that can be utilised with or without a touchscreen for portability. 

## Purpose

For: those with USB MIDI devices that need a central Host for connection, do not necessarily need a MIDI DIN plug connector and are not keen on buying standalone USB Host devices. Especially if you already own a Raspberry Pi.

This script is especially useful for people with this particular setup:

- USB MIDI Devices, **especially Teenage Engineering synthesisers - OP-1 and/or OP-Z**
  - It is especially useful as it runs RPiPlay which can be used as an airplay screen mirror reciever. This allows one to stream Videolab videopak visuals from te OP-Z iOS app to this device - either on the LCD display or to an HDMI output.
	- Alternatively, can also just be used with any iOS visualiser app, particularly if you use an iPad connected via Bluetooth MIDI
- Raspberry Pi with Raspbian/Raspberry Pi OS desktop installed.

  - with 4x USB ports or a USB hub.
 
- Touch screen display/case

  - e.g. http://www.lcdwiki.com/4inch_HDMI_Display-C
		
    - https://www.amazon.ca/gp/product/B07YDBFY8F/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
		
## Prerequisites
For full functionality:

- https://github.com/FD-/RPiPlay -- AirPlay Screen Mirroring Recveiver

- https://github.com/goodtft/LCD-show -- Drivers for the Touchscreen Display - if you don't have a touchscreen using these drivers, you will need to modify the script.

- https://neuma.studio/rpi-midi-complete.html

  - This guide details setting up automatic MIDI connections when USB devices are plugged in. This is not necessary but **may be useful and faster for on-the-go/get-out-of-my-backpack-and-start-jamming usage** of your Pi as the MIDI host. **It also details installation of the Bluetooth MIDI server.**
 My personal setup does not have the Bluetooth MIDI service set up nor does it run the service at start up. I prefer to start it via this script and close it when not in use.

## Functionality:

![Image of Menu](https://github.com/urbanvanilla/midisynctools/blob/master/menu.png?raw=true)

* Starts Bluetooth MIDI server in terminal window. Can be closed to turn it off.

* Opens terminal window to check MIDI Connection status.

* Opens MIDI Connector window, a script to disconnect all

* MIDI connections or reroute connected devices.

* Start RPiPlay (needs to be cloned/built from the RPiPlay github repo)

* Change configuration from utilising touch screen display (this script utilises the scripts and drivers from LCD-show github repo)
  * This is so you can go between using the device portably with touch screen function and using it on a normal HDMI output screen while mirroring Airplay from an iOS device for visuals. In my experience, using the touch screen drivers stops you from using full resolution with normal HDMI output, so it is necessary to change between them.

## Installation

Copy the repo files to your pi folder.
git clone https://github.com/urbanvanilla/midisynctools.git

Edit MidiTools.py

	subprocess.Popen(["xterm", "-e", "sudo", "/home/pi/LCD-show/MPI4008-show"], cwd="/home/pi/LCD-show")

Change 'MPI4008-show' to the script that installs your LCD display device. If it is not a driver included in LCD-show, then this may have different functionality. You can conversely delete the Touch Display and Monitor Display buttons if you don't have a Touch display or need to change the display drivers between touch screen and normal HDMI/monitor output.


## Caveats
Currently the midi connector script is barebones. This mostly because I'm an extremely novice programmer, including with regards to regular expressions and getting extra functionality/visual feedback may be something for further development.

The functionality is straightforward, and it does not show the live connections between various devices such as with https://github.com/nuc/Midi-Connector but also does not require running node.js or usage via a web browser.
If you like this extra functionality, Midi-Connector can be installed via node.js and npm as well.

