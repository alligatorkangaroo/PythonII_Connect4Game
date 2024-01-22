import tkinter as tk
from tkinter import messagebox
import Connect4Game as game


class Connect4GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Connect 4")
        """setting the attribute game to an instance of the class Connect4Game() """
        self.game = game.Connect4Game()
        """creates  an array of the game columns as buttons """
        self.buttons = []
        for col in range(7):
            button = tk.Button(master, text=str(col + 1), command=lambda c=col: self.make_move(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)
        """initializing the tkinter cnavas which will be the game area for the viewer"""
        self.canvas = tk.Canvas(master, width=7 * 60, height=6 * 60)
        self.canvas.grid(row=1, column=0, columnspan=7)
        self.draw_board()

    def make_move(self, column):
        """calls the make_move function of game and then the draw_board function to update the board"""
        self.game.make_move(column)
        self.draw_board()
        """checks if there is a winner after the move and displays if there is"""
        if self.game.winner is not None:
            winner_text = f"Player {self.game.winner} wins!"
            messagebox.showinfo("Game Over", winner_text)
            self.master.destroy()

    def draw_board(self):
        """draws the game board with instructions from the board object of game"""
        self.canvas.delete("all")
        """this nested for loop creates the 6 rows and 7 columns """
        for row in range(6):
            for col in range(7):
                x0, y0 = col * 60, row * 60
                x1, y1 = x0 + 60, y0 + 60
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="white")
                """if the value of the current space is 1 the function creates a red piece, if its 2,
                the function creates a yellow piece"""
                if self.game.board[row][col] == 1:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="red", outline="red")
                elif self.game.board[row][col] == 2:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill="yellow", outline="yellow")
"""checks if the columns are filled and if so, disables the button"""
        for col in range(7):
            if self.game.board[0][col] == 0:
                self.buttons[col]["state"] = tk.NORMAL
            else:
                self.buttons[col]["state"] = tk.DISABLED

"""initializing the main loop if the tkinter"""
if __name__ == "__main__":
    root = tk.Tk()
    app = Connect4GUI(root)
    root.mainloop()
