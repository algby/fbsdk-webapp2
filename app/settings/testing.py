# encoding: utf-8
config = {

    # CONFIG DO FACEBOOK
    'APP_ID': '166548656856977',
    'APP_SECRET': '196e703757a48e1624c73d32959083e0',
    'REDIRECT_URI': "http://localhost/",

    # SCOPE - PERMISSÕES NECESSÁRIAS PARA ACESSAR OS DADOS DO USUÁRIO NO FACEBOOK
    'SCOPE': ['user_birthday', 'user_events', 'friends_events',
              'email', 'publish_actions', 'user_about_me',
              'user_status', 'friends_birthday', 'create_event', 'rsvp_event', ],

    'KEY': 'key-qualquer-trocar-depois',

    'secret_key': '245affd236be479ba7a81d4e38240c9cbf248de087f421506ca59273e5197c36',

    'DOMINIO': 'localhost',

    'webapp2_extras.sessions': {
        'secret_key': 'sua-super-secret-key',
    },

}
