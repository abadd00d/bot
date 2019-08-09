from views import get_stats, receive_message_from_user, send_message_to_user

def setup_routes(app):
    app.router.add_get(app['config']['server']['routes']['stats'], get_stats)
    app.router.add_post(app['config']['server']['routes']['in'], receive_message_from_user)
    app.router.add_post(app['config']['server']['routes']['out'], send_message_to_user)