import pyrebase 

config = {
    'apiKey': "AIzaSyC4HW9KqmWWZwtOLMgF6Wrx7Vm75d9_HIs",
    'authDomain' : "playground-e7b0e.firebaseapp.com",
    'databaseURL' : "https://playground-e7b0e-default-rtdb.firebaseio.com",
    'projectId': "playground-e7b0e",
    'storageBucket': "playground-e7b0e.appspot.com",
    'messagingSenderId': "890124160113",
    'appId': "1:890124160113:web:f3d979ab80e8268b8a9fd0",
    'measurementId': "G-PJWPVP0JP8"
}

fire = pyrebase.initialize_app(config)
conexao = fire.database()