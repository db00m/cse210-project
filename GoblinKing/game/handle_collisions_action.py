from core.action import Action
import arcade

class HandleCollisionsAction(Action):
    
    def __init__(self, engine):
        super().__init__(engine)

    def execute(self, cast, cue, callback):
        self._handle_ground_collisions(cast)

    def _handle_ground_collisions(self, cast):
        player = cast.first_actor("player")
        items = cast.first_actor("items")
        # Check for collision with items
        item_hit_list = arcade.check_for_collision_with_list(player,
            items)
        self._pick_up_item(cast, item_hit_list)
        

  
                
    def _pick_up_item(self,cast,item_hit_list):
        #TODO: add item point value to player score
        # Remove item from the items list
        for item in item_hit_list:
            print("item picked up!")
            cast.first_actor("items").remove(item)
            #Add the item to the plyers item list, not sure what this will be used for yet.
            cast.first_actor("player").pick_up_item(item)