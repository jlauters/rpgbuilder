class levelOne:
    def __init__(self):
        self.setup()

    def map(self):
        return [
            ["X", "S", "X"],
            ["X", " ", "X"],
            ["X", " ", "X"],
            ["X", " ", "X"],
            ["X", " ", "X"],
            ["X", " ", "X"],
            ["X", "F", "X"]]
    
    def printMap(self):
        for (y, row) in enumerate(self.map()):
            prow = []
            for (x, letter) in enumerate(row):
                prow.append(letter)
            print(str(prow))


    def setup(self):
        
        # get positions for map, set start, open, finish
        letter_positions = {}
        for (y, row) in enumerate(self.map()):
            for (x, letter) in enumerate(row):
                letter_positions.setdefault(letter, []).append((x,y))

        self.start       = letter_positions['S']
        self.opensquares = letter_positions[' ']
        self.finish      = letter_positions['F']

