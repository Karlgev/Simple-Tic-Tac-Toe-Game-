# Tic-Tac-Toe-Game-with-AI
# This Python program implements a Tic Tac Toe game with a twist. The main objective of the game is to create an
# impossible-to-win version of Tic Tac Toe against an AI opponent. The game board is not the typical 3x3 grid but a
# larger 9x9 grid (and can be further expanded) to make it more challenging for the player.

# Future Developments:
# In the future, the AI will be trained using machine learning to become unbeatable on larger boards, including
# 16x16 and even bigger grids. This will introduce even more complexity and challenge to the game.

# Dependencies:
# This game requires the Tkinter library, which is included in most standard Python installations. If you encounter
# any issues, ensure that Tkinter is installed on your system.

from tkinter import *


# Game Settings
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"

# Initialize the player's turn ('x' represents Player X, 'o' represents Player O)
turn = ""

# Keeping count of the rounds played in the game
turn_count = 1

# Initialize the countdown time (in seconds)
five_second = 1
countdown_time = five_second

# Dictionary to keep track of the status of each position on the game board
available_pos = {1: "na",  # 'na' means not assigned, will be updated to 'x' or 'o' when clicked
                 2: "na",
                 3: "na",
                 4: "na",
                 5: "na",
                 6: "na",
                 7: "na",
                 8: "na",
                 9: "na"}

# Track the set of clicked buttons (store the IDs of buttons that have been clicked)
clicked_buttons_id = []

#  Using the 'draw' flag to prevent premature draw results
draw = False

# List to store references to the button widgets
buttons = []

# Variable to store the AI's symbol ('x' or 'o')
ai = ""

# Variable to store the player's symbol ('x' or 'o')
player = ""


# Function to handle button clicks
def on_button_click(button_id):
    global turn_count
    global draw

    # Prevent from clicking the same button
    if button_id not in clicked_buttons_id:

        # Increment the turn count to track the progress of the game
        turn_count += 1

        if player == "x":
            # Turn the button to 'x'
            assigning_x(button_id)

        else:
            # Turn the button to 'o'
            assigning_o(button_id)

        # Check if the middle button was selected
        if is_player(5) and turn_count == 2:
            # Set 'draw' to true to enable 'its_draw()' on every turn
            draw = True

        if draw:
            its_draw()
        else:
            its_win()

        # Check for a win
        if check_win(available_pos) == "won":
            # If the game is won, disable all buttons, show the result, and start the countdown
            disable_all_buttons(buttons)
            canvas.itemconfig(title_text, text="X WON", fill="red")
            countdown()

        elif turn_count == 5:
            # If it's a draw (all buttons used), disable buttons, show draw result, and start the countdown
            disable_all_buttons(buttons)
            disable_all_buttons(buttons)
            canvas.itemconfig(title_text, text="DRAW", fill="blue")
            countdown()


def player_choose_o():
    global turn
    global ai
    global player
    # Set AI to 'x' and player to 'o'
    ai = "x"
    player = "o"
    turn = "x"
    button_for_o.grid_forget()
    button_for_x.grid_forget()

    # Create game buttons
    create_buttons()
    begin_game()


def player_choose_x():
    global turn
    global ai
    global player
    # Set AI to 'x' and player to 'o'
    ai = "o"
    player = "x"
    turn = "o"
    button_for_o.grid_forget()
    button_for_x.grid_forget()

    # Create game buttons
    create_buttons()
    begin_game()


# Function to disable_all_buttons
def disable_all_buttons(buttons_list):
    for button in buttons_list:
        button.config(state="disabled")


# Function to check if a player has won
def check_win(d):
    # list of possible consecutive wining sequences
    win_sequences = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

    for sequence in win_sequences:
        if all(d[key] == ai for key in sequence):
            return "won"


# Function to handle winning conditions for player X
def its_win():
    if ai == "x":
        assign = assigning_x
    else:
        assign = assigning_o

    # for testing
    # print(ai)
    # print(turn_count)
    # # for key, value in available_pos.items():
    # #     print(f"{key}: {value}")

    if not is_player(9) and turn_count == 2:
        if is_not_assigned(8):
            assign(9)
        else:
            assign(1)
    elif is_player(9) and turn_count == 2:
        assign(1)
    elif is_ai(9) and turn_count == 3:
        if is_not_assigned(8):
            assign(8)
        elif is_player(8) and is_player(6):
            assign(1)
        elif is_player(4) and is_player(8):
            assign(3)
        elif is_player(1) and is_player(8):
            assign(3)
        elif is_player(3) and is_player(8):
            assign(1)
        else:
            assign(1)
    elif is_ai(1) and turn_count == 3:
        if is_player(4):
            assign(3)
        else:
            assign(4)
    elif is_not_assigned(5) and turn_count == 4:
        assign(5)
    elif is_ai(1) and is_ai(3) and is_not_assigned(2) and turn_count == 4:
        assign(2)
    elif is_ai(3) and is_ai(9) and is_not_assigned(6) and turn_count == 4:
        assign(6)
    elif is_ai(1) and is_not_assigned(4) and turn_count == 4:
        assign(4)
    elif is_ai(9) and is_not_assigned(8) and turn_count == 4:
        assign(8)


# Function to handle draw conditions
def its_draw():
    if ai == "x":
        assign = assigning_x
    else:
        assign = assigning_o

    if is_player(5) and turn_count == 2:
        assign(9)
    elif is_not_assigned(8) and turn_count == 3:
        assign(8)
    elif is_player(8) and turn_count == 3:
        assign(2)
    elif is_player(4) and turn_count == 4 or is_player(1) and turn_count == 4:
        assign(6)
    elif is_player(6) and turn_count == 4 or is_player(3) and turn_count == 4:
        assign(4)
    elif is_player(1) and is_player(3) and turn_count == 5:
        if is_not_assigned(6):
            assign(6)
        elif is_not_assigned(4):
            assign(4)
    elif is_player(1) and turn_count == 5:
        assign(3)
    elif is_player(3) and turn_count == 5:
        assign(1)


# Function to check if a specific position is selected by ai
def is_ai(num):
    return available_pos[num] == ai


# Function to check if a specific position is selected by player
def is_player(num):
    return available_pos[num] == player


# Function to check if a specific position is empty ('na' for 'not assigned')
def is_not_assigned(num):
    return available_pos[num] == "na"


# Function to assign 'o' to a button and update game state
def assigning_o(button_id):
    global turn
    global turn_count

    # Load and set the 'o.png' image for the clicked button
    new_image = load_image('images/o.png')
    buttons[button_id-1].config(image=new_image)
    buttons[button_id-1].image = new_image

    # Update the game's current turn to 'x'
    turn = "x"

    # Mark the clicked position as 'o' in the game state
    available_pos[button_id] = "o"

    # Add the button's ID to the list of clicked buttons
    clicked_buttons_id.append(button_id)


# Function to assign 'x' to a button and update game state
def assigning_x(button_id):
    global turn
    global turn_count

    # Load and set the 'x.png' image for the clicked button
    new_image = load_image('images/x.png')
    buttons[button_id-1].config(image=new_image)
    buttons[button_id-1].image = new_image

    # Update the game's current turn to 'o'
    turn = "o"

    # Add the button's ID to the list of clicked buttons
    clicked_buttons_id.append(button_id)

    # Mark the clicked position as 'x' in the game state
    available_pos[button_id] = "x"


def begin_game():
    global turn
    global turn_count

    if turn == "x":
        # AI starts with "x"
        assigning_x(7)

        # Set the initial turn to 'o'
        turn = "o"
        # Update the game state to mark the initial move as 'x'
        available_pos[7] = "x"

        # Add the initial move (button 7) to the list of clicked buttons
        clicked_buttons_id.append(7)
    else:
        # AI starts with "o"
        assigning_o(7)

        # Set the initial turn to 'x'
        turn = "x"
        # Update the game state to mark the initial move as 'o'
        available_pos[7] = "o"

        # Add the initial move (button 7) to the list of clicked buttons
        clicked_buttons_id.append(7)


# Function to reset the game
def restart():
    global turn
    global available_pos
    global turn_count
    global draw
    global countdown_time

    # Reset the turn to the initial player
    turn = ai

    # Clear the set of clicked buttons
    clicked_buttons_id.clear()

    # Reset all buttons to their initial state (empty image)
    for i in range(9):
        buttons[i].config(image=empty_box, state=NORMAL)
        buttons[i].image = empty_box

    # Reset the turn count to 1 and initialize game state
    turn_count = 1
    available_pos = restart_dict()

    # Begin the game with the initial move
    begin_game()

    # Reset the draw flag to prevent premature draw
    draw = False

    # Update the game title to "Tic Tac Toe" and reset text color to black
    canvas.itemconfig(title_text, text="Tic Tac Toe", fill="black")

    # Enable the restart button for a new game
    restart_button.config(state="active")

    # Reset the countdown timer to its initial value (5 seconds)
    countdown_time = five_second


# Function to initialize and return a dictionary representing the available positions
def restart_dict():
    return {1: "na", 2: "na", 3: "na", 4: "na", 5: "na", 6: "na", 7: "na", 8: "na", 9: "na"}


# Function to control the countdown
def countdown():
    global countdown_time

    # Disable the restart button during the countdown
    restart_button.config(state="disabled")

    # Check if there is time remaining
    if countdown_time >= 0:

        # Update the timer label to display the current countdown time
        countdown_label.config(text=str(countdown_time))
        countdown_time -= 1
        window.after(1000, countdown)

    # If the countdown reaches 0 or becomes negative, restart the game
    elif countdown_time < 0:
        restart()


# Function to load an image from a file path and handle exceptions
def load_image(file_path):
    try:
        image = PhotoImage(file=file_path)
        return image
    except Exception as e:
        print(f"Error loading image: {str(e)}")
        return None

# Function to create buttons for the grid
def create_buttons():
    # Create a list to store your buttons
    global buttons
    for i in range(1, 10):
        # Calculate the coordinates for button placement
        x = 187 + ((i - 1) % 3) * 130
        y = 187 + ((i - 1) // 3) * 130

        # Create a button with an image, no border, and attach a command
        button = Button(image=empty_box, highlightthickness=0, command=lambda i=i: on_button_click(i))
        button.place(x=x, y=y)

        # Append the button to the list of buttons
        buttons.append(button)


# Create the main window
window = Tk()
window.title('Tic Tac Toe')
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

# Create the canvas for the game board
canvas = Canvas(window, width=800, height=800)
title_text = canvas.create_text(400, 100, text='Tic Tac Toe', font=(FONT_NAME, 35, 'bold'), fill='black')

# Configure the canvas settings
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=5)

# Create a label for the countdown countdown_label
countdown_label = Label(window, text="", font=("Helvetica", 48), bg=BACKGROUND_COLOR)
countdown_label.grid(row=0, columnspan=1)

# Create buttons for the game
empty_box = load_image('images/empty_box.png')
image_of_x = load_image('images/x.png')
image_of_o = load_image('images/o.png')

# Create buttons for player choice
button_for_x = Button(image=image_of_x, highlightthickness=0, command=player_choose_x)
button_for_x.grid(row=0, column=1)

button_for_o = Button(image=image_of_o, highlightthickness=0, command=player_choose_o)
button_for_o.grid(row=0, column=3)

# Create buttons for the Tic Tac Toe grid and set their positions
restart_button = Button(text="Restart", font=(FONT_NAME, 35, 'bold'), highlightthickness=0, command=restart)
restart_button.place(x=255, y=700)

window.mainloop()
