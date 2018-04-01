# SocketPdb
## Debugging a Python plugin over a TCP socket
This module is intended for debugging a Python application when stdin/stdout are not accessible. It was initially created for debugging Sublime text plugins, but can be used for any script.

## How to use
Set up a TCP server socket in a terminal, e.g. with *netcat*:

```bash
nc -k -l 4444
```

Import the module into your Python script and invoke the remote debugger:

```python
from socket_pdb import SocketPdb
SocketPdb(host="localhost", port=4444).set_trace()
```

The host (*localhost*) and port number (`4444`) can be set to whatever fits your setup.

## Under the hood
### [bdb](https://github.com/python/cpython/blob/3.3/Lib/bdb.py)
Contains the actual debugging functionality

### [pdb](https://github.com/python/cpython/blob/3.6/Lib/pdb.py)
Contains a combination of bdb and a command line utility. By redirecting the input/output to the socket, we can get all the same functionality as if using the local command line.

### `sys.settrace(...)`
Is used for registering callbacks that should be run on any function return/call

## Acknowledgement
The module is initially inspired by and based on [remote_pdb](https://github.com/ionelmc/python-remote-pdb)