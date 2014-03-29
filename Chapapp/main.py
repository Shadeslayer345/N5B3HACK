import webapp2

from google.appengine.api import mail
from google.appengine.api import users

CONTACT_PAGE_HTML = """
<script type="text/javascript">
function everif(str) {

		var at="@"
		var punct="."
		var lat=str.indexOf(at)
		var lstr=str.length
		var lpunct=str.indexOf(punct)
		if (str.indexOf(at)==-1){
		   alert("Valid email must be entered")
		   return false
		}

		if (str.indexOf(at)==-1 || str.indexOf(at)==0 || str.indexOf(at)==lstr){
		   alert("Valid email must be entered")
		   return false
		}

		if (str.indexOf(punct)==-1 || str.indexOf(punct)==0 || str.indexOf(punct)==lstr){
		    alert("Valid email must be entered")
		    return false
		}

		 if (str.indexOf(at,(lat+1))!=-1){
		    alert("Valid email must be entered")
		    return false
		 }

		 if (str.substring(lat-1,lat)==punct || str.substring(lat+1,lat+2)==punct){
		    alert("Valid email must be entered")
		    return false
		 }

		 if (str.indexOf(punct,(lat+2))==-1){
		    alert("Valid email must be entered")
		    return false
		 }
		
		 if (str.indexOf(" ")!=-1){
		    alert("Valid email must be entered")
		    return false
		 }

 		 return true					
	}

function evalid(){
	var emailID=document.contact_form.mail
	
	if (everif(emailID.value)==false){
		emailID.focus()
		return false
	}
	
//empty field validation
	
	var fname=document.contact_form.fname
	if ((fname.value==null)||(fname.value=="")){
        alert("Fields marqued with * must be entered")
        fname.focus()
        return false
        }
	
	var subject=document.contact_form.subject	
	if ((subject.value==null)||(subject.value=="")){
        alert("Fields marqued with * must be entered")
        subject.focus()
        return false
        }
 
	var message=document.contact_form.message	
	if ((message.value==null)||(message.value=="")){
        alert("Fields marked with * must be entered")
        message.focus()
        return false
        }
			
	return true
 }
 </script>
<table border="0" cellpadding="5" cellspacing="0" width="600">
<form name="contact_form" method="post" action="composemail.py" onSubmit="post()">

    <td>Name *</td>
    <td colspan="2"><input name="fname" type="text" size="30" /></td>
  </tr><tr>
    <td>Your E-mail *</td>
    <td colspan="2"><input type="text" name="mail" size="30" /></td>
  </tr><tr>
    <td>Subject *</td>
    <td colspan="2"><input name="subject" type="text" size="30" /></td>
  </tr><tr>
    <td>Message *</td>
    <td colspan="2"><textarea name="message" onkeyup="return limitarelungime(this, 255)"  cols="35" rows="5"></textarea></td>
  </tr>
  <tr>
    <td><input type="reset" name="reset" value="Reset"/></td>
    <td align="right"><input type="submit" name="Submit" value="Submit"></td></td>
  </tr>
  </tr>
<tr>
<td colspan="2" align="center"> <br />
<table border="0" cellpadding="0" cellspacing="0">
<tr valign="top">
</form>"""
class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write('Hello, NSBE!')

class ContagePage(webapp2.RequestHandler):
	def get(self):
		self.response.write(CONTACT_PAGE_HTML)

class SendPage(webapp2.RequestHandler):
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

application = webapp2.WSGIApplication([('/hola', SendPage),('/hello', MainPage),('/contactus', ContagePage),], debug=True)