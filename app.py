from flask import Flask, appcontext_popped, render_template, request
from flask import MySQL

# mysql= MySQL(app)

app= Flask (__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/reg")
def register():
    if request.method== "POST" and "username" in request.form and "email" in request.form and "password" in request.form:
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO #  VALUES (%s, %s, %s)', (username, password, email))
        mysql.connection.commit()
        msg = " "
        return render_template('/')
    elif request.method =="POST":
        msg = " "
        return render_template("/")








if __name__=="__main__":
    app.run(debug=True)