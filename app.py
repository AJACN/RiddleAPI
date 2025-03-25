from flask import Flask, jsonify
import random

app = Flask(__name__)

riddles = [
    {'id':1, 'riddle':'What do you call a man with no body and no nose?', 'answer':'Nobody nose!'},

    {'id':2, 'riddle':'What do you call a cute door?', 'answer':'Adoorable!'},

    {'id':3, 'riddle':'Why did the fly never land on the computer?', 'answer':'It was afraid of the world wide web.'},

    {'id':4, 'riddle':'How does a bee get to school?', 'answer':'On a buzz!'},

    {'id':5, 'riddle':'What is orange and sounds like a parrot?', 'answer':'A carrot'},

    {'id':6, 'riddle':'What fruit can you never cheer up?', 'answer':'A blueberry.'},

    {'id':7, 'riddle':'What do you call a snail on a ship?', 'answer':'A snailor!'},

    {'id':8, 'riddle':'What type of music do rabbits listen to?', 'answer':'Hip hop!'},

    {'id':9, 'riddle':'What is on the ground and also a hundred feet in the air?', 'answer':'A centipede on its back!'},

    {'id':10, 'riddle':'What kind of room has no doors or windows?', 'answer':'A Mushroom'}
]

@app.route('/')
def index():
    return 'Riddle me this...', 200

@app.route('/riddles', methods=['GET'])
def riddle():
    return jsonify(random.choice(riddles))

@app.route('/riddles/<field>/<search>', methods=['GET'])
def search(field, search):
    if field not in ['id']:
        return jsonify({'message':'ERROR - No results available.'}), 404

    if field == 'id':
        search = int(search)

    for riddle in riddles:
        if riddle[field] == search:
            return jsonify(riddle), 200
    else:
        return jsonify({'mensagem':'ERROR! Riddle not found.'}), 404

if __name__ == '__main__':
    app.run()