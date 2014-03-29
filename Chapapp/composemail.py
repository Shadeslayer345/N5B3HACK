import webapp2
from google.appengine.api import mail
from google.appengine.api import users



class ContagePage(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hey NSBE')


class MessageHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user is None:
          login_url = users.create_login_url(self.request.path)
          self.redirect(login_url)
          return
        to_addr = self.request.get("friend_email")
        if not mail.is_email_valid(to_addr):
            # Return an error message...
            pass

        message = mail.EmailMessage()
        message.sender = (cgi.escape(self.request.get('fname')))
        message.to = 'nsbefreshhu@gmail.com'
		message.subject = (cgi.escape(self.request.get('subject')))
        message.body = (cgi.escape(self.request.get('message')))

        message.send()
		
		self.response.write('<!doctype html><html><body>Message sent</html>')
		
application = webapp2.WSGIAPPLICATION([ ('/contactus', MainPage), ('/sent', MessageHandler),], debug=True)