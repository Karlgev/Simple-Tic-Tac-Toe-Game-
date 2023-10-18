from tkinter import *


# TODO: add comment and make the code better

# Game Settings
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"

# Initialize the player's turn ('x' represents Player X, 'o' represents Player O)
turn = "x"

# Keeping count of the rounds played in the game
turn_count = 1

# Initialize the countdown time (in seconds)
five_second = 5
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


# Function to handle button clicks
def on_button_click(button_id):
    global turn
    global turn_count
    global draw

    # Prevent from clicking the same button
    if button_id not in clicked_buttons_id:
        # Turn the button to 'o'
        assigning_o(button_id)

        # Check if the middle button was selected
        if is_player_o(5) and turn_count == 2:
            # Set 'draw' to true to enable 'its_draw()' on every turn
            draw = True

        if draw:
            its_draw()
        else:
            its_win()

        # Check for a win
        if check_win(available_pos) == "won":
            disable_all_buttons(buttons)
            canvas.itemconfig(title_text, text="X WON", fill="red")
            timer()

        elif turn_count == 6:
            disable_all_buttons(buttons)
            canvas.itemconfig(title_text, text="DRAW", fill="blue")
            timer()


# Function to disable_all_buttons
def disable_all_buttons(buttons_list):
    for button in buttons_list:
        button.config(state="disabled")


# Function to check if a player has won
def check_win(d):
    # list of possible consecutive wining sequences
    win_sequences = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

    for sequence in win_sequences:
        if all(d[key] == "x" for key in sequence):
            return "won"


# Function to handle winning conditions for player X
def its_win():
    if not is_player_o(9) and turn_count == 2:
        if is_not_assigned(8):
            assigning_x(9)
        else:
            assigning_x(1)
    elif is_player_o(9) and turn_count == 2:
        assigning_x(1)
    elif is_player_x(9) and turn_count == 3:
        if is_player_o(8) and is_player_o(6):
            assigning_x(1)
        elif is_player_o(4) and is_player_o(8):
            assigning_x(3)
        elif is_not_assigned(8):
            assigning_x(8)
        else:
            assigning_x(1)
    elif is_player_x(1) and turn_count == 3:
        if is_player_o(4):
            assigning_x(3)
        else:
            assigning_x(4)
    elif is_not_assigned(5) and turn_count == 4:
        assigning_x(5)
    elif is_player_x(1) and is_player_x(3) and is_not_assigned(2) and turn_count == 4:
        assigning_x(2)
    elif is_player_x(3) and is_player_x(9) and is_not_assigned(6) and turn_count == 4:
        assigning_x(6)
    elif is_player_x(1) and is_not_assigned(4) and turn_count == 4:
        assigning_x(4)
    elif is_player_x(9) and is_not_assigned(8) and turn_count == 4:
        assigning_x(8)


# Function to handle draw conditions
def its_draw():
    if is_player_o(5) and turn_count == 2:
        assigning_x(9)
    elif is_not_assigned(8) and turn_count == 3:
        assigning_x(8)
    elif is_player_o(8) and turn_count == 3:
        assigning_x(2)
    elif is_player_o(4) and turn_count == 4 or is_player_o(1) and turn_count == 4:
        assigning_x(6)
    elif is_player_o(6) and turn_count == 4 or is_player_o(3) and turn_count == 4:
        assigning_x(4)
    elif is_player_o(1) and is_player_o(3) and turn_count == 5:
        if is_not_assigned(6):
            assigning_x(6)
        elif is_not_assigned(4):
            assigning_x(4)
    elif is_player_o(1) and turn_count == 5:
        assigning_x(3)
    elif is_player_o(3) and turn_count == 5:
        assigning_x(1)


# Function to check if a specific position contains 'x'
def is_player_x(num):
    return available_pos[num] == "x"


# Function to check if a specific position contains 'o'
def is_player_o(num):
    return available_pos[num] == "o"


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

    # Update the game's current turn to 'x' (opponent's turn)
    turn = "x"

    # Mark the clicked position as 'o' in the game state
    available_pos[button_id] = "o"

    # Add the button's ID to the list of clicked buttons
    clicked_buttons_id.append(button_id)


# Function to assign 'x' to a button and update game state
def assigning_x(button_id):
    global turn
    global turn_count

    if button_id not in clicked_buttons_id:

        # Increment the turn count to track the progress of the game
        turn_count += 1

        # Load and set the 'x.png' image for the clicked button
        new_image = load_image('images/x.png')
        buttons[button_id-1].config(image=new_image)
        buttons[button_id-1].image = new_image

        # Update the game's current turn to 'o' (opponent's turn)
        turn = "o"

        # Add the button's ID to the list of clicked buttons
        clicked_buttons_id.append(button_id)

        # Mark the clicked position as 'x' in the game state
        available_pos[button_id] = "x"


def begin_game():
    global turn
    global turn_count

    # Load and set the 'x.png' image for the initial move (button 7)
    new_image = load_image('images/x.png')
    buttons[6].config(image=new_image)
    buttons[6].image = new_image

    # Set the initial turn to 'o' (opponent's turn)
    turn = "o"

    # Update the game state to mark the initial move as 'x'
    available_pos[7] = "x"

    # Add the initial move (button 7) to the list of clicked buttons
    clicked_buttons_id.append(7)

    # Increment the turn count to track the game's progress
    turn_count += 1


# Function to reset the game
def restart():
    global turn
    global available_pos
    global turn_count
    global draw
    global countdown_time

    # Reset the turn to the initial player
    turn = "x"

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


# Function to control the countdown timer
def timer():
    global countdown_time

    # Disable the restart button during the countdown
    restart_button.config(state="disabled")

    # Check if there is time remaining
    if countdown_time >= 0:

        # Update the timer label to display the current countdown time
        timer_label.config(text=str(countdown_time))
        countdown_time -= 1
        window.after(1000, timer)

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


# Create the main window
window = Tk()
window.title('Tic Tac Toe')
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

# Create the canvas for the game board
canvas = Canvas(window, width=800, height=800)
card_front = load_image('images/bord.png')
main_image = canvas.create_image(400, 400, image=card_front)
title_text = canvas.create_text(400, 100, text='Tic Tac Toe', font=(FONT_NAME, 35, 'bold'), fill='black')

# Configure the canvas settings
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=3)

# Create a label for the countdown timer
timer_label = Label(window, text="", font=("Helvetica", 48), bg=BACKGROUND_COLOR)
timer_label.place(x=100, y=50)

# Create buttons for the game
empty_box = load_image('images/empty_box.png')

# Create buttons for the Tic Tac Toe grid and set their positions
restart_button = Button(text="Restart", font=(FONT_NAME, 35, 'bold'), highlightthickness=0, command=restart)
restart_button.place(x=255, y=700)

empty_button1 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(1))
empty_button1.place(x=187, y=187)


empty_button2 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(2))
empty_button2.place(x=317, y=187)


empty_button3 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(3))
empty_button3.place(x=447, y=187)


empty_button4 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(4))
empty_button4.place(x=187, y=317)


empty_button5 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(5))
empty_button5.place(x=317, y=317)


empty_button6 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(6))
empty_button6.place(x=447, y=317)


empty_button7 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(7))
empty_button7.place(x=187, y=447)


empty_button8 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(8))
empty_button8.place(x=317, y=447)


empty_button9 = Button(image=empty_box, highlightthickness=0, command=lambda: on_button_click(9))
empty_button9.place(x=447, y=447)

# Store all buttons in a list
buttons = [empty_button1, empty_button2, empty_button3, empty_button4, empty_button5, empty_button6,
           empty_button7, empty_button8, empty_button9]

# Initialize the game and start the main loop
begin_game()
window.mainloop()
