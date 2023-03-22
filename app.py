
# flask_web/app.py

from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)
import random
import uuid
import re

cards = (
"Sun,Gain a beneficial miscellaneous magic item and 50000 experience points,http://www.kolvir.com/deck/sun.mp4",
"Moon,You are granted 1 to 4 wishes.,http://www.kolvir.com/deck/moon.mp4",
"Star,Immediately gain 2 points on major ability score.,http://www.kolvir.com/deck/star.mp4",
"Throne,Gain a charisma of 18 and a small keep.,http://www.kolvir.com/deck/throne.mp4",
"Key,Gain a treasure map plus one magic weapon.,http://www.kolvir.com/deck/key.mp4",
"Knight, Gain the service of a 4th level fighter.,http://www.kolvir.com/deck/knight.mp4",
"The Void,Body functions,but the soul is trapped elsewhere.,http://www.kolvir.com/deck/thevoid.mp4",
"Flames,Enmity between you and a devil.,http://www.kolvir.com/deck/flames.mp4",
"Skull,Defeat death or be forever destroyed. ,http://www.kolvir.com/deck/skull.mp4",
"Ruin,Immediately lose all wealth and real property.,http://www.kolvir.com/deck/ruin.mp4",
"Euryale,Minus three on all saving throws versus petrification.,http://www.kolvir.com/deck/eurayle.mp4",
"Rogue,One of your henchmen turns against you.,http://www.kolvir.com/deck/rougue.mp4",
"Jester,Gain 10000 xp OR 2 more draws from the deck.,http://www.kolvir.com/deck/jester.mp4",
"Comet,Defeat the next monster you meet to gain one level.,http://www.kolvir.com/deck/comet.mp4",
"Gem,Gain your choice of 20 jewelry or 50 gems.,http://www.kolvir.com/deck/gem.mp4",
"Talons,All magic items owned by you are torn from you.,http://www.kolvir.com/deck/talons.mp4",
"Balance,Change alignment or be judged.,http://www.kolvir.com/deck/balance.mp4",
"Fool,Lose 10000 xp and draw again,http://www.kolvir.com/deck/fool.mp4",
"Vizier,Know the answer to your next dilemma.,http://www.kolvir.com/deck/vizier.mp4",
"Idiot,Lose 1 to 4 points on your intelligence. You may draw again.,http://www.kolvir.com/deck/idiot.mp4",
"The fates,Avoid any situation you choose ... once.,http://www.kolvir.com/deck/thefates.mp4",
"Donjon,You are imprisoned.,http://www.kolvir.com/deck/donjon.mp4"
)

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

class Deck:
    def __init__(self, isNew):
        self.all_cards = []
        if isNew == True:
            i = 0
            for card in cards :
                create_card = [i,card] 
                self.all_cards.append(create_card)
                i+=1
    
    def shuffle(self):

        random.shuffle(self.all_cards)

    def pull_one(self): 

        return self.all_cards.pop()

    def save_deck(self, deck_id):
        file1 = open(deck_id,"w")
        for card in self.all_cards:
            file1.writelines(str(card[0]) + "\n")

        file1.close()

    def load_deck(self, deck_id):
        file1 = open(deck_id,"r")
        for card in file1:
            create_card = [int(card), cards[int(card)]] 
            self.all_cards.append(create_card)

@app.route('/getdeck', methods=['GET'])
def get_deck():
    new_deck = Deck(True)
    new_deck.shuffle()
    deck_id=str(uuid.uuid4())
    # save deck to file with the file name deck_id
    new_deck.save_deck(deck_id)
    response = jsonify({'deck_id': deck_id})
    return response

@app.route('/pullcard', methods=['GET'])
def get_card():
    # Get the deck id as uuid (?deck=f50ec0b7-f960-400d-91f0-c42a6d44e3d0) 
    deck_id = request.args.get('deck')
    # Get Query string containing deck 
    if is_valid_uuid(deck_id) or deck_id=='testdeck':
        working_deck = Deck(False)
        # working_deck.shuffle()
        working_deck.load_deck(deck_id)
        card = working_deck.pull_one()
        # ToDo: Save Deck
        working_deck.save_deck(deck_id)
        mysplit = re.split(r',(?='')', card[1])
        response = jsonify({'card' : mysplit[0], 'desc' : mysplit[1], 'video' : mysplit[2]})
        return response
    else:
        return  jsonify({'error': 'Invalid deck ID. '}), 400

@app.route('/')        
def fuck_off():
    return "Fuck off.", 404

if __name__ == '__main__':
    # app.run(host='127.0.0.1')
    # app.run(host='192.168.0.18')
    # app.run(host='0.0.0.0')
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)



# @app.route('your route', methods=['GET'])
# def yourMethod(params):
#     response = flask.jsonify({'some': 'data'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response