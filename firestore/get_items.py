from google.cloud import firestore

# Instantiation du client
db = firestore.Client(project="brt-svc-data-platform-dev")

# Récupération de tous les documents dans la collection 'sources' où le champ 'nom' est 'source1'
docs = db.collection("sources").where("nom", "==", "source1").stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
