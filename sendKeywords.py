#receive a filename from an api call, and then find the keywords from that pdf 
#and then upload keyword to the database. 
from flask import Flask, request
import PDFparser
import firebase_admin
from firebase_admin import firestore
from google.cloud import storage

app = Flask(__name__)

cred = firebase_admin.credentials.Certificate('priv_key.json')
firebase_admin.initialize_app(cred)

project_id = "mhacks17typeshit"
bucket_name = "mhacks17typeshit.appspot.com"
storage_client = storage.Client(project=project_id)
bucket = storage_client.bucket(bucket_name)


db = firestore.client()


@app.route("/parseKeywords", methods=["POST"])
def find_keywords():
    email = request.json.get('email')  # Access email from JSON request body
    fileName = request.json.get('fileName')
    video_path = fileName
    blob = bucket.blob(video_path)
    # Download the video to a local file
    blob.download_to_filename(fileName)
    words = PDFparser.gen_keywords(fileName)
    print(words)
    doc_ref = db.collection('FileKeywords').document()
    doc_ref.set({
        'email': email,
        'fileName': fileName,
        'keywords': words
    })
    return f"Keywords for {fileName} uploaded for {email}", 201  # Return success message

@app.route("/findFile", methods=["GET"])
def find_pdf():
    email = request.json.get('email') # Access email from JSON request body
    keywords = request.json.get('keywords')
    
    
    

if __name__ == "__main__":
    app.run(debug=True)