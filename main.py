from services import get_concursos_pci
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(get_concursos_pci())

def create_app():
    return app
