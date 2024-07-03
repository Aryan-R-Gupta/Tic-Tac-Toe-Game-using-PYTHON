import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("600x600")
        self.window.configure(background='#F5F5DC') 

        self.welcome_screen()

    def welcome_screen(self):
        welcome_label = tk.Label(self.window, text="Welcome to Tic Tac Toe by Aryan!", font=("Arial", 30), bg='#F5F5DC')
        welcome_label.pack(pady=100)

        start_button = tk.Button(self.window, text="Start", command=self.start_game, font=("Arial", 20), bg='#F5F5DC')
        start_button.pack(pady=50)

    def start_game(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.player_turn = "X"

        self.main_frame = tk.Frame(self.window, bg='#F5F5DC')
        self.main_frame.pack(pady=50)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.main_frame, command=lambda row=i, column=j: self.click(row, column), height=6, width=12, font=("Arial", 20))
                button.grid(row=i, column=j, padx=20, pady=20)  
                row.append(button)
            self.buttons.append(row)

       
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width/2) - (600/2)
        y = (screen_height/2) - (600/2)
        self.window.geometry(f'600x600+{int(x)}+{int(y)}')

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                messagebox.showinfo("Game Over!", f"Player {self.player_turn} wins!")
                self.window.quit()
            elif self.check_tie():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.window.quit()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text']!= "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text']!= "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text']!= "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text']!= "":
            return True
        return False

    def check_tie(self):
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()