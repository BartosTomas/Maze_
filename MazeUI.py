import tkinter as tk
import tkinter.ttk as ttk
import Translator as translator

class MazeUI:
    def __init__(self):
        # Maze info from transcript 
        self.maze_transcript = [[1,0,0,0,0,0,0,0,0,1],[0,1,1,0,0,1,0,1,1,0],[0,1,0,0,1,0,0,0,1,0],[0,0,0,1,1,0,1,0,0,0],[0,1,0,0,0,0,1,1,0,0],[0,0,1,1,0,0,0,0,1,0],[0,0,0,1,0,1,1,0,0,0],[0,1,0,0,0,1,0,0,1,0],[0,1,1,0,1,0,0,1,1,2],[1,0,0,0,0,0,0,0,0,1]] # translator.transcript
        self.maze_width = 10 #translator.width
        self.maze_height = 10 #translator.height
        self.UI()

    def UI(self):
        window = tk.Tk()
        window.geometry("900x700")
        window.configure(bg="lightgray")
        window.title("Maze")
        # Grid -----------
        for column in range(6):
            window.columnconfigure(column, minsize=100)
        window.columnconfigure(6, minsize=80)
        window.columnconfigure(7, minsize=20)
        window.columnconfigure(8, minsize=80)
        window.columnconfigure(9, minsize=20)
        
        window.rowconfigure(0, minsize=100)
        window.rowconfigure(1, minsize=100)
        window.rowconfigure(2, minsize=50)
        window.rowconfigure(3, minsize=50)
        window.rowconfigure(4, minsize=100)
        window.rowconfigure(5, minsize=50)
        window.rowconfigure(6, minsize=50)
        window.rowconfigure(7, minsize=100)
        window.rowconfigure(8, minsize=100)

        # UI widgets ----
        self.draw_maze(window)
        self.draw_buttons(window)

        window.mainloop()
    


    def draw_maze(self, window):
        height = 500
        width = 500
        canvas = tk.Canvas(window, height= height, width= width)
        block_height = height / self.maze_height
        block_width = width / self.maze_width
        for y in range(self.maze_height):
            for x in range(self.maze_width):
                if self.maze_transcript[y][x] == 1:
                    block = canvas.create_rectangle(x*block_width, y*block_height, (x+1)*block_width,(y+1)*block_height, fill="black")
                elif self.maze_transcript[y][x] == 2:
                    socket_path = canvas.create_rectangle(x*block_width, y*block_height, (x+1)*block_width,(y+1)*block_height, fill="white")
                    socket = canvas.create_oval(x*block_width+5, y*block_height+5, (x+1)*block_width-5,(y+1)*block_height-5, fill="limegreen", width=2)
                    eye1 = canvas.create_rectangle(x*block_width+5+10, y*block_height+5+10, (x)*block_width+5+15,(y)*block_height+5+22, fill="black")
                    eye1 = canvas.create_rectangle((x+1)*block_width-5-10, (y+1)*block_height-5-18, (x+1)*block_width-5-15,(y+1)*block_height-5-30, fill="black")
                    mouth = canvas.create_arc((x)*block_width+5+17, (y+1)*block_height-5-10, (x+1)*block_width-5-17,(y+1)*block_height-5-10, fill="black", style=tk.CHORD)
                else:
                    path = canvas.create_rectangle(x*block_width, y*block_height, (x+1)*block_width,(y+1)*block_height, fill="white")
        canvas.grid( column=1, row=1, columnspan=5, rowspan=7, sticky="SNEW")

    def draw_buttons(self, window):
        select_maze = tk.Label(window, text="Select maze")
        select_maze.configure(bg="lightgray", font="Helvetica 14 bold")
        select_maze.grid(row=1, column=6, columnspan=4, sticky="SEW")

        choose = ttk.Combobox(window, textvariable= tk.StringVar(), font="Helvetica 10 bold")
        choose['values'] = ["MazeScript0", "MazeScript1", "MazeScript2"]
        choose.grid(row=2, column=6, columnspan=4, sticky="SNEW", padx=5, pady=5)

        from_file = tk.Entry(window, justify="center", font="Helvetica 10 bold")
        from_file.insert(0, "Copy path to maze from PC")
        from_file.grid(row=3, column=6, columnspan=3, sticky="SNEW", padx=5, pady=5)
        def clear():
            clear_window = 1
        clear_from_file = tk.Button(window, text="X", command=clear,bg="lightgray", font="Helvetica 10 bold")
        clear_from_file.grid(row=3, column=9, sticky="SNEW", pady=5)

        coords = tk.Label(window, text="Coordinates of Robot")
        coords.configure(bg="lightgray", font="Helvetica 14 bold")
        coords.grid(row=4, column=6, columnspan=4, sticky="SEW", padx=5, pady=10)

        def add():
            n=n+1

        def subtract():
            n=n-1

        x_coord = tk.Entry(window, width=3, justify="center", font="Helvetica 25 bold")
        x_coord.insert(0, "X")
        x_coord.grid(row=5, column=6, rowspan=2, sticky="SNEW", padx=5)
        up_x = tk.Button(window, text="▲", command=add, bg="lightgray", font="Helvetica 10 bold")
        up_x.grid(row=5, column=7, sticky="SNEW")
        down_x = tk.Button(window, text="▼", command=subtract, bg="lightgray", font="Helvetica 10 bold")
        down_x.grid(row=6, column=7, sticky="SNEW")

        y_coord = tk.Entry(window, width=3, justify="center", font="Helvetica 25 bold")
        y_coord.insert(0, "Y")
        y_coord.grid(row=5, column=8, rowspan=2, sticky="SNEW", padx=5)
        up_y = tk.Button(window, text="▲", command=add, bg="lightgray", font="Helvetica 10 bold")
        up_y.grid(row=5, column=9, sticky="SNEW")
        down_y = tk.Button(window, text="▼", command=subtract, bg="lightgray", font="Helvetica 10 bold")
        down_y.grid(row=6, column=9, sticky="SNEW")

        def go():
            print("help")
        play = tk.Button(window, text="Play!", command=go, bg="limegreen", font="Helvetica 25 bold")
        play.grid(row=7, column=6, columnspan=4, sticky="SNEW", padx=5, pady=10)

'''
int_variable.type() - returns type of variable as <class 'int'>
'''
if __name__ == "__main__":
    maze = MazeUI()