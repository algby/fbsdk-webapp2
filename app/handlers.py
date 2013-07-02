# encoding: utf-8
from app.settings import config
from app.base import BaseHandler
from app.utils.facebook import FacebookSDK
import webapp2


class IndexHandler(BaseHandler):

    def get(self):

        fb = FacebookSDK()

        url = fb.get_url_login()

        if not 'access_token' in self.session and not 'user' in self.session:

            if 'error' in self.request.GET:
                return self.render_template('index.html', login_facebook=url, error=u'Você precisa aceitar o aplicativo!')

            if 'code' in self.request.GET:
                token = fb.get_access_token(self.request.GET['code'])
                self.session['access_token'] = token
                return self.redirect('/')
            return self.render_template('index.html', login_facebook=url)

        else:
            if not 'user' in self.session:
                result = fb.fql(query="SELECT name FROM user WHERE uid = me()", access_token=self.session['access_token'])
                self.session['user'] = result['data'][0]
            return self.render_template('home.html', user=self.session['user'])


app = webapp2.WSGIApplication([
    ('/', IndexHandler)
], config=config, debug=True)
