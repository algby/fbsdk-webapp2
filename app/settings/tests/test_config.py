# encoding: utf-8
from app.settings import config
from app.settings.localhost import config as config_local
from app.settings.production import config as config_prod
from app.settings.testing import config as config_test
import unittest


class TestConfigLocalhost(unittest.TestCase):

    def test_deve_conter_app_id(self):
        self.assertEqual(config_local['APP_ID'], '655629421117845')

    def test_deve_conter_app_secret(self):
        self.assertEqual(config_local['APP_SECRET'], '53e1aba04d7c23f657060ed4f12a70e5')

    def test_deve_conter_scope_do_facebook(self):
        """
            A aplicação deve ter esse scope configurado para acessar
            os dados do usuário via Facebook
        """
        SCOPE = ['user_birthday', 'user_events', 'friends_events',
                 'email', 'publish_actions', 'user_about_me',
                 'user_status', 'friends_birthday', 'create_event', 'rsvp_event', ]

        for scope in SCOPE:
            self.assertTrue(scope in config_local['SCOPE'])

    def test_redirect_uri_deve_estar_correta(self):
        self.assertEqual(config_local['REDIRECT_URI'], 'http://localhost:8080/')


class TestConfigProduction(unittest.TestCase):

    def test_deve_conter_app_id(self):
        self.assertEqual(config_prod['APP_ID'], '523258614382919')

    def test_deve_conter_app_secret(self):
        self.assertEqual(config_prod['APP_SECRET'], 'e98a0936ccd75fb70f2cfa4a253f8d5e')

    def test_deve_conter_scope_do_facebook(self):
        """
            A aplicação deve ter esse scope configurado para acessar
            os dados do usuário via Facebook
        """
        SCOPE = ['user_birthday', 'user_events', 'friends_events',
                 'email', 'publish_actions', 'user_about_me',
                 'user_status', 'friends_birthday', 'create_event', 'rsvp_event', ]

        for scope in SCOPE:
            self.assertTrue(scope in config_prod['SCOPE'])

    def test_redirect_uri_deve_estar_correta(self):
        self.assertEqual(config_prod['REDIRECT_URI'], 'http://www.sonasboas.com/')


class TestConfigTesting(unittest.TestCase):

    def test_deve_conter_app_id(self):
        self.assertEqual(config_test['APP_ID'], '166548656856977')

    def test_deve_conter_app_secret(self):
        self.assertEqual(config_test['APP_SECRET'], '196e703757a48e1624c73d32959083e0')

    def test_deve_conter_scope_do_facebook(self):
        """
            A aplicação deve ter esse scope configurado para acessar
            os dados do usuário via Facebook
        """
        SCOPE = ['user_birthday', 'user_events', 'friends_events',
                 'email', 'publish_actions', 'user_about_me',
                 'user_status', 'friends_birthday', 'create_event', 'rsvp_event', ]

        for scope in SCOPE:
            self.assertTrue(scope in config_test['SCOPE'])

    def test_redirect_uri_deve_estar_correta(self):
        self.assertEqual(config_test['REDIRECT_URI'], 'http://localhost/')


class TestConfig(unittest.TestCase):

    def test_deve_importar_config_ambiente_de_test(self):
        self.assertTrue(config)

    def test_deve_conter_app_id(self):
        self.assertTrue('APP_ID' in config)

    def test_deve_conter_app_secret(self):
        self.assertTrue('APP_SECRET' in config)
