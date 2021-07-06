class Action:

    class Callback:

        def on_finished(self, next_scene):
            pass

    def __init__(self, physics_engine):
        self._enabled = True
        self._engine = physics_engine

    def enable(self):
        self._enable = True

    def disable(self):
        self._enable = False
        
    def execute(self, cast, cue, callback):
        pass
    
    def is_enabled(self):
        return self._enabled