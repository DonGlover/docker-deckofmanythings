
# flask_web/app.py

from flask import Flask
app = Flask(__name__)
import random

cards = ('Sun', 'Moon', 'Star', 'Throne', 'Key', 'Knight', 'The Void', 'Flames', 'Skull', 'Ruin', 'Euryale', 'Rogue', 'Jester', 'Vizier', 'Comet', 'The fates', 'Gem', 'Talons', 'Idiot', 'Donjon', 'Balance', 'Fool' )
descriptions = ('They were granted tremendous insight and skill as if they were much more experienced in their travels. In addition, they were granted a single wondrous item from anywhere throughout the Realms or other planes of existence.', 
'They gained the ability to cast the powerful spell wish in one to three instances.', 
'Two defining qualities of them were greatly and permanently enhanced. Such characteristics included their wit, intellect, fortitude, athletic ability, or other similar characteristics that helped define who they were as a person.', 
'They became adept at influencing others to a heroic extent. Additionally some random keep located somewhere came into their rightful possession. However, the keep was infested with monstrous creatures that had to be expelled before it could be claimed. There were no recorded instances of any keeps appearing or having their ownership transferred by means of this magic.', 
'A rare weapon, of a type with which they were proficient, appeared in the hands of the card\'s drawer.', 
'A powerful knight appeared and pledged their loyalty to them. This noble combatant believed that the fates had drawn them to that place and time. This person and the drawer belonged to the same race and sex.', 
'Their body was incapacitated and their soul was transported into a random object located somewhere. The location of the object was revealed to anyone nearby. The effects of this card could not be reversed by a wish spell.', 
'They earned the enmity of a formidable devil who sought their suffering and destruction. This hatred continued until they or the fiend died. Hostile action by the outsider was taken within one to twenty days of earning the enmity.', 
'An avatar of death appeared before them. Before assaulting them with its scythe, the skeletal reaper warned anyone nearby that they were to engage in this fight alone. Anyone slain by the avatar of death could not be resurrected or otherwise brought back to life. ', 
'They lost any and all wealth in their possession. While magical items were not affected in this manner, gold and other valuables disappeared. Any businesses, investments, land, or other holdings were also lost along with any corresponding documentation.', 
'The image of the medusa-like creature permanently cursed them. This effect could only be reversed by a deity or the magic of the fates card.', 
'A person became openly hostile towards the drawer of the card although their identity was unknown to them. This hatred could only be alleviated by a deity\'s intervention or the spell wish. The person who hated the drawer did not make a big show of his or her hatred. Instead, the person hid it until the most opportune time to show it to cause maximum to the object of his or her hatred.', 
'Great intuition and expertise were bestowed upon them in a similar manner as if they drew the sun card, albeit to a lesser extent. In addition they could draw two additional cards beyond those that they previously declared.', 
'Within one year of drawing this card, they could ask a question in a state of meditation and receive an enlightening answer within their mind. Along with specific knowledge, they gained the wisdom to apply that information and if necessary, solve a dilemma or crisis in their life. ', 
'If they defeated the next hostile creature or group of individuals they encountered single-handedly they gained a great amount of insight from the battle. If this did not occur the card had no effect.', 
'They gained the ability to undo the fabric of time and reality, completely erasing one event from their life as if it never happened (including the eurayle\'s curse). The effects of this card could be used immediately or anytime within their lifetime.', 
'A great cache of valuable gems appeared before them, in the form of 25 pieces of jewelry or 50 individual gem stones. The value of these riches totaled 50,000 gp.', 
'Every magic item in their possession disintegrated. Any artifacts on their possession were not destroyed in this manner, but did vanish to some other location.', 
'Their intellect and mental faculties were significantly diminished, but not to a point that it could cause death. They could draw one card in addition to those they declared.', 
'They became imprisoned in a state of stasis within an extra-dimensional space somewhere in existence, in a manner similar to the spell imprisonment. All of their clothes, possessions and belongings remained at the location where they drew the card. They remained there until were discovered and recovered,[3] however they could not be located by any divination magic and only by a casting of wish. Even if they previously declared, they drew no more cards.', 
'Their alignment was reversed along the axes of both good verses evil and order versus chaos. No effects occurred if they were considered neutral or unaligned. Furthermore, if the drawer\'s actions did not meet the standards of the newly imposed ethical and moral outlook, the card\'s magic sapped the drawer\'s life energy.', 
'They lost understanding and competence in a manner opposite to those effects that were caused by th1e jester card. They drew another card from the deck, regardless of how many other draws they had declared.')

class Card:
    def __init__(self, card, desc):
        self.card = card
        self.description = desc

    def __str__(self)        :
        return self.card + ": " + self.description

class Deck:
    def __init__(self):
        self.all_cards = []
        i = 0
        for card in cards :
            create_card = Card(card,descriptions[i])
            self.all_cards.append(create_card)
            i+=1
    
    def shuffle(self):

        random.shuffle(self.all_cards)

    def pull_one(self):

        return self.all_cards.pop()

@app.route('/pullcard')
def get_card():

    if 'working_deck' not in locals() or len(working_deck.all_cards)==0:
        working_deck = Deck()
        working_deck.shuffle()
        card = working_deck.pull_one()
        return card.__str__()

if __name__ == '__main__':
    app.run(host='0.0.0.0')