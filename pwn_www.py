# simple python script for making connections world wide web

import subprocess
from pyngrok import ngrok
import threading
import argparse
import socket

parser = argparse.ArgumentParser(epilog='simple script to recieve connections from the public internet')
parser.add_argument('protocol', choices=["http","tcp"], help="open http/tcp tunnel")
parser.add_argument('--port','-p',type=int, help="port to use")
parser.add_argument('--nc', action="store_true", help='open a nc listener with the tcp tunnel')
args = parser.parse_args()

port = args.port


def open_nc():
	import os
	os.system(f"ncat -lnvp {port}")


def public_tcp():
	ptcpserver = ngrok.connect(port, 'tcp')
	print(f'opened public tcp {ptcpserver}')
	alive_process = ngrok.get_ngrok_process()
	alive_process.proc.wait()



def www():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	local_ip = s.getsockname()[0]

	if args.protocol == "tcp":
		try:

			tp = threading.Thread(target=public_tcp)
			tp.start()

			if args.nc:
				tnc = threading.Thread(target=open_nc)
				tnc.start()
		
		except KeyboardInterrupt:
			print('\n[-] shutting down')
			ngrok.kill()  

	if args.protocol == "http":
		try:

			phttpserver = ngrok.connect(port, 'http')
			print(f'[*] opened local http server on (http://{local_ip}:{port})')
			print(f'[*] opened public http {phttpserver}')
			subprocess.run(['python3', '-m', 'http.server', f'{port}'], capture_output=True).stdout()
			alive_process = ngrok.get_ngrok_process()
			alive_process.proc.wait()
		except KeyboardInterrupt:
			print('\n[-] shutting down')
			ngrok.kill()

www()
