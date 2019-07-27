from views import get_stats, receive_message_from_user, send_message_to_user

def setup_routes(app):
    app.router.add_get('/stats', get_stats)
    app.router.add_post('/incoming', receive_message_from_user)
    app.router.add_post('/outgoing', send_message_to_user)