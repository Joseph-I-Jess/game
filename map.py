import mapCell

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

        self.map_cell_location_data = []
        self.map_cell_location_data = self.get_locations() # derived (cached) location data list

    def add_map_cell(self, name="unnamed map cell", description="undescribed map cell", location=(0,0), obvious_exits=dict(), secret_exits=dict()):
        if name not in self.cells.keys():
            self.cells[name] = mapCell(name, description, location, obvious_exits, secret_exits)
            self.map_cell_location_data.append(location)
        else:
            raise SyntaxError(f"Dictionary key ({name}) already exists in map's cell names")
        

    def get_locations(self):
        """Helper function to calculate a list of (x,y) locations of cells.
        
            Generate it ourselves if needed!
        """

        if not self.map_cell_location_data: # if cell location data is empty, then generate it
            self.map_cell_location_data = [map_cell.get_location() for map_cell in self.cells.values()]

        return self.map_cell_location_data
