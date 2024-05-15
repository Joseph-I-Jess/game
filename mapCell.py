
class MapCell:
    """Represents a map cell."""
    def __init__(self, name="unnamed map cell", description="undescribed map cell", location=(0,0), obvious_exits=dict(), secret_exits=dict()):
        """
        
        params:
            name: the name of this map cell
            description: how would you describe this map cell?
            location: the (x,y) position of this map cell
            obvious exits: a dictionary mapping a string that is a "direction" to be typed in that maps to another map cell for the player to move to
        """
        self.name = name
        self.description = description
        self.location = location
        self.obvious_exits = obvious_exits
        self.secret_exits = secret_exits

    def get_location(self):
        return self.location
    
    def add_obvious_exit(self, exit_name, destination):
        if exit_name not in self.obvious_exits.keys() and exit_name not in self.secret_exits.keys():
            self.obvious_exits[exit_name] = destination
        else:
            raise SyntaxError(f"Dictionary key ({exit_name}) already exists in either obvious or secret exits!")
        
    def add_secret_exit(self, exit_name, destination):
        if exit_name not in self.secret_exits.keys() and exit_name not in self.obvious_exits.keys():
            self.secret_exits[exit_name] = destination
        else:
            raise SyntaxError(f"Dictionary key ({exit_name}) already exists in either obvious or secret exits!")
    