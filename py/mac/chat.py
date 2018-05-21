#!usr/bin/env python

import socket
import threading
import select
import time

def main():
	class Chat_Server(threading.Thread):
			def __init__(self):
				threading.Thread.__init__(self)
				self.running = 1
				self.conn = None
				self.addr = None
			def run(self):
				HOST = ''
				PORT = 1776
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				s.bind((HOST,PORT))
				s.listen(1)
				self.conn, self.addr = s.accept()
				# Select loop for listen
				listenLoop()
			def kill(self):
				self.running = 0
	 
	class Chat_Client(threading.Thread):
			def __init__(self):
				threading.Thread.__init__(self)
				self.host = None
				self.sock = None
				self.running = 1
			def run(self):
				PORT = 1776
				self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				self.sock.connect((self.host, PORT))
				# Select loop for listen
				listenLoop()
			def kill(self):
				self.running = 0
				
	class Text_Input(threading.Thread):
			def __init__(self):
				threading.Thread.__init__(self)
				self.running = 1
			def run(self):
				while self.running == True:
					text = raw_input('')
					if text[0] == '/':
						if text[0:5] == '/kill':
							chat_client.sock.sendall('\tdisconnected.')
							chat_server.conn.sendall('\tdisconnected.')
							this.kill()
						elif text[0:4] == '/me ':
							chat_client.sock.sendall('\t'+text[4:])
							chat_server.conn.sendall('\t'+text[4:])
					try:
						chat_client.sock.sendall('\b'+text)
					except:
						Exception
					try:
						chat_server.conn.sendall('\b'+text)
					except:
						Exception
					time.sleep(0)
			def kill(self):
				self.running = 0

	# Prompt, object instantiation, and threads start here.
	def listenLoop():
		while parent.running == True:
			inputready,outputready,exceptready \
				= select.select ([self.sock],[self.sock],[])
			for input_item in inputready:
				# Handle sockets
				data = self.sock.recv(1024)
				if data:
					if data[0]=='\b':
						print "Enemy: " + data[1:]
					if data[0]=='\t':
						print "Enemy " + data[1:]
				else:
					break
			time.sleep(0)


	ip_addr = raw_input('What IP (or type listen)?: ')
	addrs = ['listen','server','serv']
	if ip_addr.lower() in addrs:
		chat_server = Chat_Server()
		chat_client = Chat_Client()
		chat_server.start()
		text_input = Text_Input()
		text_input.start()
	else:
		chat_server = Chat_Server()
		chat_client = Chat_Client()
		chat_client.host = ip_addr
		text_input = Text_Input()
		chat_client.start()
		text_input.start()

if __name__ == "__main__":
	main()



