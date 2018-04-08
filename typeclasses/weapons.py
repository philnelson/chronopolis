"""
Object

The Object is the "naked" base class for things in the game world.

Note that the default Character, Room and Exit does not inherit from
this Object, but from their respective default implementations in the
evennia library. If you want to use this class as a parent to change
the other types, you can do so by adding this as a multiple
inheritance.

"""
from objects import Object
from world import rules

WEAPON_MATERIALS = {
    "bone": {
        "bonus": 0,
    },
    "wood": {
        "bonus": 0,
    },
    "steel": {
        "bonus": 1,
    },
}

WEAPON_TYPES = {
    "dagger": {
        "min": 1,
        "max": 3,
    },
}


class Weapon(Object):
    
    def return_appearance(self, looker):
        """
        The return from this method is what
        looker sees when looking at this object.
        """
        text = "{} {} {}".format(self.db.quality, self.db.material, super(Object, self).return_appearance(looker))
        
        damage_bonus = rules.ITEM_QUALITY[self.db.quality]['bonus'] + WEAPON_MATERIALS[self.db.material]['bonus']
        damage = "{}-{}".format(WEAPON_TYPES[self.db.weapon_type]['min'], WEAPON_TYPES[self.db.weapon_type]['max'])
        
        if damage_bonus > 0:
            cscore = " ({} {} damage)".format(damage,damage_bonus)
        else:
            cscore = " ({} damage)".format(damage)
            
        cscore += ""
        if "\n" in text:
            # text is multi-line, add score after first line
            first_line, rest = text.split("\n", 1)
            text = first_line + cscore + "\n" + rest
        else:
            # text is only one line; add score to end
            text += cscore
        return text
    
    def at_object_creation(self):
        self.db.health = 100
        self.db.weapon_type = 'dagger'
        self.db.material = 'wood'
        self.db.quality = 'average'
        
        damage_bonus = rules.ITEM_QUALITY[self.db.quality]['bonus'] + WEAPON_MATERIALS[self.db.material]['bonus']
        damage = "{}-{}".format(WEAPON_TYPES[self.db.weapon_type]['min'], WEAPON_TYPES[self.db.weapon_type]['max'])
        
        if damage_bonus > 0:
            desc = "{} +{} damage".format(damage,damage_bonus)
        if damage_bonus < 0:
            desc = "{} {} damage".format(damage,damage_bonus)
        else:
            desc = "{} damage".format(damage)
        
        self.db.desc = desc
        
    def at_drop(self, dropper):
        
        for item in dropper.db.equipment:
            if item == self:
                dropper.msg("De-equipped {}".format(super(Object, self).return_appearance(dropper)))
                dropper.db.equipment.remove(item)
        