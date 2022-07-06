from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'us-cdbr-east-06.cleardb.net'
app.config['MYSQL_USER'] = 'b83699d4ef4d2f'
app.config['MYSQL_PASSWORD'] = '15434603'
app.config['MYSQL_DB'] = 'heroku_3da0faa61686dd7'

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
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO feedback(customer, dealer, rating, comments) VALUES (%s, %s, %s, %s)", (customer, dealer, rating, comments))
            mysql.connection.commit()
            cur.close()
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please enter required fields')
        return render_template('success.html')         
        
   

if __name__ == '__main__':
    app.run()