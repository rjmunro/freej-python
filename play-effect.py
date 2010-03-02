#!/usr/bin/env python
# System wide useful modules
import threading
import time
import sys

import freej

# initializes FreeJ creating a Context
cx = freej.Context()

# creates a screen of given size
scr = freej.SdlScreen(400, 300)

# adds the screen
cx.add_screen(scr)

# refreshes the list of available filter effects
cx.plugger.refresh(cx)

# check that we have an argument
if(sys.argv.__len__()<2):
  print "[!] this script needs an argument: file to play"
  quit()

# opens the file given on commandline as a layer
lay = cx.open(sys.argv[1])

# gets the vertigo filter effect
filt = cx.filters["vertigo"]

# adds the filter to the layer
lay.add_filter(filt)

# start the layer thread
lay.start()

# adds the layer to the freej context
cx.add_layer(lay)

# starts freej in a separate thread
th = threading.Thread(target = cx.start , name = "freej")
th.start()
