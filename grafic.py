from tkinter import *
from matrix import *
from logik import *

a = 8
cell_size = 64
matrix = matrix_generacia(8)
first_move = True


root = Tk()
root.geometry("800x600")
root.attributes("-fullscreen", False)
root.title("Saper")
root.iconbitmap("gameico/icons8-minesweeper-96.ico")

root["bg"] = "#FFFDD0"

# Загружаем оригинальные картинки (64x64)
flaga_orig = PhotoImage(file="gameico/flaga.png")
n1_orig = PhotoImage(file="gameico/1.png")
n2_orig = PhotoImage(file="gameico/2.png")
n3_orig = PhotoImage(file="gameico/3.png")
n4_orig = PhotoImage(file="gameico/4.png")
n5_orig = PhotoImage(file="gameico/5.png")
n6_orig = PhotoImage(file="gameico/6.png")
n7_orig = PhotoImage(file="gameico/7.png")
n8_orig = PhotoImage(file="gameico/8.png")
bomba_orig = PhotoImage(file="gameico/bomba.png")

def scale_image(img, size):
    if size == 64:
        return img
    elif size == 32:
        return img.subsample(2, 2)
    elif size == 48:
        return img.zoom(3, 3).subsample(4, 4)
    else:
        return img

def update_images(size):
    global flaga, n1, n2, n3, n4, n5, n6, n7, n8, bomba
    flaga = scale_image(flaga_orig, size)
    n1 = scale_image(n1_orig, size)
    n2 = scale_image(n2_orig, size)
    n3 = scale_image(n3_orig, size)
    n4 = scale_image(n4_orig, size)
    n5 = scale_image(n5_orig, size)
    n6 = scale_image(n6_orig, size)
    n7 = scale_image(n7_orig, size)
    n8 = scale_image(n8_orig, size)
    bomba = scale_image(bomba_orig, size)

update_images(cell_size)

label = Label(root, text = "Saper", font = ("Arial", 50, "bold"), fg = "#3F3E33", bg = "#FFFDD0")
label.pack()

canvas = Canvas(root, width = a * cell_size, height = a * cell_size, highlightbackground="#B5B08E")
def reg():
    canvas.delete("all")
    for ii in range(a):
        for jj in range(a):
            if matrix[jj][ii][1] == 0 or matrix[jj][ii][1] == 2:
                canvas.create_rectangle(1 + cell_size * ii, 1 + cell_size * jj, 1 + cell_size * (ii + 1), 1 + cell_size * (jj + 1), fill="#FFFDD0", outline="#B5B08E")
                if matrix[jj][ii][1] == 2:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=flaga, anchor="nw")
            else:
                canvas.create_rectangle(1 + cell_size * ii, 1 + cell_size * jj, 1 + cell_size * (ii + 1), 1 + cell_size * (jj + 1), fill="#FFF9E6", outline="#B5B08E")
                if matrix[jj][ii][0] == -1:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=bomba, anchor="nw")
                if matrix[jj][ii][0] == 1:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n1, anchor="nw")
                if matrix[jj][ii][0] == 2:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n2, anchor="nw")
                if matrix[jj][ii][0] == 3:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n3, anchor="nw")
                if matrix[jj][ii][0] == 4:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n4, anchor="nw")
                if matrix[jj][ii][0] == 5:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n5, anchor="nw")
                if matrix[jj][ii][0] == 6:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n6, anchor="nw")
                if matrix[jj][ii][0] == 7:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n7, anchor="nw")
                if matrix[jj][ii][0] == 8:
                    canvas.create_image(1 + cell_size * ii, 1 + cell_size * jj, image=n8, anchor="nw")
def lkm(event):

    global first_move
    x = (event.x + 1) // cell_size
    y = (event.y + 1) // cell_size
    if not (0 <= x < a and 0 <= y < a):
        return
    if first_move:
        clear_safe_zone(matrix, y, x)
        first_move = False
    open_cell(matrix, y, x)
    reg()


def rkm(event):
    x = (event.x + 1) // cell_size
    y = (event.y + 1) // cell_size
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
