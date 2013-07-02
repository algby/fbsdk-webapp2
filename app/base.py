# encoding: utf-8
from webapp2_extras import sessions
from webapp2_extras import jinja2
import webapp2


class BaseHandler(webapp2.RequestHandler):

    """
        Classe generica que implementa metodos de config
        para poder utilizar o jinja2
    """
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def render_template(self, filename, **template_args):
        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        # args default
        # template_args['chave'] = config['valor']
        self.response.out.write(self.jinja2.render_template(filename, **template_args))

    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)

        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()
