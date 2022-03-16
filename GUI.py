# Asmaa Gamal
#state_class of Assignment 1
# Electronics & Communications department
#using informed and uninformed search Algorithms to solve 8-puzzle

# ---------------------------------------visualization---------------------------------------------
from tkinter import *

tk = Tk()

ANSI_RESET = "\u001B[0m"
ANSI_CYAN = "\u001B[36m"

def print_cyan(msg):
    print(f"{ANSI_CYAN}{msg}{ANSI_RESET}")


def init_button(num):
    if num == 0:
        return Label(tk, text=num, font='Times 25 bold', bg='grey', fg='black', height=4, width=8) #"tk"means to import the window of the TK library in this label
    else:
        return Label(tk, text=num, font='Times 25 bold', bg='cyan3', fg='black', height=4, width=8)


def shuffle(index, target,puzzle):  #puzzle=initial_state
    temp = puzzle[target]
    puzzle[target] = 0
    puzzle[index] = temp

def GUI(puzzle,sol):                #puzzle=initial_state  #sol=moves=position

    tk.title("                  GUI Solver Of The 8-Puzzle Game")
    index = 0

    button0 = init_button(puzzle[0])
    button0.grid(row=3, column=0)
    button1 = init_button(puzzle[1])
    button1.grid(row=3, column=1)
    button2 = init_button(puzzle[2])
    button2.grid(row=3, column=2)
    button3 = init_button(puzzle[3])
    button3.grid(row=4, column=0)
    button4 = init_button(puzzle[4])
    button4.grid(row=4, column=1)
    button5 = init_button(puzzle[5])
    button5.grid(row=4, column=2)
    button6 = init_button(puzzle[6])
    button6.grid(row=5, column=0)
    button7 = init_button(puzzle[7])
    button7.grid(row=5, column=1)
    button8 = init_button(puzzle[8])
    button8.grid(row=5, column=2)


    def fun(index):
        zero_place = puzzle.index(0)
        target = 0
        if zero_place == 0:
            if sol[index] == 'Down':
                target = 3
                button0["text"] = button3["text"]
                button0["bg"] = 'cyan2'
                tk.update()
                button3["text"] = 0
                button3["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Right':
                target = 1
                button0["text"] = button1["text"]
                button0["bg"] = 'cyan2'
                tk.update()
                button1["text"] = 0
                button1["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 1:
            if sol[index] == 'Left':
                target = 0
                button1["text"] = button0["text"]
                button1["bg"] = 'cyan2'
                tk.update()
                button0["text"] = 0
                button0["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Down':
                target = 4
                button1["text"] = button4["text"]
                button1["bg"] = 'cyan2'
                tk.update()
                button4["text"] = 0
                button4["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Right':
                target = 2
                button1["text"] = button2["text"]
                button1["bg"] = 'cyan2'
                tk.update()
                button2["text"] = 0
                button2["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 2:
            if sol[index] == 'Left':
                target = 1
                button2["text"] = button1["text"]
                button2["bg"] = 'cyan2'
                tk.update()
                button1["text"] = 0
                button1["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Down':
                target = 5
                button2["text"] = button5["text"]
                button2["bg"] = 'cyan2'
                tk.update()
                button5["text"] = 0
                button5["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 3:
            if sol[index] == 'Up':
                target = 0
                button3["text"] = button0["text"]
                button3["bg"] = 'cyan2'
                tk.update()
                button0["text"] = 0
                button0["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Down':
                target = 6
                button3["text"] = button6["text"]
                button3["bg"] = 'cyan2'
                tk.update()
                button6["text"] = 0
                button6["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Right':
                target = 4
                button3["text"] = button4["text"]
                button3["bg"] = 'cyan2'
                tk.update()
                button4["text"] = 0
                button4["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 4:
            if sol[index] == 'Up':
                target = 1
                button4["text"] = button1["text"]
                button4["bg"] = 'cyan2'
                tk.update()
                button1["text"] = 0
                button1["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Left':
                target = 3
                button4["text"] = button3["text"]
                button4["bg"] = 'cyan2'
                tk.update()
                button3["text"] = 0
                button3["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Down':
                target = 7
                button4["text"] = button7["text"]
                button4["bg"] = 'cyan2'
                tk.update()
                button7["text"] = 0
                button7["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Right':
                target = 5
                button4["text"] = button5["text"]
                button4["bg"] = 'cyan2'
                tk.update()
                button5["text"] = 0
                button5["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 5:
            if sol[index] == 'Up':
                target = 2
                button5["text"] = button2["text"]
                button5["bg"] = 'cyan2'
                tk.update()
                button2["text"] = 0
                button2["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Left':
                target = 4
                button5["text"] = button4["text"]
                button5["bg"] = 'cyan2'
                tk.update()
                button4["text"] = 0
                button4["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Down':
                target = 8
                button5["text"] = button8["text"]
                button5["bg"] = 'cyan2'
                tk.update()
                button8["text"] = 0
                button8["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 6:
            if sol[index] == 'Up':
                target = 3
                button6["text"] = button3["text"]
                button6["bg"] = 'cyan2'
                tk.update()
                button3["text"] = 0
                button3["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Right':
                target = 7
                button6["text"] = button7["text"]
                button6["bg"] = 'cyan2'
                tk.update()
                button7["text"] = 0
                button7["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 7:
            if sol[index] == 'Up':
                target = 4
                button7["text"] = button4["text"]
                button7["bg"] = 'cyan2'
                tk.update()
                button4["text"] = 0
                button4["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Left':
                target = 6
                button7["text"] = button6["text"]
                button7["bg"] = 'cyan2'
                tk.update()
                button6["text"] = 0
                button6["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Right':
                target = 8
                button7["text"] = button8["text"]
                button7["bg"] = 'cyan2'
                tk.update()
                button8["text"] = 0
                button8["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target,puzzle)
        elif zero_place == 8:
            if sol[index] == 'Up':
                target = 5
                button8["text"] = button5["text"]
                button8["bg"] = 'cyan2'
                tk.update()
                button5["text"] = 0
                button5["bg"] = 'grey'
                tk.update()
            elif sol[index] == 'Left':
                target = 7
                button8["text"] = button7["text"]
                button8["bg"] = 'cyan2'
                tk.update()
                button7["text"] = 0
                button7["bg"] = 'grey'
                tk.update()
            shuffle(zero_place, target, puzzle)
        if index != len(sol) - 1:
            index += 1
            tk.after(650, fun,index)
        index += 1

    tk.after(3000, fun,index)
    tk.mainloop()