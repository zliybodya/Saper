from tkinter import *
from matrix import *
from logik import *

a = 8
matrix = matrix_generacia(8)
first_move = True


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

canvas = Canvas(root, width = a * 64, height = a * 64, highlightbackground="#B5B08E")
def reg():
    canvas.delete("all")
    # Słownik mapujący wartości z macierzy na zmienne z obrazkami.
    # Zakładam, że zmienne n1, n2, flaga, bomba itd. są już zdefiniowane globalnie.
    images_map = {
        -1: bomba,
        1: n1, 2: n2, 3: n3, 4: n4,
        5: n5, 6: n6, 7: n7, 8: n8
    }
    
    CELL_SIZE = 64
    OFFSET = 1

    for col in range(a):      
        for row in range(a):  
            
            cell_content = matrix[row][col][0] # Wartość: -1 (bomba), 0 (puste), 1-8 (liczby)
            cell_state = matrix[row][col][1]   # Stan: 0 (zakryte), 1 (odkryte), 2 (flaga)
            
            x_pos = OFFSET + CELL_SIZE * col
            y_pos = OFFSET + CELL_SIZE * row
            fill_color = "#FFF9E6" 
            image_to_draw = None   

            if cell_state == 0 or cell_state == 2: # Zakryta lub flaga
                fill_color = "#FFFDD0"
                if cell_state == 2:
                    image_to_draw = flaga
            else: # Komórka odkryta (cell_state == 1)
                image_to_draw = images_map.get(cell_content)

            canvas.create_rectangle(
                x_pos, y_pos, 
                x_pos + CELL_SIZE, y_pos + CELL_SIZE, 
                fill=fill_color, outline="#B5B08E"
            )

            if image_to_draw:
                canvas.create_image(x_pos, y_pos, image=image_to_draw, anchor="nw")
def lkm(event):

    global first_move
    x = (event.x + 1) // 64
    y = (event.y + 1) // 64
    if not (0 <= x < a and 0 <= y < a):
        return
    if first_move:
        clear_safe_zone(matrix, y, x)
        first_move = False
    open_cell(matrix, y, x)
    reg()


def rkm(event):
    x = (event.x + 1) // 64
    y = (event.y + 1) // 64
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
