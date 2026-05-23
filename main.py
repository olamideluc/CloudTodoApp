import firebase_admin
from firebase_admin import credentials, firestore
import time

# Initialize Firebase with your Service Account JSON
cred = credentials.Certificate("serviceAccount.json")
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# ---------------- USERS COLLECTION ----------------

def add_user(name, email):
    """
    Adds a new user to the 'users' collection.
    Each user has a name and email.
    Returns the document ID of the new user.
    """
    doc_ref = db.collection("users").document()
    doc_ref.set({
        "name": name,
        "email": email
    })
    print("User added!")
    return doc_ref.id

def get_users():
    """
    Retrieves all users from the 'users' collection.
    """
    users = db.collection("users").stream()
    for user in users:
        print(f"{user.id} => {user.to_dict()}")

# ---------------- TASKS COLLECTION ----------------

def add_task(user_id, title, description, status):
    """
    Adds a new task to the 'tasks' collection.
    Each task is linked to a user by user_id.
    """
    doc_ref = db.collection("tasks").document()
    doc_ref.set({
        "user_id": user_id,
        "title": title,
        "description": description,
        "status": status
    })
    print("Task added!")
    return doc_ref.id

def get_tasks():
    """
    Retrieves all tasks from the 'tasks' collection.
    """
    tasks = db.collection("tasks").stream()
    for task in tasks:
        print(f"{task.id} => {task.to_dict()}")

def update_task(doc_id, status):
    """
    Updates the status of a task by document ID.
    """
    db.collection("tasks").document(doc_id).update({"status": status})
    print("Task updated!")

def delete_task(doc_id):
    """
    Deletes a task by document ID.
    """
    db.collection("tasks").document(doc_id).delete()
    print("Task deleted!")

# ---------------- NOTIFICATIONS ----------------

def watch_tasks():
    """
    Sets up a listener to receive notifications when tasks change.
    Prints messages when tasks are added, modified, or removed.
    """
    def on_snapshot(col_snapshot, changes, read_time):
        print("---- Notification: Tasks changed ----")
        for change in changes:
            if change.type.name == "ADDED":
                print(f"New task: {change.document.id} => {change.document.to_dict()}")
            elif change.type.name == "MODIFIED":
                print(f"Updated task: {change.document.id} => {change.document.to_dict()}")
            elif change.type.name == "REMOVED":
                print(f"Deleted task: {change.document.id}")

    db.collection("tasks").on_snapshot(on_snapshot)

# ---------------- DEMO RUN ----------------

if __name__ == "__main__":
    # Add a sample user and capture their ID
    user_id = add_user("Olamide", "olassignibo@example.com")

    print("---- USERS ----")
    get_users()

    print("---- TASKS ----")
    task_id = add_task(user_id, "Learn Firebase", "Practice CRUD operations", "pending")
    get_tasks()

    # Start watching for notifications
    print("---- STARTING TASK WATCHER ----")
    watch_tasks()

    # Keep the program alive to listen for changes
    print("Listening for task changes... (Press Ctrl+C to stop)")
    while True:
        time.sleep(1)
