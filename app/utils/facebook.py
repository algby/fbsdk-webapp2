# encoding: utf-8
from google.appengine.api import urlfetch
from app.settings import config
import urlparse
import hashlib
import urllib
import json
import time
import os


class FacebookSDK(object):

    def __init__(self, access_token=None):
        self.access_token = access_token
        self.app_id = config['APP_ID']
        self.app_secret = config['APP_SECRET']
        self.redirect_uri = config['REDIRECT_URI']

    def get_url_login(self):
        state = self._generate_hash(num_random=self._get_encode_random())
        return ("https://www.facebook.com/dialog/oauth"
                "?client_id=%(APP_ID)s"
                "&redirect_uri=%(REDIRECT_URI)s"
                "&state=%(STATE)s"
                "&scope=%(SCOPE)s" % {'APP_ID': self.app_id,
                                      'STATE': state,
                                      'REDIRECT_URI': self.redirect_uri,
                                      'SCOPE': ",".join(config['SCOPE'])})

    def get_url_logout(self):
        return ("https://www.facebook.com/logout.php?"
                "next=%(REDIRECT_URI)s&"
                "access_token=%(ACCESS_TOKEN)s" % {
                'REDIRECT_URI': self.redirect_uri,
                'ACCESS_TOKEN': self.access_token
                })

    def _generate_hash(self, num_random):
        """
            O objetivo desse metodo eh gerar uma chave unica
            num_random - num_random do usuário
            millis - por questões de segurança, é gerado um numero para poder
            ser usado na url de auth, é praticamente impossível ter 2 pessoas
            com o mesmo num_random e com o mesmo milesegundos autenticando
        """
        num_random = self._get_encode_random()
        millis = self._get_milleseconds()
        return hashlib.md5("%s%s%s" % (config['KEY'], num_random, millis)).hexdigest()

    def _get_encode_random(self):
        """
            Esse metodo pega o num_random do usuario
        """
        return os.urandom(16).encode('hex')

    def _get_milleseconds(self):
        """
            Pegando o tempo e convertendo pra milesegundos
        """
        return int(round(time.time() * 1000))

    def _url_oauth_token(self, code):
        return ("https://graph.facebook.com/oauth/access_token?"
                "client_id=%(APP_ID)s&"
                "client_secret=%(APP_SECRET)s&"
                "redirect_uri=%(REDIRECT_URI)s&"
                "code=%(code)s" % {'APP_ID': self.app_id,
                                   'APP_SECRET': self.app_secret,
                                   'REDIRECT_URI': self.redirect_uri,
                                   'code': code})

    def get_access_token(self, code):
        try:
            url = self._url_oauth_token(code)
            result = urlfetch.fetch(url)
            access_token = urlparse.parse_qs(result.content)['access_token'][0]
            return access_token
        except Exception:
            return None

    def fql(self, query):
        params = {
            'access_token': self.access_token,
            'q': query
        }
        url = "https://graph.facebook.com/fql?%s" % urllib.urlencode(params)
        return json.loads(urlfetch.fetch(url).content)

    def graph_api(self, url, method=urlfetch.GET):
        params = {
            'access_token': self.access_token,
        }
        url = "https://graph.facebook.com/%(url)s?%(access_token)s" % {
            'access_token': urllib.urlencode(params),
            'url': url,
        }
        return json.loads(urlfetch.fetch(url).content)
