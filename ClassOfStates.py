# Asmaa Gamal
#state_class of Assignment 1
# Electronics & Communications department
#using informed and uninformed search Algorithms to solve 8-puzzle



class State:

    #depth = {} #i won't use it but it is to solve a warning as what stackoverflow told me here: https://stackoverflow.com/questions/28172008/pycharm-visual-warning-about-unresolved-attribute-reference

    def __init__(self, state, parent, move, depth, cost, key):

        self.state = state

        self.parent = parent

        self.move = move

        self.depth = depth

        self.cost = cost

        self.key = key

        if self.state:
            self.map = ''.join(str(e) for e in self.state)    #map = for loop of the whole elements in all 2d or 4 d or n dimensions so al map  btmsk each element we te apply 3leh al change elle ana 3awza 23mloh

    def __eq__(self, other): #to transform the num into str to compare and find if equal
        return self.map == other.map

    def __lt__(self, other): #to transform the num into str to compare and find if less than
        return self.map < other.map