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

@app.route('/shoping')
def shoping():
    return render_template('shoping-cart.html')

@app.route('/features')
def features():
    return render_template('product-cart.html')

@app.route('/product')
def product():
    return render_template('product.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


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
    return render_template('register.html')

@app.route ('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form ['username']
        password = request.form ['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT* FROM ecommerce WHERE username = %s AND password = %s', (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['username'] = account['username']
            session['password'] = account['password']
            msg = 'Logged in successful !'
            return render_template ('main.html')
        else:
            msg = 'Plase fill out form'
    return render_template ('login.html')

@app.route('/login/index')
def loggedin():
    if 'loggedin' in session:
        return render_template('index.html', username=['username'])
    return redirect(url_for('/log'))

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('index'))



if __name__=="__main__":
    app.run(debug=True, port=5000)