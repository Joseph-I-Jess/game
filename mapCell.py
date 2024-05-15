
class MapCell:
    """Represents a map cell."""
    def __init__(self, name="unnamed map cell", description="undescribed map cell", obvious_exits=dict()):
        """
        
        params:
            name: the name of this map cell
            description: how would you describe this map cell?
            obvious exits: a dictionary mapping a string that is a "direction" to be typed in that maps to another map cell for the player to move to
        """
        self.name = name
        self.description = description
        self.obvious_exits = obvious_exits

    