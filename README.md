# Overview

This project demonstrates how to integrate a Python application with a cloud database. The software connects to Google Firebase Firestore and performs basic CRUD operations: insert, update, delete, and query. The program is designed to show how cloud databases can be used to store and manage data without maintaining a local server.  

The purpose of this software is to strengthen my skills as a software engineer by learning how to interact with cloud services, handle data securely, and prepare for building scalable applications.  

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

The cloud database used in this project is **Google Firebase Firestore**, a NoSQL key/value store.  

**Database Structure:**  
- Collection: `users`  
  - Fields: `name`, `email`  
- Collection: `tasks`  
  - Fields: `user_id`, `title`, `description`, `status`  
- Each task is linked to a user by `user_id`.  
- The program demonstrates adding new users, linking tasks to users, updating tasks, deleting tasks, and querying both collections.  

# Development Environment

- Tools: Visual Studio Code, GitHub Desktop, Firebase Console  
- Programming Language: Python 3.13.2  
- Libraries: `firebase-admin` for Firestore integration  

# Useful Websites

- [Firebase Documentation](https://firebase.google.com/docs/firestore)  
- [Python Official Documentation](https://docs.python.org/3/)  
- [GitHub Guides](https://guides.github.com/)  
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)  

# Future Work

- Add user authentication for secure access.  
- Implement notifications when data changes in Firestore.  
- Expand database to include multiple related collections (e.g., users and tasks).  
