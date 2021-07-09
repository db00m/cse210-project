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
        gems = items[0]
        hazards = items[1]
        waters = items[2]
        # Check for collision with items
        gem_hit_list = arcade.check_for_collision_with_list(player,
            gems)
        if not len(gem_hit_list) == 0:
            self._pick_up_item(gems, gem_hit_list, player)
        
        hazard_hit_list = arcade.check_for_collision_with_list(player,
            hazards)
        if not len(hazard_hit_list) == 0:
            self._encounter_hazard(cast,hazard_hit_list)
        
        waters_hit_list = arcade.check_for_collision_with_list(player, waters)
        if not len(waters_hit_list) == 0:
            self._pick_up_item(waters, waters_hit_list, player)

  
                
    def _pick_up_item(self,items,item_hit_list, player):
        #TODO: add item point value to player score
        # Remove item from the items list
        for item in item_hit_list:
            print("item picked up!")
            items.remove(item)
            #Add the item to the plyers item list, not sure what this will be used for yet.
            player.pick_up_item(item)
            
    def _encounter_hazard(self,cast,hazard_hit_list):
        player = cast.first_actor("player")
        for hazard in hazard_hit_list:
            player.hit()