# encoding: utf-8

config = {

    # CONFIG DO FACEBOK
    'APP_ID': '655629421117845',
    'APP_SECRET': '53e1aba04d7c23f657060ed4f12a70e5',
    'REDIRECT_URI': "http://localhost:8080/",

    # SCOPE - PERMISSÕES NECESSÁRIAS PARA ACESSAR OS DADOS DO USUÁRIO NO FACEBOOK
    'SCOPE': ['user_birthday', 'user_events', 'friends_events',
              'email', 'publish_actions', 'user_about_me',
              'user_status', 'friends_birthday', 'create_event', 'rsvp_event', ],

    'KEY': 'key-qualquer-trocar-depois',

    # session/cookie
    'secret_key': '9389da06cafc5cb76e01085d0d3fbc0aaa3febe23e4c2116e08032dcdf131b6b',

    'DOMINIO': 'localhost',

    'webapp2_extras.sessions': {
        'secret_key': 'sua-super-secret-key',
    },
}
