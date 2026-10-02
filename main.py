from database.req import DATABASE_URL, addClient, getClients
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL

@app.route('/', methods=['POST', 'GET'])
@app.route('/home', methods=['POST', 'GET'])
def index():
    return render_template('homepage.html')

@app.route('/Clients', methods=['POST', 'GET'])
def clients():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        note = request.form['note']
        addClient(name, contact, note)
        redirect('/Clients')
    clients = getClients()

    return render_template('clients.html', articles=clients)

if __name__ == '__main__':
    app.run(debug=True)
