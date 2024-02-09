from flask import Flask, appcontext_popped, render_template, request
from flask_mysqldb import MySQL

app = Flask (__name__)

app.config['SECRET_KEY'] = 'your-secret-key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'


mysql= MySQL(app)


@app.route("/")
def index():
    return render_template('nav.html')


# @app.route("/reg")
# def reg():
#     if request.method== "POST" and "username" in request.form and "email" in request.form and "password" in request.form:
#         username = request.form["username"]
#         email = request.form["email"]
#         password = request.form["password"]
#         cursor = mysql.connection.cursor()
#         cursor.execute('INSERT INTO #  VALUES (%s, %s, %s)', (username, password, email))
#         mysql.connection.commit()
#         msg = " "
#         return render_template('now.html')
#     elif request.method == "POST":
#         msg = "page not found "
#         return render_template("register.html", msg = msg)









if __name__=="__main__":
    app.run(debug=True, port=5000)