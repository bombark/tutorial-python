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

	def send_error_404(self):
		self.send_response(404)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write("Error!\n")


	def exec_request(self):
		if self.path == "/":

			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write( "Hello World!" )

		else:
			self.send_error_404()







class HttpCtrl:
	def __init__(self,port):
		self.port   = port
		self.httpd = HTTPServer(('', port), CtrlHttpTask)

		#server_address = ('', self.port)
		#httpd = server_class(server_address, CtrlHttpTask)

#-------------------------------------------------------------------------------



#===============================================================================

client = HttpCtrl(8080);
while True:
	client.httpd.handle_request()

#-------------------------------------------------------------------------------
