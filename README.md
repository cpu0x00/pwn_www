# pwn_www

open public http and tcp tunnels on the go ;)

```
# pwn_www.py --help
usage: pwn_www.py [-h] [--port PORT] [--nc] {http,tcp}

positional arguments:
  {http,tcp}            open http/tcp tunnel

options:
  -h, --help            show this help message and exit
  --port PORT, -p PORT  port to use
  --nc                  open a nc listener with the tcp tunnel

simple script to recieve connections from the public internet
```
dependencies:
```
python3 -m pip install pyngrok
```
