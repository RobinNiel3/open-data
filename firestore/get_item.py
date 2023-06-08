from google.cloud import firestore

# Instantiation du client
db = firestore.Client(project="brt-svc-data-platform-dev")

# Création de la référence au document
doc_ref = db.collection("sources").document("0cK5UJflqKHJkVoCOhcJ")

# Récupération du document
doc = doc_ref.get()

if doc.exists:
    print(f"Document data: {doc.to_dict()}")
else:
    print("No such document!")
