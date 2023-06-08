def get_item(db_client, collection_name, key):
    doc_ref = db_client.collection(collection_name).document(key)
    doc = doc_ref.get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
        return doc.to_dict()
    else:
        print("No such document!")
        return None