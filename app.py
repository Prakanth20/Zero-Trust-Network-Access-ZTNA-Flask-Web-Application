from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import sqlite3
from auth import generate_token, verify_token
from policy import policy_check

app = Flask(__name__)
app.secret_key = "ztna_web_secret"

# Database function
def get_user(username, password):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(
        "SELECT username, role FROM users WHERE username=? AND password=?",
        (username, password)
    )
    user = c.fetchone()
    conn.close()
    return user

# ---------------- WEB ROUTES ---------------- #

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = get_user(username, password)
    if user:
        token = generate_token(user[0], user[1])
        session['token'] = token
        return redirect(url_for('dashboard'))

    return "Invalid credentials", 401

@app.route('/dashboard')
def dashboard():
    token = session.get('token')
    if not token:
        return redirect(url_for('home'))

    decoded = verify_token(token)
    if not decoded:
        return "Session expired. Login again."

    return render_template(
        "dashboard.html",
        user=decoded['user'],
        role=decoded['role']
    )

@app.route('/access/<resource>')
def access(resource):
    token = session.get('token')
    if not token:
        return redirect(url_for('home'))

    decoded = verify_token(token)
    if not decoded:
        return "Invalid or expired token"

    if policy_check(decoded['role'], resource):
        return f"✅ Access granted to {resource}"
    else:
        return f"❌ Access denied to {resource}"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# ---------------- API ROUTES (OPTIONAL) ---------------- #

@app.route('/api/login', methods=['POST'])
def api_login():
    data = request.json
    user = get_user(data['username'], data['password'])
    if user:
        token = generate_token(user[0], user[1])
        return jsonify({"token": token})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
