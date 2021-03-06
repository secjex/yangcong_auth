from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('bind', '/')
    config.add_route('auth_page', '/auth_page/')
    config.add_route('check', '/check')
    config.add_route('offline_auth', '/offline_auth')
    config.add_route('online_auth', '/online_auth')
    config.scan()
    return config.make_wsgi_app()
