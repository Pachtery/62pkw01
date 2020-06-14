import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
Request = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request
    messagetosend = bytes('Home!!!',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    print(Request)
    if Request == 'lamp1/on':
      GPIO.output(12,True)
    if Request == 'lamp1/off':
      GPIO.output(12,False)
    if Request == 'lamp2/on':
      GPIO.output(21,True)
    if Request == 'lamp2/off':
      GPIO.output(21,False)
    if Request == 'lamp3/on':
      GPIO.output(16,True)
    if Request == 'lamp3/off':
      GPIO.output(16,False)
    if Request == 'lamp4/on':
      GPIO.output(20,True)
    if Request == 'lamp4/off':
      GPIO.output(20,False)
    return


server_address_httpd = ('192.168.43.180',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('Starting server :')
httpd.serve_forever()
GPIO.cleanup()

