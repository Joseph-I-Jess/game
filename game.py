import gameGui
import map
import mapCell

class Game:
    """Collect the game objects together and present an interface for easier maintenance."""

    def __init__(self, map_name="unnamed map", map_description="undescribed map", map_cells=dict()):
        """Create a map with given values.
        
        params:
            map_name: name of the map tied to this game,
            map_description: description of the map for this game,
            map_cells: a dictionary of map cells, mapping a map_cell name to its associated map_cell
        """
        self.map_cells = map_cells
        self.map = map.Map(map_name, map_description, self.map_cells)
        self.game_gui = gameGui.GameGui(self.map.get_locations())

    def run(self):
        """Start the game_gui!"""
        self.game_gui.run()
