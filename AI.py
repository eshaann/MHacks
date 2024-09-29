import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from google.cloud import storage as gcs

# Initialize Firebase Admin SDK
cred = credentials.Certificate('priv_key.json')
firebase_admin.initialize_app(cred, {
    'storageBucket': 'mhacks17typeshit.appspot.com'
})

# Initialize Google Cloud Storage client
storage_client = gcs.Client()

# Get a reference to the file in storage
bucket = storage_client.bucket('mhacks17typeshit')
blob = bucket.blob('gs://mhacks17typeshit.appspot.com/Safari.pdf')

# Download the file to a local file
with open('downloaded_file.pdf', 'wb') as f:
    blob.download_to_file(f)

print('File downloaded successfully!')