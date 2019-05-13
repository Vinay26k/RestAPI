import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate(
    "C:\\Vinay Files\\Videos\\RestAPI\\firebase-api\\serviceAccountKey.json")
app = firebase_admin.initialize_app(
    cred, {'databaseURL': "https://fir-pyapi.firebaseio.com"})
# GET
ref = db.reference('tasks')
print(ref.get())
# PUT
ref.update({'-LelDvllP7cU0UW0nXkV/summary': 'blue'})
print(ref.get())
# POST
ref.push({
    'summary': 'purple',
    'description': 'checking'
})
print(ref.get())
# DELETE
ref.delete(ref.child('-LelF6ii0PAxqtMSCCGa'))
print(ref.get())
