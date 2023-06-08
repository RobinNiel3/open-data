from google.cloud import firestore

# Instantiation du client
db = firestore.Client(project="brt-svc-data-platform-dev")

# Création de la référence à la collection
sources_ref = db.collection("sources")

# Création de l'objet à ajouter (changez-le en fonction de vos besoins)
data = {
    "nom": "source1",
    "url": "https://www.source1.com",
    "date": firestore.SERVER_TIMESTAMP,  # Timestamp du serveur
}

# Ajout de l'objet à la collection
doc_ref = sources_ref.add(data)[1]  # [1] pour récupérer seulement la référence du document

print(f"L'élément a été ajouté avec l'ID : {doc_ref.id}")
