#!/usr/bin/python

import time
from threading import Thread
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer





#This class will handles any incoming request from
#the browser
class CtrlHttpTask(BaseHTTPRequestHandler):

	def do_GET(self):
		self.exec_request()

	def do_POST(self):
		self.exec_request()

	def exec_request(self):
		self.finish = False;
		self.data = {}
		self.data["method"] = "get"
		self.data["url"] = "/"

		#while ( ! self.finish ):
		#	time.sleep(1)

		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write( "Hello World!" )


	def send_error_404(self):
		self.send_response(404)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("Error!\n")



	def input(self):
		return self.data;

	def output(self):
		self.finish = True;





class HttpCtrl:
	def __init__(self,port):
		self.port   = port
		self.httpd = HTTPServer(('', port), CtrlHttpTask)
		#server_address = ('', self.port)
		#httpd = server_class(server_address, CtrlHttpTask)

	def next(self):
		a = self.httpd.handle_request()
		print(a)
		return "sss"



def main():
	client = HttpCtrl(8080);
	while True:
		task = client.next();
		print(task)


main()
