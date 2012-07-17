"""[ main.py ]
it's just here to redirect '/' to '/index.htm'
the redirect-link could be changed by changing the link below
"""

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainHandler(webapp.RequestHandler):
  def get(self):
    self.redirect('/flat_web/index.htm')
  def post(self):
    self.redirect('/flat_web/index.htm')

def main():
  application = webapp.WSGIApplication(
    [
          ('/', MainHandler),
        ], debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
