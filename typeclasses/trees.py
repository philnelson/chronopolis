# mygame/typeclasses/trees.py

from typeclasses.objects import Object

class Oak(Object):
    """
    This creates a simple tree object        
    """    
    def at_object_creation(self):
        "this is called only once, when object is first created"
        self.db.desc = "An oak tree."
        self.locks.add("get:false()")
        self.db.health = 100
        