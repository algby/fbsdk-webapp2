# encoding: utf-8
from app.utils.facebook import FacebookSDK
from google.appengine.ext import testbed
from app.settings import config
import unittest


class TestFacebookSDK(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.facebook = FacebookSDK()


class TestGetUrlLogin(TestFacebookSDK):

    """
        Classe de teste responsável por testar o metodo get_url_login
    """

    def setUp(self):
        self.url_login = self.facebook.get_url_login()

    def test_deve_retornar_url_de_login_com_app_id(self):
        self.assertTrue(config['APP_ID'] in self.url_login)

    def test_deve_retornar_url_de_login_com_redirect_uri(self):
        self.assertTrue(config['REDIRECT_URI'] in self.url_login)

    def test_deve_conter_variavel_state_na_uri(self):
        self.assertTrue('state' in self.url_login)

    def test_url_login_deve_conter_scope(self):
        SCOPE = ['user_birthday', ]
        for s in SCOPE:
            self.assertTrue(s in self.url_login)


class TestGetNumRandom(TestFacebookSDK):

    def test_numeros_gerados_devem_ser_diferentes(self):
        num1 = self.facebook._get_encode_random()
        num2 = self.facebook._get_encode_random()
        self.assertNotEqual(num1, num2)


class TestGenerateHash(TestFacebookSDK):

    def test_hashes_devem(self):
        num = self.facebook._get_encode_random()
        hash1 = self.facebook._generate_hash(num_random=num)
        hash2 = self.facebook._generate_hash(num_random=num)
        self.assertNotEqual(hash1, hash2)


class TestUrlOAuthToken(TestFacebookSDK):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_urlfetch_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def test_deve_ter_app_id(self):
        url_access_token = self.facebook._url_oauth_token('coidequalquerasdadsas')
        self.assertTrue(config['APP_ID'] in url_access_token)

    def test_deve_ter_app_secret(self):
        url_access_token = self.facebook._url_oauth_token('coidequalquerasdadsas')
        self.assertTrue(config['APP_SECRET'] in url_access_token)

    def test_deve_ter_redirect_uri(self):
        url_access_token = self.facebook._url_oauth_token('coidequalquerasdadsas')
        self.assertTrue(config['REDIRECT_URI'] in url_access_token)

    def test_get_access_token(self):
        token = self.facebook.get_access_token('asdadcodeqlqr1231')
        self.assertEqual(token, None)
