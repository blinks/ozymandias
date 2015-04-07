import json
import webapp2

class GameApi(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'application/json'
    self.response.write(json.dumps({
      'map': [{'q': 0, 'r': 0, 'value': 1, 'gems': 0, 'stack': []}],
      }))

app = webapp2.WSGIApplication([
  ('/api', GameApi),
], debug=True)
