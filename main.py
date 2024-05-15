import game
import mapCell

def main():

    cell_00 = mapCell.MapCell("origin", "this is the starting cell of the map and the game!", (0,0))
    cell_01 = mapCell.MapCell("second cell", "this is the second map cell of the map and the game!", (1,0), {"north":cell_00})
    cell_00.obvious_exits["south"] = cell_01

    initial_map_cells = {cell_00.name:cell_00, cell_01.name:cell_01}

    my_game = game.Game("Example Map!", "Just an example map!", initial_map_cells)
    my_game.run()


if __name__ == "__main__":
    main()