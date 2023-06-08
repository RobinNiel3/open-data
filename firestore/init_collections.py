from google.cloud import firestore

# Instantiation du client
db = firestore.Client(project="brt-svc-data-platform-dev")

# Référence de la collection
sources_ref = db.collection('sources')

# Récupération de tous les documents dans la collection
docs = sources_ref.stream()

# Suppression de chaque document
for doc in docs:
    doc.reference.delete()
    
# Liste des données à ajouter
data_list = [
    {"title": "Le concert de Booba au Maroc annulé par les autorités locales après des appels au boycott.", 
     "id": "eb83e748-344e-4cf6-8812-dd6bafc3410a", 
     "sources":["https://www.lemonde.fr/afrique/article/2023/06/07/au-maroc-le-concert-de-booba-annule-apres-un-appel-au-boycott-lance-par-une-mouvance-nationaliste_6176628_3212.html#:~:text=Un%20concert%20de%20Booba%20programm%C3%A9,qui%20avaient%20achet%C3%A9%20leur%20billet.",
            "https://www.youtube.com/watch?v=Tk20thb6z-g",
            "https://www.youtube.com/watch?v=rZkPJ9LMiwA",
            "https://telquel.ma/instant-t/2023/06/06/le-concert-de-booba-a-casablanca-est-officiellement-annule_1815724/",
            "https://www.change.org/p/p%C3%A9tition-pour-annuler-le-concert-de-booba-pr%C3%A9vu-le-21-06-2022-%C3%A0-casablanca"], 
     "date": firestore.SERVER_TIMESTAMP},
    {"title": "Des menhirs détruits pour construire un Mr.Bricolage à Carnac.", 
     "id": "da0e3e54-c960-4865-87c9-e496f1ee7514",
     "sources": ["https://www.ouest-france.fr/culture/patrimoine/a-carnac-39-menhirs-detruits-pour-construire-un-magasin-que-sest-il-passe-ac3d997c-03bc-11ee-bfa0-5e45e3198685",
                "https://www.sitesetmonuments.org/carnac-amenagements-brutaux-aux-abords-des-alignements-de-menhirs"], 
     "date": firestore.SERVER_TIMESTAMP},
]

# Ajout des données à la collection
for data in data_list:
    doc_ref = sources_ref.document(data["id"])
    doc_ref.set(data)

