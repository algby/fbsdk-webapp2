# encoding: utf-8

config = {

    # CONFIG DO FACEBOK
    'APP_ID': '480963215313040',
    'APP_SECRET': '9adcfc8fe8419dfc64d8c83f96418e5c',
    'REDIRECT_URI': "http://localhost:8080/",

    # SCOPE - PERMISSÕES NECESSÁRIAS PARA ACESSAR OS DADOS DO USUÁRIO NO FACEBOOK
    'SCOPE': ['user_birthday', ],

    'KEY': 'key-qualquer-trocar-depois',

    # session/cookie
    'secret_key': '9389da06cafc5cb76e01085d0d3fbc0aaa3febe23e4c2116e08032dcdf131b6b',

    'DOMINIO': 'localhost',

    'webapp2_extras.sessions': {
        'secret_key': 'sua-super-secret-key',
    },
}
