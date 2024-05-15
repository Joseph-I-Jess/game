import gameGui
import map
import mapCell

class Game:
    """Collect the game objects together and present an interface for easier maintenance."""

    def __init__(self, map_name="unnamed map", map_description="undescribed map", map_cells=dict()):
        """Create some default values!"""
        self.game_gui = gameGui.GameGui()
        self.map_cells = map_cells
        self.map = map.Map(map_name, map_description, self.map_cells)

    def run(self):
        """Start the game_gui!"""
        self.game_gui.run()
