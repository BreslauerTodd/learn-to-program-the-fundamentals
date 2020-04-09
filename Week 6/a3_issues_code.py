def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    
    wordFile = open(words_file, 'r')
    words = []
    
    for line in wordFile:
        words.append(line.rstrip('\n'))
    
    wordFile.close()
    
    return words


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    
    boardFile = open(board_file, 'r')
    board = []
    for line in boardFile:
        baseline = line.rstrip('\n')
        lineList = []
        for i in range(0,len(line)-1):
            lineList.append(baseline[i])
        board.append(lineList)
        
    boardFile.close()
    
    return board
