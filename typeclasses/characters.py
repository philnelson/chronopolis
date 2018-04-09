"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from random import randint
import json

SKILLS = {
    'fighter': {
        "effects": [{
            
        }],
    },
}

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_object_creation(self):
        "Called only when first created"
        self.db.level = 1 
        self.db.health = randint(4, 24)
        self.db.mana = randint(4, 24)
        self.db.charisma = randint(1,6)
        self.db.perception = randint(1,6)
        self.db.strength = randint(1,6)
        self.db.experience = 0
        self.db.armor_rating = 1
        self.db.equipment = []
        self.db.skills = []

    def return_appearance(self, looker):
        """
        The return from this method is what
        looker sees when looking at this object.
        """
        text = super(Character, self).return_appearance(looker)
        cscore = " (LVL {}, HP {}, MP {})".format(self.db.level, self.db.health, self.db.mana)
        cscore += ""
        if "\n" in text:
            # text is multi-line, add score after first line
            first_line, rest = text.split("\n", 1)
            text = first_line + cscore + "\n" + rest
        else:
            # text is only one line; add score to end
            text += cscore
        return text
        
    # inside the character class
    def at_after_move(self, source_location):
        """
        Default is to look around after a move 
        Note:  This has been moved to room.at_object_receive
        """
        #self.execute_cmd('look')
        pass