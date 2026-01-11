---

# 🔐 Zero Trust Network Access (ZTNA) – Flask Web Application

## 📌 Project Description

This project demonstrates the **Zero Trust Network Access (ZTNA)** security model using a **Flask-based web application**.
The system follows the principle of **“Never Trust, Always Verify”**, ensuring that every user and every request is authenticated, authorized, and continuously verified before granting access to protected resources.

Unlike traditional VPN-based access, this ZTNA implementation provides **application-level access control** using identity-based policies.

---

## 🎯 Key Objectives

* Implement Zero Trust principles
* Enforce identity-based authentication
* Apply role-based access control (RBAC)
* Demonstrate least-privilege access
* Provide a web-based UI for testing

---

## 🏗️ System Architecture

```
User (Browser)
   ↓
Authentication (Login)
   ↓
JWT Token Issuance
   ↓
ZTNA Controller
   ↓
Policy Engine (RBAC)
   ↓
Protected Resources
```

---

## 🛠️ Technology Stack

* **Programming Language:** Python 3
* **Framework:** Flask
* **Authentication:** JWT (JSON Web Tokens)
* **Authorization:** Role-Based Access Control (RBAC)
* **Database:** SQLite
* **Frontend:** HTML (Flask Templates)
* **Environment:** Windows + VS Code

---

## 📂 Project Structure

```
ZTNA-Project/
│
├── app.py                 # Main Flask application
├── auth.py                # JWT authentication logic
├── policy.py              # ZTNA policy engine
├── database.db            # SQLite user database
├── requirements.txt       # Python dependencies
│
├── templates/
│   ├── login.html         # Login page
│   └── dashboard.html     # User dashboard
│
└── README.md              # Project documentation
```

---

## 👤 User Roles & Access Policies

| Role     | Admin Panel | Employee Dashboard | Guest Page |
| -------- | ----------- | ------------------ | ---------- |
| Admin    | ✅ Allowed   | ✅ Allowed          | ✅ Allowed  |
| Employee | ❌ Denied    | ✅ Allowed          | ✅ Allowed  |
| Guest    | ❌ Denied    | ❌ Denied           | ✅ Allowed  |

---

## 🚀 Installation & Execution

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ZTNA-Project.git
cd ZTNA-Project
```

---

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install flask pyjwt werkzeug
```

---

### 4️⃣ Run the Application

```bash
python app.py
```

---

### 5️⃣ Access in Browser

```
http://127.0.0.1:5000/
```

---

## 🔑 Test Credentials

| Username | Password | Role     |
| -------- | -------- | -------- |
| admin    | admin123 | Admin    |
| employee | emp123   | Employee |
| guest    | guest123 | Guest    |

---

## 🧪 Testing the ZTNA Model (Web)

1. Login using any user
2. Access different resources from dashboard
3. Observe **access granted or denied** based on role
4. Wait for token expiry to see **continuous verification**
5. Logout and attempt direct access (should be blocked)

---

## 🔍 Zero Trust Features Demonstrated

* No implicit trust
* Authentication on every session
* Authorization on every request
* Least-privilege access
* Continuous token verification
* Micro-segmentation of resources

---

## 📊 ZTNA vs Traditional VPN

| Feature      | VPN          | ZTNA              |
| ------------ | ------------ | ----------------- |
| Trust Model  | Implicit     | Zero Trust        |
| Access Scope | Network-wide | Application-level |
| Security     | Medium       | High              |
| Scalability  | Limited      | High              |

---

## 🔮 Future Enhancements

* Multi-Factor Authentication (MFA)
* Device posture validation
* Access logging & monitoring
* Bootstrap UI
* Cloud deployment (AWS/Azure)
* Docker containerization

---

## 📜 License

This project is for **educational purposes only**.

---

## 👨‍💻 Author

**Prakanth**
Zero Trust Network Access Project
Cyber Security / Network Security

---

