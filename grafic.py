from tkinter import *
from matrix import *
from logika import *

a = 8
matrix = matrix_generacia(8)


root = Tk()
root.geometry("800x600")
root.attributes("-fullscreen", False)
root.title("Saper")
root.iconbitmap("gameico/icons8-minesweeper-96.ico")
root["bg"] = "#FFFDD0"

flaga = PhotoImage(file="gameico/flaga.png")
n1 = PhotoImage(file="gameico/1.png")
n2 = PhotoImage(file="gameico/2.png")
n3 = PhotoImage(file="gameico/3.png")
n4 = PhotoImage(file="gameico/4.png")
n5 = PhotoImage(file="gameico/5.png")
n6 = PhotoImage(file="gameico/6.png")
n7 = PhotoImage(file="gameico/7.png")
n8 = PhotoImage(file="gameico/8.png")
bomba = PhotoImage(file="gameico/bomba.png")

label = Label(root, text = "Saper", font = ("Arial", 50, "bold"), fg = "#3F3E33", bg = "#FFFDD0")
label.pack()

canvas = Canvas(root, width = a * 64, height = a * 64, highlightthickness=2, highlightbackground="#B5B08E")
def reg():
    canvas.delete("all")
    for ii in range(a):
        for jj in range(a):
            canvas.create_rectangle(1 + 64 * ii, 1 + 64 * jj, 1 + 64 * (ii + 1), 1 + 64 * (jj + 1), fill="#FFFDD0", outline="#B5B08E")
            if matrix[jj][ii][1] == 2:
                canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=flaga, anchor="nw")
            if matrix[jj][ii][1] == 1:
                if matrix[jj][ii][0] == -1:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=bomba, anchor="nw")
                if matrix[jj][ii][0] == 0:
                    canvas.create_rectangle(1 + 64 * ii, 1 + 64 * jj, 1 + 64 * (ii + 1), 1 + 64 * (jj + 1), fill="#FFF9E6", outline="#B5B08E")
                if matrix[jj][ii][0] == 1:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n1, anchor="nw")
                if matrix[jj][ii][0] == 2:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n2, anchor="nw")
                if matrix[jj][ii][0] == 3:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n3, anchor="nw")
                if matrix[jj][ii][0] == 4:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n4, anchor="nw")
                if matrix[jj][ii][0] == 5:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n5, anchor="nw")
                if matrix[jj][ii][0] == 6:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n6, anchor="nw")
                if matrix[jj][ii][0] == 7:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n7, anchor="nw")
                if matrix[jj][ii][0] == 8:
                    canvas.create_image(1 + 64 * ii, 1 + 64 * jj, image=n8, anchor="nw")
def lkm(event):

    x = event.x // 64
    y = event.y // 64
    if not (0 <= x < a and 0 <= y < a):
        return
    open_cell(matrix, y, x)
    reg()


def rkm(event):
    x = event.x // 64
    y = event.y // 64
    if not (0 <= x < a and 0 <= y < a):
        return
    toggle_flag(matrix, y, x)
    reg()

canvas.bind("<Button-1>", lkm)
canvas.bind("<Button-3>", rkm)

reg()


canvas.pack()



def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))





root.bind("<F11>", toggle_fullscreen)

root.mainloop()
