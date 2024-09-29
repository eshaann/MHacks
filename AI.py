import firebase_admin
from firebase_admin import credentials, firestore, storage
import requests

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/kanishkkandoi/Desktop/Hackathon/priv_key.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'mhacks17typeshit.appspot.com'
})

# Initialize Firestore and Storage
db = firestore.client()
bucket = storage.bucket()

def download_pdf_from_firestore(filename, collection_name, document_id):
    doc_ref = db.collection(collection_name).document(document_id)
    doc = doc_ref.get()

    if doc.exists:

        cloud_link = doc.to_dict().get('cloud_link')

        if cloud_link:

            response = requests.get(cloud_link)

            with open(filename, 'wb') as pdf_file:
                pdf_file.write(response.content)
            print(f"File {filename} downloaded successfully.")
        else:
            print("Cloud link not found in Firestore document.")
    else:
        print("Document does not exist.")

download_pdf_from_firestore('x.pdf', 'your_collection', 'your_document_id')