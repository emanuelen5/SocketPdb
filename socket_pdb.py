import socket
import sys
from pdb import Pdb

__version__ = "1.0.0"
is_python_3 = sys.version_info[0] == 3

class SocketPdb(Pdb):
    """
    On construction this object will block execution until it's connected to a server.

    Start up a terminal and set up a TCP server socket: 
    ```bash
    nc -k -l 4444
    ```

    Then start up the Python script with the stack trace embedded:
        SocketPdb(host="localhost", port=4444).set_trace()

    It might also be possible to use it as the pdb module and invoke another module (`python -m SocketPdb <script_to_debug>`), but I have not tested it.
    """

    def __init__(self, host, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        print("SocketPdb session open at %s:%s" % self.socket.getsockname())
        if is_python_3:
            self.handle = self.socket.makefile('rw')
        else:
            self.handle = self.socket.makefile()
        self.handle.write("\n*********************\n")
        self.handle.write("PDB debugger opening\n")
        Pdb.__init__(self, completekey='tab', stdin=self.handle, stdout=self.handle)

    def close(self):
        self.handle.write("PDB debugger closing\n")
        self.handle.write("********************\n")
        self.handle.close() # Need to close this before the socket?
        self.socket.close()

    def set_quit(self):
        # Use the usual handler when quitting, but make sure to close socket as well
        super(SocketPdb, self).set_quit()
        self.close()

    def set_continue(self):
        # Override bdb's function so that the sys.settrace handler is not removed when running without breakpoints. Otherwise we cannot detect when exiting the topmost frame (which we need to do to be able to close the socket when finished)
        self._set_stopinfo(self.botframe, None, -1) # Copied from bdb.set_continue

    def dispatch_return(self, frame, arg):
        super(SocketPdb, self).dispatch_return(frame, arg)
        # If at the topmost frame, quit the debugger
        if frame.f_back is None:
            self.set_quit()