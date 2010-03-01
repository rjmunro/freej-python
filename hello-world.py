# system wide useful modules
import threading
import time

import freej

# initializes FreeJ creating a Contex
cx = freej.Context()

# creates a screen of given size
scr = freej.SdlScreen( 400, 300 )
# adds the screen
cx.add_screen(scr)

# create an instance of a TextLayer
txt = freej.TextLayer()

# initializes the new layer with the freej context
txt.init(cx)

# writes the hello world text inside the layer
txt.write("Hello World!")

# start the layer
txt.start()

# add the layer to the screen
cx.add_layer(txt)

# starts freej in a separate thread
th = threading.Thread(target = cx.start , name = "freej")
th.start()
