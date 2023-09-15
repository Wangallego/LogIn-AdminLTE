from flask import Flask, render_template,request 

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello World"

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ""
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form:
        fullname = request.form['name']
        password = request.form['password']
        email = request.form['email']
        print(fullname)
        print(password)
        print(email)
        print(message)
        message = 'You have successfully registered!'
    elif request.method == 'POST':
        print(message)
        message = 'Please fill out the form!'

    return render_template('register.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
