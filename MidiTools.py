#!/usr/bin/python3

from guizero import App, Text, PushButton, yesno, info
import subprocess

def startBT():
    welcome_message.value = "Starting Bluetooth MIDI Server"
    subprocess.Popen(["xterm", "/home/pi/midisynctools/ToolScripts/btMidi"])

def checkStatus():
    welcome_message.value = "Displaying MIDI Connections"
    subprocess.Popen(["xterm","/home/pi/midisynctools/ToolScripts/MidiStatus"])

def startMidiConnector():
    welcome_message.value = "Starting Midi Connector"
    subprocess.Popen(["/home/pi/midisynctools/ToolScripts/MidiConnectorPy.py"])

    
def startAPReciever():
    welcome_message.value = "Starting AirPlay Reciever"
    info("Info", "Best run when in 1080p HDMI output. May need to run '/home/pi/LCD-show/LCD-hdmi' prior to running.")
    if (yesno("RPiPlay", "Display may lose visual feedback, best used with keyboard/VNC control. Terminate with Ctrl+ C. Continue?")):
        subprocess.Popen(["xterm", "-e", "/home/pi/RPiPlay/build/rpiplay", "-n","MidiToolsAP", "-b", "auto"])

def startLCDhdmi():
    welcome_message.value = "Changing display settings"
    if(yesno("Reboot?", "This will require a restart. Continue?")):
        subprocess.Popen(["xterm", "-e", "sudo", "/home/pi/LCD-show/LCD-hdmi"], cwd="/home/pi/LCD-show")

def startLCDdriver():
    welcome_message.value = "Changing display settings"
    if(yesno("Reboot?", "This will require a restart. Continue?")):
        subprocess.Popen(["xterm", "-e", "sudo", "/home/pi/LCD-show/MPI4008-show"], cwd="/home/pi/LCD-show")
    
    
app = App(title="Midi Sync Tools", layout="auto", height="350", width="300")

welcome_message = Text(app, text=" ", size=12, font="Helvetica", color="Black")


BTbutton = PushButton(app, command=startBT, text="Start Bluetooth MIDI", width="fill")

MidiStatbutton = PushButton(app, command=checkStatus, text="Check MIDI Status", width="fill")

MidiConnectbutton = PushButton(app, command=startMidiConnector, text="Midi Connector", width="fill")


APbutton = PushButton(app, command=startAPReciever, text="Start AirPlay Reciever", width="fill")

LCDhdmibutton = PushButton(app, command=startLCDhdmi, text="Monitor Display", width="fill")

MPI4button = PushButton(app, command=startLCDdriver, text="Touch Display", width="fill")

Output_message = Text(app, text="by James", size=10, font="Helvetica", color="Black", align = "bottom")


app.display()
