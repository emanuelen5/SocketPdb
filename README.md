# SocketPdb
[![Build Status](https://travis-ci.org/emanuelen5/SocketPdb.svg?branch=master)](https://travis-ci.org/emanuelen5/SocketPdb)

## Debugging a Python plugin over a TCP socket
This module is intended for debugging a Python application when stdin/stdout are not accessible. It was initially created for debugging Sublime text plugins, but can be used for any script.

## How to use
Set up a TCP server socket in a terminal, e.g. with *netcat* (for setting up a TCP TTY server) together with *rlwrap* (for command history):

```bash
rlwrap nc -k -l 4444
```

Import the module into your Python script and invoke the remote debugger:

```python
from socket_pdb import SocketPdb
SocketPdb(host="localhost", port=4444).set_trace()
```

The host (*localhost*) and port number (`4444`) can be set to whatever fits your setup.

## Acknowledgement
The module is initially inspired by and based on [remote_pdb](https://github.com/ionelmc/python-remote-pdb)
