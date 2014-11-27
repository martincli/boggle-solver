import sys, ast

# Boggle game parameters
GRID_HEIGHT = 0
GRID_WIDTH = 0
MIN_WORD_LENGTH = 0

# List of valid words
WORD_LIST = {}

# Tuples used for determining grid neighbors
ADJACENT = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

#=============
# Main method
#=============
def main():
    if len(sys.argv) != 3:
        print 'ERROR: Invalid number of arguments.'
    else:
        # Initialize grid and Boggle parameters from input
        grid = ast.literal_eval(sys.argv[1])
        global GRID_HEIGHT
        GRID_HEIGHT = len(grid)
        global GRID_WIDTH
        GRID_WIDTH = len(grid[0])
        global MIN_WORD_LENGTH
        MIN_WORD_LENGTH = int(sys.argv[2])

        # Initialize word list
        global WORD_LIST
        WORD_LIST = initWordList()

        # Execute algorithm
        result = solveBoard(grid)
        print sorted(result)

#================================================================
# Opens text file word list and stores valid words in dictionary
# Key: prefix of length N, where N = minimum word length
# Value: list of words that begin with corresponding prefix
# Returns dictionary
#================================================================
def initWordList():
    WORD_LIST = {}
    with open('words.txt') as f:
        for line in f:
            word = line.rstrip().lower()
            # Length check
            if len(word) >= MIN_WORD_LENGTH:
                prefix = word[:MIN_WORD_LENGTH]
                if prefix in WORD_LIST:
                    WORD_LIST[prefix].append(word)
                else:
                    WORD_LIST[prefix] = [word]
    return WORD_LIST

#====================================================
# Executes algorithm starting from each tile on grid
# Returns words found
#====================================================
def solveBoard(grid):
    words = []
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            findWords(grid, row, col, grid[row][col], [(row,col)], words)
    return words

#==============================================================================
# Main algorithm function
# At each tile:
#   - If the word so far is valid, append to output words
#   - If the length of the word so far is less than the minimum word length or
#     the word so far begins with a valid prefix, recurse for each neighbor,
#     adding its letter to the new path
#   - Keep track of which tiles have been visited for each path
# =============================================================================
def findWords(grid, row, col, current, visited, words):
    if len(current) >= MIN_WORD_LENGTH and isWord(current) and current not in words:
        words.append(current)
    if len(current) < MIN_WORD_LENGTH or current[:MIN_WORD_LENGTH] in WORD_LIST:
        neighbors = getNeighbors(row, col, visited)
        # Return when there are no neighbors remaining
        if not neighbors:
            return
        else:
            for neighbor in neighbors:
                # Keep track of visited tiles separately for each path
                new_visited = list(visited)
                new_visited.append(neighbor)
                new_row = neighbor[0]
                new_col = neighbor[1]
                # Recurse
                findWords(grid, new_row, new_col, current+grid[new_row][new_col], new_visited, words)

#================================================
# Returns True if word is valid, False otherwise
#================================================
def isWord(word):
    prefix = word[:MIN_WORD_LENGTH]
    if prefix in WORD_LIST:
        return word in WORD_LIST[prefix]
    else:
        return False

#===========================================
# Returns unvisited neighbors of given tile
#===========================================
def getNeighbors(row, col, visited):
    neighbors = []
    # For each possible neighbor
    for adj in ADJACENT:
        new_row = row + adj[0]
        new_col = col + adj[1]
        # Boundary check
        if new_row >= 0 and new_row < GRID_HEIGHT and new_col >= 0 and new_col < GRID_WIDTH:
            # Visited check
            if (new_row,new_col) not in visited:
                neighbors.append((new_row,new_col))
    return neighbors

if __name__ == '__main__':
    main()