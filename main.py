from tkinter import *

# Define constants for better readability
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"

# Initialize the player's turn
turn = "x"

# Function to handle button clicks
def on_button_click(button_id):
    global turn
    button = buttons[button_id - 1]

    # Check whose turn it is and handle accordingly
    if turn == "x":
        print("X Button Clicked!")

        # Load and set the 'x.png' image
        new_image = PhotoImage(file='images/x.png')
        button.config(image=new_image)
        button.image = new_image

        # Disable the button and switch to the other player's turn
        button.config(state=DISABLED)
        turn = "o"
    else:
        print("O Button Clicked!")

        # Load and set the 'o.png' image
        new_image = PhotoImage(file='images/o.png')
        button.config(image=new_image)
        button.image = new_image

        # Disable the button and switch to the other player's turn
        button.config(state=DISABLED)
        turn = "x"

# Function to reset the game
def restart():
    global turn

    # Reset the turn to the initial player
    turn = "x"

    # Clear the set of clicked buttons
    clicked_buttons.clear()

    # Reset all buttons to their initial state (empty image)
    empty_box = PhotoImage(file='images/empty_box.png')
    for i in range(9):
        buttons[i].config(image=empty_box, state=NORMAL)
        buttons[i].image = empty_box

# Create the main window
window = Tk()
window.title('Tic Tac Toe')
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)
canvas = Canvas(window, width=800, height=800)
card_front = PhotoImage(file='images/bord.png')
card_back = PhotoImage(file='images/card_back.png')
main_image = canvas.create_image(400, 400, image=card_front)
title_text = canvas.create_text(400, 100, text='Tic Tac Toe', font=(FONT_NAME, 35, 'bold'), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# Create buttons for the game
empty_box = PhotoImage(file='images/empty_box.png')
buttons = []
for i in range(1, 10):
    x = 187 + ((i - 1) % 3) * 130
    y = 187 + ((i - 1) // 3) * 130

    button = Button(image=empty_box, highlightthickness=0, command=lambda i=i: on_button_click(i))
    button.place(x=x, y=y)
    buttons.append(button)

# Create a restart button
restart_button = Button(text="Restart", font=(FONT_NAME, 35, 'bold'), highlightthickness=0, command=restart)
restart_button.place(x=255, y=700)

# Track the set of clicked buttons
clicked_buttons = set()

# Start the main loop
window.mainloop()
