# simple python script for making connections world wide web

import subprocess
from pyngrok import ngrok
import click
import socket

@click.command()
@click.option('--tcp', is_flag=True, help='public tcp server')
@click.option('--http', is_flag=True, help='public http server')
@click.option('--port','-p', type=int, help='port to listen on')
def www(tcp,http,port):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	local_ip = s.getsockname()[0]

	if tcp:
		try:

			ptcpserver = ngrok.connect(port, 'tcp')
			print(f'[*] opened public tcp {ptcpserver}')
			print(f"[+] if you didn't already you have to open a listener locally on port {port} ")
			alive_process = ngrok.get_ngrok_process()
			alive_process.proc.wait()
		
		except KeyboardInterrupt:
			print('\n[-] shutting down')
			ngrok.kill()  
		

	if http:
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
