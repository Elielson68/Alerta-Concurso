from services import get_concursos_pci
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(get_concursos_pci())

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
