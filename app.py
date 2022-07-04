from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'lexus'

mysql = MySQL(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO feedback VALUES(%s,%s,%s,%s)''',(customer, dealer, rating, comments))
        
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        else:
            return render_template('success.html')
        mysql.connection.commit()
        cursor.close()
   

app.run(host='localhost', port=5000)