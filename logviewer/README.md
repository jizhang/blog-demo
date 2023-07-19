# Logviewer

## Development

Require Python 3.7 or newer.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Demo

### Start WebSocket server

```
$ python server.py -h
usage: server.py [-h] [--host HOST] [--port PORT] --prefix PREFIX

optional arguments:
  -h, --help       show this help message and exit
  --host HOST
  --port PORT
  --prefix PREFIX  Allowed directories

$ python server.py --host 127.0.0.1 --port 8765 --prefix /tmp/ --prefix /tmp/dir1
```

### Start demo client

```
python -m http.server
```

Create `/tmp/demo.log` file and browse `http://localhost:8000/demo.html`, you will see the content of the log file. Append logs to this file and the content will be shown in browser immediately.
