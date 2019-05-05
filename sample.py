from flask import Flask, render_template,redirect,url_for,request
import sqlite3


app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/users')
def get_users():
    con = sqlite3.connect('mydb.db')
    db = con.cursor()
    res = db.execute('select * from user')
    
    return render_template('sample1.html', rows=res.fetchall())

@app.route('/delete/<int:value>', methods=['POST'])
def delete_user(value):
    con = sqlite3.connect('mydb.db')
    db = con.cursor()
    res = db.execute('delete from user where ID = ?',(value,))
    con.commit() 
    con.close() 
    return redirect(url_for('get_users'))

@app.route('/add/', methods=['POST'])
def add_user():
    con = sqlite3.connect('mydb.db')
    db = con.cursor()
    one=request.form.get('one')
    two=request.form.get('two')
    three=request.form.get('three')
    five=request.form.get('five')
    four=request.form.get('four')
    res = db.execute('insert into user (ID,NAME,AGE,ADDRESS,SALARY) values (?,?,?,?,?)',(one,two,three,four,five))
    con.commit()
    con.close()
    return redirect(url_for('get_users'))


if __name__ == "__main__":
    app.run(port=8014)
