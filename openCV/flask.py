from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sign_up.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    # Here you can perform database operations or any other necessary processing with the form data
    
    # For this example, let's just print the form data
    print("New user signed up with username:", username)
    print("Email:", email)
    print("Password:", password)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

                                             