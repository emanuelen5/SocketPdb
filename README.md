# Debugging a Sublime text plugin using sockets
The module is based on [remote_pdb](https://github.com/ionelmc/python-remote-pdb)

## How to use
Import the module into your plugin:

```python
from remote_pdb import RemotePdb
```

Set up a virtual terminal with a raw TCP connection, e.g.

```bash
nc -k -l <PORT>
```

Stop execution in the Python script and invoke the remote debugger:

```python
RemotePdb(host="localhost", port=<PORT>).set_trace()
```
