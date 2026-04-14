# Flask User Management REST API

## 📌 Project Description

This project is a REST API built using Flask that performs CRUD operations on user data.  
The API allows adding, retrieving, updating, deleting, and searching users.

User data is stored permanently in a JSON file (`users.json`).

This project demonstrates understanding of:

- REST API development
- HTTP methods
- JSON handling
- File-based persistence
- API testing using Postman
- Backend logic implementation

---

## 🚀 Features

✔ Add new user  
✔ Get all users  
✔ Get user by ID  
✔ Update user  
✔ Delete user  
✔ Delete all users  
✔ Search user by name  
✔ Prevent duplicate email entries  
✔ Automatic ID generation  
✔ Automatic alphabetical sorting of users  
✔ Timestamp tracking  
✔ Persistent storage using JSON file  
✔ API status endpoint  

---

## 🛠 Tech Stack

- Python
- Flask
- JSON
- Postman (for testing)

---

## 📂 Project Structure
```
task4-flask-user-api/
│
├── app.py
├── users.json
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

Step 1:
pip install flask

Step 2:
python app.py

Server runs at:
http://127.0.0.1:5000

---

## 📡 API Endpoints

### Home Route
GET /

Returns API welcome message

---

### API Status
GET /status

Returns API running status and total users count

---

### Get All Users
GET /users

Returns sorted list of users

---

### Get User by ID
GET /users/<id>

Example:
GET /users/1

---

### Add New User
POST /users

Example JSON body:
{
"name": "Akanksha",
"email": "akanksha@gmail.com"
}

---

### Update User
PUT /users/<id>

Example:
PUT /users/1

JSON:
{
"name": "Updated Name"
}

---

### Delete User
DELETE /users/<id>

Example:
DELETE /users/1

---

### Delete All Users
DELETE /users

Deletes all stored users

---

### Search User
GET /search?name=akanksha

Returns matching users

---

## 📊 Example Response Format
{
"total_users": 2,
"users": [
{
"id": 1,
"name": "Akanksha",
"email": "akanksha@gmail.com"
}
]
}

---

## 📚 Key Concepts Used

- REST API
- HTTP Methods (GET, POST, PUT, DELETE)
- Flask Routing
- JSON Handling
- Status Codes (200, 201, 404, 409)
- Persistent Storage

---

## 🔮 Future Improvements

- Database integration (MySQL / MongoDB)
- Authentication system
- Frontend interface
- Deployment on cloud

---

## 👩‍💻 Author

Akanksha Jadhav  
MCA Student
