#! /usr/bin/python

import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO

#Initialize Raspberry PI GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#Tornado Folder Paths
settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static")
	)

#Tonado server port
PORT = 80


class MainHandler(tornado.web.RequestHandler):
  def get(self):
     print ("[HTTP](MainHandler) User Connected.")
     self.render("index.html")

	
class WSHandler(tornado.websocket.WebSocketHandler):
  def open(self):
    print ('[WS] Connection was opened.')
 
  def on_message(self, message):
    print ('[WS] Incoming message:'), message
    
    if message == "on_g":
      GPIO.output(16, True)
    if message == "off_g":
      GPIO.output(16, False)
      
    if message == "on_r":
      GPIO.output(18, True)
    if message == "off_r":
      GPIO.output(18, False)
      
    if message == 'on_b':
      GPIO.output(11 , True)
    if message == 'off_b':
      GPIO.output(11 , False)
      
    if message == 'on_w':
      GPIO.output(13 , True)
    if message == 'off_w':
      GPIO.output(13 , False)

  def on_close(self):
    print ('[WS] Connection was closed.')


application = tornado.web.Application([
  (r'/', MainHandler),
  (r'/ws', WSHandler),
  ], **settings)


if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(application)
        http_server.listen(PORT)
        main_loop = tornado.ioloop.IOLoop.instance()

        print ("Tornado Server started")
        main_loop.start()

    except:
        print ("Exception triggered - Tornado Server stopped.")
        GPIO.cleanup()

#End of Program
