import tkinter as tk

PLAYER1 = "PLAYER1"
PLAYER2 = "PLAYER2"
O = "O"
X = "X"
BLANK = ""


class TicTacToeFrame(tk.Frame):


    def __init__(self, parent):

        tk.Frame.__init__(self, parent)

        self.turn = PLAYER1

        self.board = []

        for i in range(3):

            l = []

            line = tk.Frame(self)
            line.pack()

            for j in range(3):

                button_text = tk.StringVar(line, BLANK)
                button = tk.Button(
                    line,
                    textvariable=button_text,
                    width=1,
                    command = self.press(i, j)
                    )
                button.pack(side=tk.LEFT)

                l.append((button_text, button))

            self.board.append(l)


    def press(self, i, j):

        def real_press():
            button_text, button = self.board[i][j]

            if self.turn == PLAYER1:
                button_text.set(O)
                self.turn = PLAYER2
            
            elif self.turn == PLAYER2:
                button_text.set(X)
                self.turn = PLAYER1

        return real_press


if __name__ == "__main__":
    window = tk.Tk()
    app = TicTacToeFrame(window)
    app.pack()
    window.mainloop()
