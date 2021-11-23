import flask
from flask import Flask, request
app = Flask(__name__)

@app.route('/trazabilidad', methods=['GET','POST'])

def traza():
    if request.method == 'GET':
        return 'El archivo llega'
    else:
        return 'el archivo no llega'