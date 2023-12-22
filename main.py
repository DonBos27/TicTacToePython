import tkinter
import tkinter.messagebox
from pathlib import Path


def winner_of_game():
    global win
    if not win:
        win = True
        print("Player ", current_player, " won the game. Congratulations !!!")
        result = tkinter.messagebox.showinfo(
            title="Winner!",
            message=f"Player {current_player} won the game. Congratulations!",
            icon=tkinter.messagebox.INFO
        )
        if result == "" or result == "ok":
            root.destroy()


def switch_player():
    global current_player
    if current_player == 'X':
        current_player = '0'
    else:
        current_player = 'X'


def check_win(clicked_row, clicked_col):
    try:
        # detect horizontally
        count = 0
        for i in range(3):
            current_button = buttons[i][clicked_row]
            if current_button.winfo_exists() and current_button['text'] == current_player:
                count += 1
        if count == 3:
            print('Horizontal win')
            winner_of_game()

        # detect vertically
        count = 0
        for i in range(3):
            current_button = buttons[clicked_col][i]
            if current_button.winfo_exists() and current_button['text'] == current_player:
                count += 1
        if count == 3:
            print('Vertical win')
            winner_of_game()

        # detect diagonal starting from left
        count = 0
        for i in range(3):
            current_button = buttons[i][i]
            if current_button.winfo_exists() and current_button['text'] == current_player:
                count += 1
        if count == 3:
            winner_of_game()

        # detect diagonal starting from right
        count = 0
        for i in range(3):
            current_button = buttons[2 - i][i]
            if current_button.winfo_exists() and current_button['text'] == current_player:
                count += 1
        if count == 3:
            winner_of_game()

        if win is False:
            count = 0
            for col in range(3):
                for row in range(3):
                    current_button = buttons[col][row]
                    if current_button.winfo_exists() and (
                            current_button['text'] == 'X' or current_button['text'] == '0'):
                        count += 1
                    if count == 9:
                        result = tkinter.messagebox.showinfo(
                            title="Draw!",
                            message="It's a draw !",
                            icon=tkinter.messagebox.INFO
                        )
                        if result == "" or result == "ok":
                            root.destroy()
    except tkinter.TclError as e:
        if "application has been destroyed" not in str(e):
            raise


def place_symbol(row, column):
    print("click", row, column)

    clicked_button = buttons[column][row]
    if clicked_button.winfo_exists():  # Check if the button still exists
        if clicked_button['text'] == "":
            clicked_button.config(text=current_player)

            check_win(row, column)
            switch_player()


def drawing_grid():
    for col in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(
                root, font=("Arial", 70),
                # text="X",
                width=3,
                height=1,
                command=lambda r=row, c=col: place_symbol(r, c)
            )
            button.grid(row=row, column=col)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)


# Stockages
buttons = []
current_player = 'X'
win = False

# Create a window to open the game
root = tkinter.Tk()

# Add icon to the application
icon_path = Path(r"C:\Users\Hp\PycharmProjects\TicTacToe\TicTacToe.ico")
root.iconbitmap(default=icon_path)

# personalised the window
root.title("TicTacToe")
root.minsize(200, 300)

drawing_grid()
root.mainloop()
