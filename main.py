from flask import Flask, json, jsonify
from flask_cors import CORS
import src.functions as functions
import src.GlobalInfo.Messages as Messages

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


@app.route("/biceps", methods=["GET"])
def getWeigth():
    try:
        print("entre a biceps")
        objResult = functions.weigth()
        return objResult
    except Exception as e :
        print("erroren getTest:" , e)
        return jsonify(Messages.err500)
    


@app.route("/WeihtAnalisis", methods=["GET"])
def getWeigthAnalisis():
    try:
        print("getting into analisis")
        objResult = functions.WeigthAnalysis()
        return objResult
    except Exception as e :
        print("erroren while getting the analisis:", e)
        return jsonify(Messages.err500)
    

@app.route("/BicepsAnalisis", methods=["GET"])
def getBicepsAnalisis():
    try:
        print("getting into analisis")
        objResult = functions.BicepsAnalysis()
        return objResult
    except Exception as e :
        print("erroren while getting the analisis:", e)
        return jsonify(Messages.err500)
    

@app.route("/ApartmentsLocation", methods=["GET"])
def getApartmentsLocation():
    try:
        print("getting into Apartments Location")
        objResult = functions.ApartmentsLocation()
        return objResult
    except Exception as e :
        print("erroren while getting the locations of the apartments... check this out:", e)
        return jsonify(Messages.err500)
    

@app.route("/AveragePrices", methods=["GET"])
def getApartmentsPrices():
    try:
        print("getting into Apartments pricing")
        objResult = functions.Apartmentsprices()
        return objResult
    except Exception as e :
        print("error while getting the prices and the m2 of the apartments... check this out:", e)
        return jsonify(Messages.err500)


@app.route("/Kmeans", methods=["GET"])
def getKmeans():
    try:
        print("getting into kmeans")
        objResult = functions.ApartmentsAnalysis()
        return objResult
    except Exception as e :
        print("error while getting the kmeans... check this out:", e)
        return jsonify(Messages.err500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
