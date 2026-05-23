import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase with your Service Account JSON
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# CREATE
def add_task(title, description, status):
    doc_ref = db.collection("tasks").document()
    doc_ref.set({
        "title": title,
        "description": description,
        "status": status
    })
    print("Task added!")

# READ
def get_tasks():
    tasks = db.collection("tasks").stream()
    for task in tasks:
        print(f"{task.id} => {task.to_dict()}")

# UPDATE
def update_task(doc_id, status):
    db.collection("tasks").document(doc_id).update({"status": status})
    print("Task updated!")

# DELETE
def delete_task(doc_id):
    db.collection("tasks").document(doc_id).delete()
    print("Task deleted!")

# Test run
if __name__ == "__main__":
    add_task("Learn Firebase", "Practice CRUD operations", "pending")
    get_tasks()
