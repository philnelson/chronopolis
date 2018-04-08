"""
Room

Rooms are simple containers that has no location of their own.

"""

from evennia import DefaultRoom
from world.map import Map
from evennia import utils
from characters import Character
from npc import Npc
import random
from evennia import DefaultRoom, TICKER_HANDLER

class Room(DefaultRoom):
    
    def return_appearance(self, looker):
        # [...]
        string = "\n====== MAP ====== %s\n" % Map(looker).show_map()
        # Add the room description under the map     
        #string += "\n{c%s{n\n" % self.get_display_name(looker)
        # Add all the normal stuff like room description, 
        # contents, exits etc. 
        string += "================="
        string += "\n\n" + super(Room, self).return_appearance(looker)
        
        
        return string
        
    def at_object_receive(self, obj, source_location):
        if utils.inherits_from(obj, Npc): # An NPC has entered
            pass
        else:
            if utils.inherits_from(obj, Character): 
                # A PC has entered, NPC is caught above.
                # Cause the character to look around
                obj.execute_cmd('look')
                for item in self.contents:
                    if utils.inherits_from(item, Npc): 
                        # An NPC is in the room
                        item.at_char_entered(obj)
                        
    
    ECHOES = ["The sky is clear.", 
              "Clouds gather overhead.",
              "It's starting to drizzle.",
              "A breeze of wind is felt.",
              "The wind is picking up"] # etc

class WeatherRoom(Room):
    "This room is ticked at regular intervals"        
   
    def at_object_creation(self):
        "called only when the object is first created"
        TICKER_HANDLER.add(60 * 60, self.at_weather_update)

    def at_weather_update(self, *args, **kwargs):
        "ticked at regular intervals"
        echo = random.choice(ECHOES)
        self.msg_contents(echo)