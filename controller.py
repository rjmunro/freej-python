#!/usr/bin/env python
import threading
import freej

# context and screen initialization
cx = freej.Context()
scr = freej.SdlScreen()
scr.init(1024,576,32)
cx.add_screen(scr)

### declare the Trigger Controller
class Frame(freej.TriggerController):
  def __init__(self, *args):
    super(Frame, self).__init__(*args)

  ### the dispatch function is the callback
  ### it will be called at every frame
  def dispatch(self):
    ### rotate around 360 degrees, incrementing
    ### this function is called once every frame
    if self.i>360:
      self.i=0
    self.i += 1
    self.txt.set_rotate( self.i )
    return 1
    # dispatch should always return an integer value

### create an instance of our Trigger Controller
f = Frame()
### set rotation index to zero
f.i = 0
### create a text layer inside the controller
f.txt = freej.TextLayer()
f.txt.init()
f.txt.write("Hello World!")
f.txt.start()
cx.add_layer(f.txt)

# register it on the current context
cx.register_controller(f)

# start running freej in a separate thread
th = threading.Thread(target = cx.start , name = "freej")
th.start()
