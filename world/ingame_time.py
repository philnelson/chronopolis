# in a file ingame_time.py in mygame/world/

from evennia.utils import gametime 
from typeclasses.rooms import Room

def at_sunrise():
    """When the sun rises, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The sun rises from the eastern horizon.")
        
def at_sunset():
    """When the sun rises, display a message in every room."""
    # Browse all rooms
    for room in Room.objects.all():
        room.msg_contents("The sun sets below the western horizon.")

def start_sunrise_event():
    """Schedule an sunrise event to happen every day at 6 AM."""
    script = gametime.schedule(at_sunrise, repeat=True, hour=6, min=0, sec=0)
    script.key = "at sunrise"
    
def start_sunset_event():
    """Schedule an sunrise event to happen every day at 6 pm."""
    script = gametime.schedule(at_sunrise, repeat=True, hour=18, min=0, sec=0)
    script.key = "at sunset"