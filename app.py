import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = "secret_key_offline_mode"  # Session Key

# --- DATABASE SETUP ---
def init_db():
    with sqlite3.connect("users.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                mobile TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()

init_db()  # Start Database

# --- AUTH ROUTES ---

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()
            if user:
                session['user'] = username
                return redirect(url_for('dashboard'))
            else:
                flash("❌ Wrong Username or Password!", "error")
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mobile = request.form['mobile']
        try:
            with sqlite3.connect("users.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (username, password, mobile) VALUES (?, ?, ?)", (username, password, mobile))
                conn.commit()
            flash("✅ Account Created! Please Login.", "success")
            return redirect(url_for('login'))
        except:
            flash("⚠️ Username or Mobile already exists!", "error")
    return render_template('register.html')

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == 'POST':
        mobile = request.form['mobile']
        new_pass = request.form['new_password']
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET password = ? WHERE mobile = ?", (new_pass, mobile))
            if cursor.rowcount > 0:
                flash("✅ Password Reset Successful!", "success")
                return redirect(url_for('login'))
            else:
                flash("❌ Mobile number not found!", "error")
    return render_template('forgot.html')

@app.route('/find_user', methods=['GET', 'POST'])
def find_user():
    found_name = None
    if request.method == 'POST':
        mobile = request.form['mobile']
        with sqlite3.connect("users.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT username FROM users WHERE mobile = ?", (mobile,))
            user = cursor.fetchone()
            if user:
                found_name = user[0]
            else:
                flash("❌ Mobile number not found!", "error")
    return render_template('find_user.html', found_name=found_name)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# --- DASHBOARD & TOOL ---

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/tool')
def simple_tool():
    if 'user' not in session: return redirect(url_for('login'))
    return render_template('simple_tool.html')

if __name__ == '__main__':
    print("🚀 Offline App running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)