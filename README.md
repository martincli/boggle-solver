Instructions
------------

To run:

    python boggle.py GRID MIN_WORD_LENGTH

GRID should be formatted as a list of lists.<br/>
MIN\_WORD\_LENGTH is simply an integer.

For example, for the grid below (with minimum word length = 3):

    S T N G
    E I A E
    D R L S
    S E P O

Example input:

    python boggle.py [['s','t','n','g'],['e','i','a','e'],['d','r','l','s'],['s','e','p','o']] 3

The program takes roughly 1 minute to solve this example.<br/>NOTE: Make sure `words.txt` is in the same directory as `boggle.py`.

Approach
--------

This implementation is essentially a brute force approach that recursively searches through every possible string in the grid. The search is done by starting from each tile and branching to its unvisited neighbors until there are none. The function keeps track of visited tiles for each recursive call. At each step, if the word created by combining the current letter and the path so far is valid, it is appended to an output list that is passed into the function (it can be referenced by each call). This approach is similar to a depth first graph search, except the recursive calls maintain separate sets of visited nodes (tiles).

Optimization: the valid words are stored in a hash table (Python dictionary) where the keys are prefix strings of length N, where N is the minimum allowed word length. The values are lists of words that begin with the corresponding prefixes. For example:

    'boa': ['board', 'boat'],
    'boy': ['boy', 'boyhood']...

The word list used to generate this data structure (included in `words.txt`) was found here: [http://svnweb.freebsd.org/csrg/share/dict/](http://svnweb.freebsd.org/csrg/share/dict/)

With this optimization, the dictionary is initialized before the algorithm executes. The algorithm can stop recursive calls from going further if the prefix of the word so far is not in the dictionary (if the path has at least N letters). This eliminates a huge portion of the paths that need to be searched.
