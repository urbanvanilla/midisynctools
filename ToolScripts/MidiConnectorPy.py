#!/usr/bin/python3

from guizero import App, ButtonGroup, Text, PushButton, Box, info
import subprocess
import re

sourceid = 0
destinationid = 0

def changeSource():
    sourceid = midisource.value

def changeDestination():
    destinationid = mididestination.value
    
def checkStatus():
    subprocess.Popen(["xterm","/home/pi/midisynctools/ToolScripts/MidiStatus"])
    
def connectMidi():
    sourceid = midisource.value
    destinationid = mididestination.value
    subprocess.Popen(["aconnect", str(sourceid)+":0", str(destinationid)+":0"])
    
def disconnectMidi():
    subprocess.Popen(["uxterm", "-e", "aconnect", "-x"])

cmd = [ "aconnect", "-l"]
rawmidilist = str(subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0])
pattern1 = r"client (\d+)"
clients = re.findall(pattern1, rawmidilist)
pattern2 = r": '(.{15})"
names = re.findall(pattern2, rawmidilist)

for y in range(0,len(names)):
    temp = names[y].split("'")
    names[y] = temp[0]


app = App(title="Midi Connector", layout="grid", height='300', width='400')

TopBox = Box(app, align='top', height='100', width='200', grid=[1,1])
LeftBox = Box(app, align='left', grid=[0,3])

RightBox = Box(app, align='right', grid=[3,3])
BottomBox = Box(app, align='bottom', height='100', width='300', grid=[1,3])

MidiStatbutton = PushButton(TopBox, command=checkStatus, text="Check MIDI Status", align='top', width="fill")
sourcetitle = Text(LeftBox, text="Source", size=12, font="Helvetica", color="Black", align="top")
destinationtitle = Text(RightBox, text="Destination", size=12, font="Helvetica", color="Black", align="top")
ConnectButton = PushButton(BottomBox, text="Connect", command=connectMidi, width="fill")
DisconnectButton = PushButton(BottomBox, text="Disconnect All", command=disconnectMidi, width="fill")

midisource = ButtonGroup(LeftBox, command=changeSource, align="left")
mididestination = ButtonGroup(RightBox, command=changeDestination, align="right")

for x in range(0,len(clients)):
    row = []
    row.append(names[x])
    row.append(clients[x])
    midisource.append(row)
    
for x in range(0,len(clients)):
    row = []
    row.append(names[x])
    row.append(clients[x])
    mididestination.append(row)
    
app.display()



