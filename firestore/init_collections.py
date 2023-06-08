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
     "thumbnail": "https://img.brut.media/thumbnail/le-concert-de-booba-au-maroc-annule-0552cb44-d89b-4921-8c32-22cdca081d79-f8a804be-db42-4c1d-a871-520a8e9790af-portrait-auto.jpg?ts=20230607-151508",
     "sources":[{"label": "Le Monde - Au Maroc le concert de Booba annule apres un appel au boycott lance par une mouvance nationaliste", "url":"https://www.lemonde.fr/afrique/article/2023/06/07/au-maroc-le-concert-de-booba-annule-apres-un-appel-au-boycott-lance-par-une-mouvance-nationaliste_6176628_3212.html#:~:text=Un%20concert%20de%20Booba%20programm%C3%A9,qui%20avaient%20achet%C3%A9%20leur%20billet."},
            {"label": "Youtube - Booba - É.L.É.P.H.A.N.T" , "url": "https://www.youtube.com/watch?v=Tk20thb6z-g"},
            {"label": "Youtube - Booba - Génération Assassin (Clip Officiel)" , "url":"https://www.youtube.com/watch?v=rZkPJ9LMiwA"},
            {"label": "TelQuel - Le concert de Booba a casablanca est officiellement annule" , "url":"https://telquel.ma/instant-t/2023/06/06/le-concert-de-booba-a-casablanca-est-officiellement-annule_1815724/"},
            {"label": "Change.org - Pétition pour annuler le concert de Booba" , "url":"https://www.change.org/p/p%C3%A9tition-pour-annuler-le-concert-de-booba-pr%C3%A9vu-le-21-06-2022-%C3%A0-casablanca"}], 
     "date": firestore.SERVER_TIMESTAMP},
    {"title": "Des menhirs détruits pour construire un Mr.Bricolage à Carnac.", 
     "id": "da0e3e54-c960-4865-87c9-e496f1ee7514",
     "thumbnail": "https://img.brut.media/thumbnail/des-menhirs-detruits-pour-construire-un-mr-bricolage-a-carnac--da0e3e54-c960-4865-87c9-e496f1ee7514-a54920d0-d1a1-44b6-9dd8-98178d4b0ad1-portrait-auto.jpg?ts=20230607-200852",
     "sources": [
         {"label": "Ouest-France - A carnac 39 menhirs detruits pour construire un magasin" , "url": "https://www.ouest-france.fr/culture/patrimoine/a-carnac-39-menhirs-detruits-pour-construire-un-magasin-que-sest-il-passe-ac3d997c-03bc-11ee-bfa0-5e45e3198685"},
         {"label": "Sites et Monuments - Carnac, aménagements brutaux aux abords des alignements de menhirs" , "url": "https://www.sitesetmonuments.org/carnac-amenagements-brutaux-aux-abords-des-alignements-de-menhirs"}], 
     "date": firestore.SERVER_TIMESTAMP},
    {"title": "En Mauritanie, la mort d’un jeune noir provoque de violentes manifestations", 
     "id": "37e36a4c-a797-4d83-85a7-21474ccf6aa4",
     "thumbnail": "https://img.brut.media/thumbnail/que-se-passe-t-il-en-mauritanie--34a3e6be-1a62-4682-9146-cf1e7f4d447a-74db2e05-757d-4d2f-b966-2381524ccb67-portrait-auto.jpg?ts=20230607-125002",
     "sources": [
         {"label": "Jeune Afrique - En Mauritanie, internet coupé après de violentes manifestations" , "url": "https://www.jeuneafrique.com/1449753/politique/en-mauritanie-internet-coupe-apres-de-violentes-manifestations/"},
         {"label": "RFI - Mauritanie: vives protestations suite à la mort d'un jeune noir, après son arrestation par la police" , "url": "https://www.rfi.fr/fr/afrique/20230531-mauritanie-vives-protestations-suite-%C3%A0-la-mort-d-un-jeune-noir-apr%C3%A8s-son-arrestation-par-la-police"},
         {"label": "Twitter Amnesty West Center Africa - Restriction internet" , "url": "https://twitter.com/AmnestyWARO/status/1666071576935104512?s=20"}], 
     "date": firestore.SERVER_TIMESTAMP},
    {"title": "Canada: des messages anti-tabac imprimés sur les cigarettes", 
     "id": "8fe1f598-266e-4eba-afeb-e1eed2bc1f97",
     "thumbnail": "https://img.brut.media/thumbnail/des-messages-de-prevention-directement-imprimes-sur-les-cigarettes-au-canada--8fe1f598-266e-4eba-afeb-e1eed2bc1f97-7682d81d-5ca8-4f5f-bec4-acd9fc76b7cd-portrait-auto.jpg?ts=20230601-151510",
     "sources": [
         {"label": "France 24 - Le Canada va exiger qu'un avertissement soit imprimé sur chaque cigarette" , "url": "https://www.8fe1f598-266e-4eba-afeb-e1eed2bc1f97.com/fr/info-en-continu/20230531-le-canada-va-exiger-qu-un-avertissement-soit-imprimé-sur-chaque-cigarette"}], 
     "date": firestore.SERVER_TIMESTAMP},
    {"title": "L'accord de 1968 entre la France et l'Algérie ? ", 
     "id": "ffcd14df-af7f-4086-b53a-ce913fdb5546",
     "thumbnail": "https://img.brut.media/thumbnail/-que-prevoit-l-accord-de-1968-entre-la-france-et-l-algerie--a0304126-45da-411c-bc39-17c337bad4ac-2c194841-7d86-46d7-acd1-7378bc8599cf.thumbnail-2c194841-7d86-46d7-acd1-7378bc8599cf-portrait.jpg?ts=20230608-114806",
     "sources": [
         {"label": "Gouvernement France, Ministere de l'Intérieur - Accord franco-algérien du 27 décembre 1968 modifié" , "url": "https://www.immigration.interieur.gouv.fr/content/download/119881/961556/file/Accord-Franco-Algerien-27-decembre-1968-19680021.pdf"},
         {"label": "Echorouk - Immigration: Que prévoit l’accord de 1968 liant la France et l’Algérie, qu’Edouard Philippe remet en cause ?" , "url": "https://www.echoroukonline.com/immigration-que-prevoit-laccord-de-1968-liant-la-france-et-lalgerie-quedouard-philippe-remet-en-cause"}], 
     "date": firestore.SERVER_TIMESTAMP},
    {"title": "L'État de Rio au Brésil adopte une loi pour interrompre les matchs en cas de comportements racistes dans les stades.", 
     "id": "b5bb3606-cc23-4f6e-ba42-9619294f13ae",
     "thumbnail": "https://img.brut.media/thumbnail/l-etat-de-rio-au-bresil-adopte-une-loi-pou-interrompre-les-matchs-en-cas-de-comportements-racistes-dans-les-stades--b5bb3606-cc23-4f6e-ba42-9619294f13ae-faba1dbf-d07a-4222-bdcf-f1be36234d80-portrait-auto.jpg?ts=20230607-182118",
     "sources": [
         {"label": "Scielo - Anti-racism legislation in Brazil: the role of the Courts in the reproduction of the myth of racial democracy" , "url": "https://www.jeuneafrique.com/1449753/politique/en-mauritanie-internet-coupe-apres-de-violentes-manifestations/"}], 
     "date": firestore.SERVER_TIMESTAMP},
]

# Ajout des données à la collection
for data in data_list:
    doc_ref = sources_ref.document(data["id"])
    doc_ref.set(data)

