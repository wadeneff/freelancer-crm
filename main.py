from database.req import DATABASE_URL, addClient, deleteClient, getClient, getClients
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
    clients = getClients()

    return render_template('clients.html', articles=clients)

@app.route('/Client/<int:id>/info', methods=['POST', 'GET'])
def clientInfo(id):
    client = getClient(id)
    return render_template('client_info.html', client=client)

@app.route('/AddClients', methods=['POST', 'GET'])
def addClients():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        note = request.form['note']
        addClient(name, contact, note.strip())
        return redirect('/Clients')

    return render_template('add_clients.html', articles=clients)

if __name__ == '__main__':
    app.run(debug=True)
