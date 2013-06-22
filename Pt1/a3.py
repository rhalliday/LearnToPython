'''A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''


def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'to')
    False
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TON')
    False
    '''

    return word in wordlist

def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2)
    ''
    '''

    return_string = ''

    # return an empty string if row_index is greater than the number of elements
    if row_index >= len(board):
        return return_string

    # go through each element of board[row_index] appending them to return_string
    for letter in board[row_index]:
        return_string = return_string + letter

    return return_string

def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    Precondition: the list of str's should be the same length

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 3)
    'TB'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 4)
    ''
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['S', 'O', 'B']], 3)
    'T'
    '''

    return_string = ''

    for letters in board:
        if column_index < len(letters):
            return_string = return_string + letters[column_index]

    return return_string

def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    '''

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO')
    True
    '''

    for col_index in range(len(board[0])):
        if word in make_str_from_column(board, col_index):
            return True

    return False

def board_contains_word(board, word):
    '''(list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'BOX')
    False
    '''

    return board_contains_word_in_row(board, word) or board_contains_word_in_column(board, word)

def word_score(word):
    '''(str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('TO')
    0
    >>> word_score('BIGGER')
    6
    >>> word_score('ENORMOUSLY')
    30
    '''

    if len(word) < 3:
        return 0
    elif len(word) < 7:
        return len(word)
    elif len(word) < 10:
        return len(word) * 2
    else:
        return len(word) * 3

def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''
    player_info[1] = player_info[1] + word_score(word)

def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''

    # variable to keep track of the number of words found
    words_found_count = 0
    for word in words:
        if board_contains_word(board, word):
            words_found_count = words_found_count + 1

    return words_found_count

def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    '''

    return_list = []
    # loop through the file stripping the newline and appending it to the list
    for line in words_file:
        return_list.append(line.rstrip('\n'))

    # return the array
    return return_list

def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    '''

    board = []

    # go through each line in the file    
    for line in board_file:
        # remove the spaces
        row_string = line.rstrip('\n')

        letters = []
        
        # append each letter to the correct row of the board
        for letter in row_string:
            letters.append(letter)

        # add letters to the board
        board.append(letters)

    # return our list
    return board
    
