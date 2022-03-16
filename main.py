# Asmaa Gamal
#Assignment 1
# Electronics & Communications department
#using informed and uninfoormed search Algorithms to solve 8-puzzle


#---------------------------------------------------libiraries-------------------------------------------------------
import  math
import  timeit                                                               #Measure execution time of small code
from    heapq           import heappush, heappop, heapify
from    ClassOfStates   import State                                         #importing from class
from    collections     import deque
from    GUI             import  GUI,print_cyan



# -----------------------------------------------------The 8-Puzzle Game -------------------------------------------------
print(" ---------------------8-puzzle Game using (BFS, DFS,& A*) search algorithms------------------------------- ")
print("-------------------------------------Welcome to the game---------------------------------------------------")
#initialization
goal_state    = [0, 1, 2, 3, 4, 5, 6, 7, 8]
goal_node     = State #Goal node is a full class which has depth, state,key,total cost,...  etc
initial_state = list()

#zero_initialization
board_len      = 0
board_side     = 0
nodes_expanded = 0

moves = list()  #there is another global moves in the export fun below
costs = set()


#-----------------------------------------------------BFS------------------------------------------------------------------------------
def bfs(start_state):                    #passing the initial_state_to_BFS_algorism

    global  goal_node

    explored= set() ; queue = deque([State(start_state, None, None, 0, 0, 0)]) #queue=frontier #q=deque ([])

    while queue: #frontier is not empty

        node = queue.popleft() #node= state object #remove and return the first in or the most left element

        explored.add(node.map)

        if node.state == goal_state: #node=State object  # accessing the state in the class to compare it with the goal if success
            goal_node = node
            return queue

        neighbors = expand(node)

        for neighbor in neighbors:
            if neighbor.map not in explored:
                queue.append(neighbor) #queue==frontier
                explored.add(neighbor.map)



#----------------------------------------------------DFS--------------------------------------------------------------------

def dfs(start_state):

    global goal_node

    explored=set(); stack =  list([State(start_state, None, None, 0, 0, 0)]) #here this means: list = stack, queue =deque

    while stack:                                                              #frontier = stack is not empty

        node = stack.pop()

        explored.add(node.map)                                                #node= state object

        if node.state == goal_state:
            goal_node = node
            return stack

        neighbors = reversed(expand(node))                                   #because it's a stack

        for neighbor in neighbors:
            if neighbor.map not in explored:
                stack.append(neighbor)
                explored.add(neighbor.map)


#--------------------------------------------------------------A*------------------------------------------------------------------------

#----------------------------------------------------------heuristics ------------------------------------------------------------------

#------------------------Manhattan_distance
def h(state):

    return sum(    abs(b % board_side - g % board_side) + abs(b//board_side - g//board_side)
               for b, g in (  ( state.index(i), goal_state.index(i)  ) for i in range(1, board_len)  )     ) #board_len=9


#--------------------------Euclidean_distance
def eclidean_h(state):


    ecl_sum = 0
    for i in range(1, 9):
        brd= state.index(i)  ; gl = goal_state.index(i)
        x = (brd % 3 - gl % 3) ** 2
        y = (brd // 3 - gl // 3) ** 2
        ecl_sum += math.sqrt(x+y)
    return ecl_sum
'''
    # the above code lines in this fun are the same as saying:
    return sum(    math.sqrt(   ((b % board_side - g % board_side)**2 + (b//board_side - g//board_side)**2)    )  #board_side=3
               for b, g in (  ( state.index(i), goal_state.index(i)  ) for i in range(1, board_len)  )     )  #board_len=9
'''
#-----------------------------------------------------------------------A* algorithm code -------------------------------
#--------------------------------------------------------------------using Manhattan_distance----------------------------
def ast(start_state):
    print('------------------------A* Using Manhattan Distance Heuristics------------------')
    global  goal_node
    explored=set(); heap=list(); heap_entry={}                  #dic #frontier=heap #not used in any thing below  counter = itertools.count()

    key = h(start_state)                                        #heuristics manhattan distance

    root = State(start_state, None, None, 0, 0, key)            #root=neighbor

    entry = (key, 0, root)                                      #tuple does not change

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:

        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == goal_state:
            goal_node = node[2]
            return heap

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key = neighbor.cost + h(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)         #neighbor.move means the element neighbor in the list move

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap)                                       #trannsform a list into a heap

#--------------------------------------------------------------------A* algorithm code --------------------------------
#----------------------------------------------------------------using Euclidean_distance------------------------------
def euclidean_ast(start_state):

    global  goal_node
    explored=set(); heap=list(); heap_entry={}                      #dic #frontier=heap #not used in any thing below  counter = itertools.count()
    key = eclidean_h(start_state)                                   #heuristics manhattan distance

    root = State(start_state, None, None, 0, 0, key)                #root=neighbor

    entry = (key, 0, root)                                           #tuple does not change

    heappush(heap, entry)

    heap_entry[root.map] = entry

    while heap:

        node = heappop(heap)

        explored.add(node[2].map)

        if node[2].state == goal_state:
            goal_node = node[2]
            return heap

        neighbors = expand(node[2])

        for neighbor in neighbors:

            neighbor.key = neighbor.cost + eclidean_h(neighbor.state)

            entry = (neighbor.key, neighbor.move, neighbor)                 #neighbor.move means the element neighbor in the list move

            if neighbor.map not in explored:

                heappush(heap, entry)

                explored.add(neighbor.map)

                heap_entry[neighbor.map] = entry

            elif neighbor.map in heap_entry and neighbor.key < heap_entry[neighbor.map][2].key:

                hindex = heap.index((heap_entry[neighbor.map][2].key,
                                     heap_entry[neighbor.map][2].move,
                                     heap_entry[neighbor.map][2]))

                heap[int(hindex)] = entry

                heap_entry[neighbor.map] = entry

                heapify(heap) #trannsform a list into a heap


#-------------------------------------------------Actions & paths --------------------------------------------------------------
def move(state, position):

    new_state = state[:]                                                                #every element in the array

    index = new_state.index(0)

    if position == 1:  # Up

        if index not in range(0, board_side):                                            #impossible = [0,1,2]

            temp = new_state[index - board_side]                                         #board_side=3
            new_state[index - board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 2:  # Down

        if index not in range(board_len - board_side, board_len):                       #impossible=range(9-3,9)=[6,7,8]

            temp = new_state[index + board_side]
            new_state[index + board_side] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 3:  # Left

        if index not in range(0, board_len, board_side):

            temp = new_state[index - 1]
            new_state[index - 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

    if position == 4:  # Right

        if index not in range(board_side - 1, board_len, board_side):

            temp = new_state[index + 1]
            new_state[index + 1] = new_state[index]
            new_state[index] = temp

            return new_state
        else:
            return None

#-------------------------------------------------------Expanding neibours & frontiers --------------------------------------------------
def expand(node):

    global nodes_expanded
    nodes_expanded += 1

    neighbors = list()

    neighbors.append(State(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))  #up  # state, parent, move, depth, cost, key
    neighbors.append(State(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))  #down
    neighbors.append(State(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))  #left
    neighbors.append(State(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))  #right

    nodes = [neighbor for neighbor in neighbors if neighbor.state]

    return nodes


#---------------------------------------------------- preparing of the output stage----------------------------------------------------
def backtrace():

    current_node = goal_node

    while initial_state != current_node.state:

        if current_node.move == 1:
            movement = 'Up'
        elif current_node.move == 2:
            movement = 'Down'
        elif current_node.move == 3:
            movement = 'Left'
        else:
            movement = 'Right'

        moves.insert(0, movement)
        current_node = current_node.parent                                                  #the parent node will be considered as a currnt node for the comming check or iteration

    return moves

#-----------------------------------------------------the output stage -----------------------------------------------------------------------
def export( time ):

    global moves
    global nodes_expanded
    moves = backtrace()

    print('1.Path To Goal:  ',end = '' )
    print_cyan(str(moves))

    print('2.Cost Of Path:  ' , end = '')
    print_cyan(str(len(moves)))
    print('3.Nodes Expanded:', end = '')
    print_cyan(str(nodes_expanded))

    print('4.Search Depth:  ' , end = '')               #search depth = max search depth i found in it my goal
    print_cyan(str(goal_node.depth))

    print('5.Running Time:  ', end = '' )
    print_cyan( format( time , '.8f'))

    # clearing everything in case we call the export method again in the A* algorithm using the Euclidean distance
    moves = []
    nodes_expanded=0
    goal_node.depth = {}

#-----------------------------------------------populating and reading  i/p from the the input stage ------------------------------------------------------
def inputread(configuration):                   # populates a configuration thing

    global board_len, board_side

    data = configuration.split(",")

    for element in data:
        initial_state.append(int(element))      #adding elements

    board_len = len(initial_state)

    board_side = int(board_len ** 0.5)          #sqrt root of 9 =3



#---------------------------------------------------------the main --------------------------------------------------------------------------
def main(algorithm,board):

    inputread(board)                             #calling the read fun or method

    if  algor_type == 'A*' or algor_type == 'a*' or algor_type == 'a star'or algor_type == 'A STAR'or algor_type == 'A Star'or algor_type == 'A star'or algor_type == 'A* ':
        print('------------------------A* Using Euclidean Distance Heuristics------------------')

        start = timeit.default_timer()           # This will return the default time before executing the next line
        euclidean_ast(initial_state)
        stop = timeit.default_timer()            # This will return the default time after executing the above previous line
        export( stop-start)

    function = function_map[algorithm]          #google told me that this tricky line we use when we wanna put the name of the calling algorithm from the user

    start = timeit.default_timer()              #This will return the default time before executing the next line
    function(initial_state)
    stop = timeit.default_timer()               #This will return the default time after executing the above previous line

    export( stop-start)

    print('--------------the Graphical user interface of the "8-Puzzle Game" is working in a new window now ------------------')
    print('------------------------------------End Of The program--------------------------\n-----------------------------------------bye..bye!------------------------')
    sol = backtrace()                           # sol=moves
    GUI(initial_state, sol)                     #if the algorithm choosen by the user is A* ,then i will make the Gui for manhatten distance heuristics only , in order not to duplicate the root and destroy the current tk, 34an md5l4 nfsy fe 7warat


function_map ={
    'BFS': bfs,'bfs': bfs,
    'DFS': dfs,'dfs': dfs,
    'A*' : ast, 'a*':ast, 'a star':ast, 'A STAR':ast, 'A Star':ast, 'A star':ast
    }


#-------#-------------------------------------------------inserting the input from the user-------------------------------------------------------------
algor_type    = input("Enter the algorithm type u wanna use..For ex,type works like these>> BFS,DFS,A* : ")
initial_board = input("Enter your initial state..For ex>> 0,8,7,6,5,4,3,2,1 or 1,2,5,3,4,0,6,7,8 or etc: ")
print('the program is running now! just wait for a second and the program will print your output in details')
main(algor_type,initial_board)