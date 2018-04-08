import random
from evennia import DefaultRoom, TICKER_HANDLER

ECHOES = ["The sky is clear.", 
          "Clouds gather overhead.",
          "It's starting to drizzle.",
          "A breeze of wind is felt.",
          "The wind is picking up"] # etc  

class WeatherRoom(DefaultRoom):
    "This room is ticked at regular intervals"        
   
    def at_object_creation(self):
        "called only when the object is first created"
        TICKER_HANDLER.add(60 * 60, self.at_weather_update)

    def at_weather_update(self, *args, **kwargs):
        "ticked at regular intervals"
        echo = random.choice(ECHOES)
        self.msg_contents(echo)