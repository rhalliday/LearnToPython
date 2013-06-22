# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """
    
    def __init__(self,symbol,row,col):
        """ (Rat, str, int, int) -> NoneType
        
        Create a rat that takes a symbol and a start position row and column.

        >>> paul = Rat('P', 1, 4)
        >>> paul.symbol
        'P'
        >>> paul.row
        1
        >>> paul.col
        4
        >>> paul.num_sprouts_eaten
        0
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType

        Sets the rat's position to row and col.
        
        >>> jen = Rat('J', 1, 2)
        >>> jen.set_location(2, 3)
        >>> jen.row
        2
        >>> jen.col
        3
        """

        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType

        Increases the number of sprouts eaten by one.

        >>> jen = Rat('J', 1, 2)
        >>> jen.eat_sprout()
        >>> jen.num_sprouts_eaten
        1
        >>> jen.eat_sprout()
        >>> jen.num_sprouts_eaten
        2
        """

        self.num_sprouts_eaten += 1

    def __str__(self):
        """ (Rat) -> str

        Returns a string in the format:
        'symbol at (row, col) ate num_sprouts_eaten sprouts.'

        >>> paul = Rat('P', 1, 2)
        >>> paul.__str__()
        'P at (1, 2) ate 0 sprouts.'
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol,
                    self.row, self.col, self.num_sprouts_eaten)        


class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """ (Maze, list of list of str, Rat, Rat) -> NoneType

        Create a maze object with a maze and two rats.

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1),Rat('P', 1, 4))
        >>> mymaze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> mymaze.rat_1.symbol
        'J'
        >>> mymaze.rat_2.col
        4
        >>> mymaze.num_sprouts_left
        3
        """

        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        num_sprouts = 0
        for sub_list in maze:
            num_sprouts += sub_list.count(SPROUT)

        self.num_sprouts_left = num_sprouts

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Returns true iff there is a wall at the given row and column.

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1),Rat('P', 1, 4))
        >>> mymaze.is_wall(0,0)
        True
        >>> mymaze.is_wall(1,3)
        False
        >>> mymaze.is_wall(2,2)
        True
        >>> mymaze.is_wall(5,3)
        True
        """

        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column.

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1),Rat('P', 1, 4))
        >>> mymaze.get_character(0,0)
        '#'
        >>> mymaze.get_character(1,1)
        'J'
        >>> mymaze.get_character(1,4)
        'P'
        >>> mymaze.get_character(4,4)
        '@'
        >>> mymaze.get_character(2,1)
        '.'
        """

        if self.rat_1.row == row and self.rat_1.col == col:
            return self.rat_1.symbol
        elif self.rat_2.row == row and self.rat_2.col == col:
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, rat, vert, horiz):
        """ (Maze, Rat, int, int) -> bool

        Moves the rat in the maze.
        Returns true iff there wasn't a wall in the way

        >>> jen = Rat('J', 1, 1)
        >>> paul = Rat('P', 1, 4)
        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']],jen, paul)
        >>> mymaze.move(jen,UP,NO_CHANGE)
        False
        >>> mymaze.move(jen,NO_CHANGE,LEFT)
        False
        >>> mymaze.move(jen,DOWN,RIGHT)
        False
        >>> mymaze.move(jen,DOWN,NO_CHANGE)
        True
        >>> jen.row
        2
        >>> jen.col
        1
        >>> mymaze.move(jen,DOWN,NO_CHANGE)
        True
        >>> mymaze.get_character(4,1)
        '@'
        >>> mymaze.move(jen,DOWN,NO_CHANGE)
        True
        >>> jen.row
        4
        >>> jen.col
        1
        >>> jen.num_sprouts_eaten
        1
        >>> mymaze.move(jen,UP,NO_CHANGE)
        True
        >>> mymaze.get_character(4,1)
        '.'
        >>> jen.row
        3
        >>> jen.col
        1
        >>> mymaze.move(jen,NO_CHANGE,RIGHT)
        True
        >>> jen.row
        3
        >>> jen.col
        2
        >>> mymaze.move(jen,NO_CHANGE,LEFT)
        True
        >>> jen.row
        3
        >>> jen.col
        1
        """

        new_row = rat.row + vert
        new_col = rat.col + horiz

        if self.is_wall(new_row, new_col):
            return False
        else:
            rat.set_location(new_row, new_col)
            if self.maze[new_row][new_col] == SPROUT:
                rat.eat_sprout()
                self.maze[new_row][new_col] = HALL
                self.num_sprouts_left -= 1

        return True

    def __str__(self):
        """ (Maze) -> str

        returns a string representation of the maze.

        >>> mymaze = Maze([['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']], Rat('J', 1, 1), Rat('P', 1, 4))
        >>> print(str(mymaze))
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        return_string = ''

        for row in range(0,len(self.maze)):
            for col in range(0,len(self.maze[row])):
                return_string += self.get_character(row,col)

            return_string += '\n'

        return return_string + str(self.rat_1) + '\n' + str(self.rat_2)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
