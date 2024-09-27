from flask import Flask, json, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/data", methods=["GET"])
def data():
    try:
        with open('src/datos.json') as json_file:
            data = json.load(json_file) 
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Archivo no encontrado"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error al decodificar el JSON"}), 500
    
@app.route("/Apartments", methods=["GET"])
def apartments():
    try:
        with open('src/Apartmens.json') as json_file:
            data = json.load(json_file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Archivo no encontrado"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error al decodificar el JSON"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
