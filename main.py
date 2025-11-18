import tkinter as tk
import ttkbootstrap as ttk
import fun2048_gui


def update():
    global matr, score, isGameOver
    fun2048_gui.draw_grid(canvas, border, matr)
    score.set(sum(sum(x) for x in matr))
    isGameOver.set(fun2048_gui.noRoom(matr))
    if isGameOver.get():
        print('game over')
        # call game over function

def left_move():
    print('left')
    global matr
    matr = fun2048_gui.move(matr, 'a')
    update()


def right_move():
    print('right')
    global matr
    matr = fun2048_gui.move(matr, 'd')
    update()


def up_move():
    print('up')
    global matr
    matr = fun2048_gui.move(matr, 'w')
    update()


def down_move():
    print('down')
    global matr
    matr = fun2048_gui.move(matr, 's')
    update()


n = 4
border = 10
matr = fun2048_gui.matr_init(n, 2)


window = ttk.Window()
window.title("2048")
window.geometry("600x420")

score = tk.IntVar()
score.set(4)

isGameOver = tk.BooleanVar()
isGameOver.set(False)

canvas = ttk.Canvas(master=window, width=400, height=400)
canvas.configure(bg='#BDB76B')
canvas.pack(pady=10, padx=10, side='left')
height = canvas.winfo_reqheight()
width = canvas.winfo_reqwidth()

right_frame = ttk.Frame(window)

score_text = ttk.Label(right_frame, text='Score:', font=('Calibri', 15))
score_label = ttk.Label(right_frame, textvariable=score, font=("Calibri", 25))

fun2048_gui.draw_grid(canvas, border, matr)

input_frame = ttk.Frame(right_frame)
bottom_keys = ttk.Frame(input_frame)

left_button = ttk.Button(master=bottom_keys, text='<', command=left_move)
right_button = ttk.Button(master=bottom_keys, text='>', command=right_move)
up_button = ttk.Button(master=input_frame, text='^', command=up_move)
down_button = ttk.Button(master=bottom_keys, text='v', command=down_move)

up_button.pack(pady=5)
left_button.pack(side='left', padx=10)
right_button.pack(side='right', padx=10)
down_button.pack()
bottom_keys.pack(pady=5)
score_text.pack()
score_label.pack(pady=5)
input_frame.pack(pady=30, padx=20)
right_frame.pack(side='right')

# arrows
window.bind('<KeyPress-Right>', lambda event: right_move())
window.bind('<KeyPress-Left>', lambda event: left_move())
window.bind('<KeyPress-Up>', lambda event: up_move())
window.bind('<KeyPress-Down>', lambda event: down_move())

# wasd
window.bind('<KeyPress-d>', lambda event: right_move())
window.bind('<KeyPress-a>', lambda event: left_move())
window.bind('<KeyPress-w>', lambda event: up_move())
window.bind('<KeyPress-s>', lambda event: down_move())

window.mainloop()
