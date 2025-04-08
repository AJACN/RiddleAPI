from flask import Flask, jsonify, request
import random
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

#Pega a variável de ambiente e converte para JSON
FBKEY = json.loads(os.getenv('CONFIG_FIREBASE'))

cred = credentials.Certificate(FBKEY)
firebase_admin.initialize_app(cred)

#Conectando com o Firestore da Firebase
db = firestore.client()


# ---------- ROTA PRINCIPAL DE TESTE ----------
@app.route('/')
def index():
    return 'Riddle me this...', 200


# ------ MÉTODO GET - CHARADA ALEATÓRIA -------
@app.route('/riddles', methods=['GET'])
def riddle():
    riddles = []
    list = db.collection('riddles').stream()

    for item in list:
        riddles.append(item.to_dict())

    if riddles:
        return jsonify(random.choice(riddles)), 200
    else:
        return jsonify({'message':'Error! No riddles found!'}), 404

# ------ MÉTODO GET - LISTA CHARADAS -------
@app.route('/riddles/list', methods=['GET'])
def riddlelist():
    riddles = []
    list = db.collection('riddles').stream()

    for item in list:
        riddles.append(item.to_dict())

    if riddles:
        return jsonify(riddles), 200
    else:
        return jsonify({'message':'Error! No riddles found!'}), 404

# -------- MÉTODO GET - CHARADA POR ID --------
@app.route('/riddles/<id>', methods=['GET'])
def search(id):
    doc_ref = db.collection('riddles').document(id)
    doc = doc_ref.get().to_dict()

    if doc:
        return jsonify(doc), 200
    else:
        return jsonify({'message':'Riddle not found'}), 404


# ------- MÉTODO POST - ADICIONAR CHARADA -------
@app.route('/riddles', methods=['POST'])
def add_riddle():
    data = request.json

    if "question" not in data or "answer" not in data:
        return jsonify({'message':'Error. Question and Answer fields are required'}), 400

    # Counter
    counter_ref = db.collection('id_control').document('counter')
    counter_doc = counter_ref.get().to_dict()
    last_id = counter_doc.get('id')
    new_id = int(last_id) + 1
    counter_ref.update({'id': new_id}) #atualização da coleção

    db.collection('riddles').document(str(new_id)).set({
        "id": new_id,
        "question": data['question'],
        "answer": data['answer']
    })

    return jsonify({'message':'Riddle submitted successfully!'}), 201

# -------- MÉTODO PUT - ALTERAR CHARADA -------
@app.route('/riddles/<id>', methods=['PUT'])
def alter_riddle(id):
    data = request.json

    if "question" not in data or "answer" not in data:
        return jsonify({'mensagem':'Error. Question and Answer field are required'}), 400

    doc_ref = db.collection('riddles').document(id)
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            'question': data['question'],
            'answer': data['answer']
        })
        return jsonify({'message':'Riddle updated successfully'}), 201
    else:
        return jsonify({'message':'Error. Riddle not found.'}), 404

# ------- MÉTODO DELETE - EXCLUIR CHARADA -------
@app.route('/riddles/<id>', methods=['DELETE'])
def delete_riddle(id):
    doc_ref = db.collection('riddles').document(id)
    doc = doc_ref.get()

    if not doc.exists:
        return jsonify({'message':'Error. Riddle not found.'}), 404

    doc_ref.delete()
    return jsonify({'message':'Riddle deleted successfully!'})

if __name__ == '__main__':
    app.run()