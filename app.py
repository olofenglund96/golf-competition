import tornado.ioloop
import tornado.web
import os
from dotenv import load_dotenv
import pandas as pd
from db import MongoDB

db = None

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        players = db.get_players()
        
        self.render("index.html", players=players)

def make_app():
    load_dotenv()

    settings = {
        "template_path": os.path.join(os.path.dirname(__file__), "templates")
    }
    global db

    db = MongoDB(os.getenv("MONGO_CONN_STRING"))

    return tornado.web.Application([
        (r"/", MainHandler),
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()