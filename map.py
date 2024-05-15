
class Map:
    """Represent a group of map cells"""
    def __init__(self, name="unnamed map", description="undescribed map", cells=dict()):
        """
        create a new map

        params:
            name: the name of this map
            description: how is this map described
            cells: a dictionary mapping a map cell name to a map cell
        """
        self.name = name
        self.description = description
        self.cells = cells