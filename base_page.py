import webapp2

class HelloWorld(webapp2.RequestHandler):
	def get(self):
		self.response.handlers['Content-Type'] = 'text/plain'
		self.response.write = 'Hello World!'