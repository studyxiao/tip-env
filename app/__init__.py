from datetime import datetime
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.get("/")
def index():
    return {"msg": Config.dict(), 'time': datetime.now()}
