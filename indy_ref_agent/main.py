from sanic import Sanic
from indy_ref_agent.api.message_bus import message_route

app = Sanic()

if __name__ == '__main__':
    app.blueprint(message_route)
    app.run(host='0.0.0.0', port=8000)
