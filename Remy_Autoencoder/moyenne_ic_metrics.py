import json
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import pickle

# Charger les données depuis les fichiers JSON
metrics_file_path = "./metrics_autoencoder_model_batch1024_1.json"
metrics_file_path2 = "./metrics_autoencoder_model_batch1024_2.json"
metrics_file_path3 = "./metrics_autoencoder_model_batch1024_3.json"

with open(metrics_file_path, "r") as json_file:
    metrics_history1 = json.load(json_file)
with open(metrics_file_path2, "r") as json_file:
    metrics_history2 = json.load(json_file)
with open(metrics_file_path3, "r") as json_file:
    metrics_history3 = json.load(json_file)

# Extraire les métriques d'accuracy et de loss pour chaque fichier
losses1 = metrics_history1["metrics"]["loss"]
losses2 = metrics_history2["metrics"]["loss"]
losses3 = metrics_history3["metrics"]["loss"]


def confidence_interval(data,confidence):
    a = 1.0 * np.array(data)
    n = len(a)
    se = st.sem(a)
    h = se * st.t.ppf((1 + confidence) / 2.,n-1)
    return h


liste_loss_moy=[]
liste_intervalle=[]

for i in range (len(losses3)): 
    loss_moy=(losses1[i]+losses2[i]+losses3[i])/3
    liste_loss_moy.append(loss_moy)
    
    h=confidence_interval([losses1[i],losses2[i],losses3[i]],0.95)
    liste_intervalle.append(h)

with open('val_loss_autoencoder.pkl', 'wb') as file:
            # Utiliser pickle.dump() pour écrire l'objet dans le fichier
            pickle.dump(liste_loss_moy, file)

with open('val_ic_autoencoder.pkl', 'wb') as file:
            # Utiliser pickle.dump() pour écrire l'objet dans le fichier
            pickle.dump(liste_intervalle, file)
