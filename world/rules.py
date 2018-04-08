from random import randint
from evennia.contrib import dice

ATTACK_TYPES = {
    "slashing": {
        "min": 1,
        "max": 4,
    },
    "stabbing": {
        "min": 1,
        "max": 5,
    },
    "crushing": {
        "min": 1,
        "max": 6,
    },
}

ITEM_QUALITY = {
    "poor": {
        "bonus": -2,
    },
    "sub-par": {
        "bonus": -1,
    },
    "average": {
        "bonus": 0,
    },
    "exceptional": {
        "bonus": 1,
    },
    "masterwork": {
        "bonus": 2,
    },
}

def roll_hit():
    "Roll 1d20"
    return randint(1, 20)

def roll_dmg(damage_type):
    "Roll 1d6"
    return randint(DAMAGE_TYPES[damage_type].min, DAMAGE_TYPES[damage_type].max)

def check_defeat(character):
    "Checks if a character is 'defeated'."
    if character.db.health <= 0:
       character.msg("You fall down, defeated!")
       character.db.health = 100   # reset

def add_XP(character, amount):
    "Add XP to character, tracking level increases."
    character.db.XP += amount
    if character.db.XP >= (character.db.level + 1) ** 2:
        character.db.level += 1
        character.msg("You are now level %i!" % character.db.level)
        
def do_attack(char1, char2):
    
    char1.msg(dice.roll_dice(1,6))
    char2.msg(dice.roll_dice(1,6))