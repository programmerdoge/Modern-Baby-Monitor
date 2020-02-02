from pyrebase import pyrebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/home/jetson/modernbabymonitor-firebase-adminsdk-3rz0t-8228c36eaf.json")
firebase_admin.initialize_app(cred)

config = {
  "apiKey": "AIzaSyApL_nuUj724MSsi7g75v5XHBy52C4xs74",
  "authDomain": "modernbabymonitor.firebaseapp.com",
  "databaseURL": "https://modernbabymonitor.firebaseio.com",
  "serviceAccount": "/home/jetson/modernbabymonitor-firebase-adminsdk-3rz0t-8228c36eaf.json",
  "storageBucket": "modernbabymonitor.appspot.com"
}
firebase = pyrebase.initialize_app(config)


#https://github.com/thisbejim/Pyrebase