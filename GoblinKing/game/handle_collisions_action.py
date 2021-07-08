from core.action import Action
import arcade

class HandleCollisionsAction(Action):
    
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)

    def _handle_ground_collisions(self, cast):
        player = cast.first_actor("player")
        items = cast.get_actors("items")
        
        #TODO: Add logic for picking up an items
        # it need to involve identifing which object
        # is being picked up.
            
        

  
                
    def _pick_up_item(self,cast,item):
        #TODO: add item point value to player score
        # Remove item from the items list
        cast.get_actors("items").remove(item)
        #Add the item to the plyers item list, not sure what this will be used for yet.
        cast.first_actor("player").pick_up_item(item)