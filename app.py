from flask import Flask, render_template, request, session,redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask (__name__)

app.secret_key = 'key'

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'


mysql= MySQL(app)


@app.route("/")
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('shopping-cart')
def shopping():
    return render_template('shoping-cart.html')

@app.route('/features')
def features():
    return render_template('product-cart.html')

@app.route('/reg', methods=['GET','POST'])
def reg():
    if request.method == "POST" and "username" in request.form and "email" in request.form and "password" in request.form:
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO ecommerce  VALUES (%s, %s, %s)', (username, email, password))
        mysql.connection.commit()
        msg = "Registration Successful"
        return render_template('login.html')
    elif request.method == "POST":
        msg = "please fill out form "
        return render_template('register.html', msg = msg)

@app.route ('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form ['email']
        password = request.form ['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT* FROM ecommerce WHERE email = %s AND password = %s', (email, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['email'] = account['email']
            session['password'] = account['password']
            msg = 'Logged in successful !'
            return render_template ('now.html', msg=msg)
        else:
            msg = 'Plase fill out form'
            return render_template ('login.html', msg=msg)





if __name__=="__main__":
    app.run(debug=True, port=5000)