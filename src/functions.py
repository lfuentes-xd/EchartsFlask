from flask import json, jsonify
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np


def weigth():
    try:
        with open('src/datos.json') as json_file:
            data = json.load(json_file) 
        age_groups = {
            "20-30": {"total": 0, "biceps": 0},
            "31-40": {"total": 0, "biceps": 0},
            "41-50": {"total": 0, "biceps": 0},
            "51+": {"total": 0, "biceps": 0},
        }

        for item in data: 
            if 20 <= item["edad"] <= 30:
                age_groups["20-30"]["total"] += 1
                age_groups["20-30"]["biceps"] += item["biceps"]
            elif 31 <= item["edad"] <= 40:
                age_groups["31-40"]["total"] += 1
                age_groups["31-40"]["biceps"] += item["biceps"]
            elif 41 <= item["edad"] <= 50:
                age_groups["41-50"]["total"] += 1
                age_groups["41-50"]["biceps"] += item["biceps"]
            else:
                age_groups["51+"]["total"] += 1
                age_groups["51+"]["biceps"] += item["biceps"]

        dataset_source = [
            ["Edad", "Promedio de bíceps", "Cantidad de personas"],
            ["20-30", round(age_groups["20-30"]["biceps"] / age_groups["20-30"]["total"], 2) if age_groups["20-30"]["total"] > 0 else 0, age_groups["20-30"]["total"]],
            ["31-40", round(age_groups["31-40"]["biceps"] / age_groups["31-40"]["total"], 2) if age_groups["31-40"]["total"] > 0 else 0, age_groups["31-40"]["total"]],
            ["41-50", round(age_groups["41-50"]["biceps"] / age_groups["41-50"]["total"], 2) if age_groups["41-50"]["total"] > 0 else 0, age_groups["41-50"]["total"]],
            ["51+", round(age_groups["51+"]["biceps"] / age_groups["51+"]["total"], 2) if age_groups["51+"]["total"] > 0 else 0, age_groups["51+"]["total"]]
        ]
        return jsonify(dataset_source)
    except Exception as e:
        return jsonify({"error": "Archivo no encontrado"}), 404
    
def WeigthAnalysis():
    try:
        with open('src/datos.json') as json_file:
             data = json.load(json_file) 

        weigth_analysis = {
            "Hombres":{
                "total": 0,
                "peso_total": 0,
                "peso_min": float('inf'),
                "peso_max": float('-inf')
            }, 
            "Mujeres":{
                "total": 0,
                "peso_total": 0,
                "peso_min": float('inf'),
                "peso_max": float('-inf')
            }
        }

        
        for item in data: 
            if item["sexo"] == "Hombre": 
                weigth_analysis["Hombres"]["total"] += 1
                weigth_analysis["Hombres"]["peso_total"] += item["peso"]
                weigth_analysis["Hombres"]["peso_min"] = min(weigth_analysis["Hombres"]["peso_min"], item["peso"])
                weigth_analysis["Hombres"]["peso_max"] = max(weigth_analysis["Hombres"]["peso_max"], item["peso"])
            elif item["sexo"] == "Mujer":
                weigth_analysis["Mujeres"]["total"] += 1
                weigth_analysis["Mujeres"]["peso_total"] += item["peso"]
                weigth_analysis["Mujeres"]["peso_min"] = min(weigth_analysis["Mujeres"]["peso_min"], item["peso"])
                weigth_analysis["Mujeres"]["peso_max"] = max(weigth_analysis["Mujeres"]["peso_max"], item["peso"])

        weigth_analysis["Hombres"]["peso_promedio" ] = round(weigth_analysis["Hombres"]["peso_total"] / weigth_analysis["Hombres"]["total"], 2) if weigth_analysis["Hombres"]["total"] > 0 else 0
        weigth_analysis["Mujeres"]["peso_promedio"] = round(weigth_analysis["Mujeres"]["peso_total"] / weigth_analysis["Mujeres"]["total"], 2) if weigth_analysis["Mujeres"]["total"] > 0 else 0

        return jsonify(weigth_analysis)
    except Exception as e:
        return jsonify({"error": "Archivo no encontrado"}), 404
    

def BicepsAnalysis():
    try:
        with open('src/datos.json') as json_file:
            data = json.load(json_file)
        
        peso = [item['peso'] for item in data]
        biceps = [item['biceps'] for item in data]

        result = {
            'peso': peso,
            'biceps': biceps
        }

        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({"error": "Archivo no encontrado"}), 404


def ApartmentsLocation():
    try:            
        with open('src/Apartmens.json') as json_file:
            data = json.load(json_file)
        df = pd.DataFrame(data)
        
        #checamos si estan terminados oh no.
        df_terminados = df[df['terminado_flag'] == 'si']

        Ubications = df_terminados["ubicacion"].value_counts()

        res = [
            {"name": location, "value":count}
            for location, count in Ubications.items()
        ]

        return jsonify(res), 200
    except Exception as e:
        return jsonify({"error": "Archivo no encontrado"}), 404
    
def Apartmentsprices():
    try: 
        with open('src/Apartmens.json') as json_file:
            data = json.load(json_file)
        df = pd.DataFrame(data)

        promedio_por_estrato = df.groupby('estrato').agg(
            precio_promedio=('precio', 'mean'),
            mt2_promedio=('mt2', 'mean')
        ).reset_index()

        return jsonify(promedio_por_estrato.to_dict(orient='records'))  
    except Exception as e:
        return jsonify({"error": "Archivo no encontrado"}), 404  
    
def ApartmentsAnalysis():
    try:
        with open('src/Apartmens.json') as json_file:
            data = json.load(json_file)
       
        price = [apartment['precio'] for apartment in data]
        meters = [apartment['mt2'] for apartment in data]
        
        
        X = np.array(list(zip(price, meters)))

        Kmeans = KMeans(n_clusters=3)
        Kmeans= Kmeans.fit(X)
        labels= Kmeans.predict(X)
        centroids = Kmeans.cluster_centers_
        
        colors=["m.","r.","c.","y.","b."]

        for i in range(len(X)):
            print("Coordenada: ",X[i],"Label: ",labels[i])
            plt.plot(X[i][0],X[i][1], colors[labels[i]],markersize=10)
            
        plt.scatter(centroids[:,0],centroids[:,1],marker="X",s=50,linewidths=2,zorder=10)
        plt.show()
        return jsonify({"message": "success"})
    except Exception as e:
        print("the error is: ", e)
        return jsonify({"error": "theres an error"})