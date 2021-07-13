from core.action import Action
from game import constants
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
            self._pick_up_item(gems, gem_hit_list, player, cast)
        
        player_hazard_hit_list = arcade.check_for_collision_with_list(player,
            hazards)
        water_hazard_hit_list = arcade.check_for_collision_with_list(player.get_spray(),hazards)
        if not len(player_hazard_hit_list) == 0:
            self._encounter_hazard(cast,player_hazard_hit_list)
            
        if not len(water_hazard_hit_list) == 0:
            for hazard in water_hazard_hit_list:
                hazards.remove(hazard)
                cast.get_actors("items")[2].remove(player.use_water())
            
        waters_hit_list = arcade.check_for_collision_with_list(player, waters)
        if not len(waters_hit_list) == 0:
            self._pick_up_item(waters, waters_hit_list, player, cast)

  
                
    def _pick_up_item(self,items,item_hit_list, player, cast):
        #TODO: add item point value to player score
        # Remove item from the items list
        score = cast.first_actor("score")
        timer = cast.first_actor("timer")
        for item in item_hit_list:

            if item.get_type() == "item":
                if item._value == 10:
                    timer.reduce_time(item._value * constants.TIME_REDUCE)
                else:
                    score.add_score(item._value)
                items.remove(item)
                
            #Add the item to the plyers item list, not sure what this will be used for yet.
            player.pick_up_item(item)
            
    def _encounter_hazard(self,cast,hazard_hit_list):
        player = cast.first_actor("player")
        for hazard in hazard_hit_list:
                player.hit()