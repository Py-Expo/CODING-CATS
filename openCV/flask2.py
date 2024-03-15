from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login page.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Here you can add your authentication logic.
    # For simplicity, let's just print the submitted username and password.
    print("Username:", username)
    print("Password:", password)
    
    # Redirect to a success page after login
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)
