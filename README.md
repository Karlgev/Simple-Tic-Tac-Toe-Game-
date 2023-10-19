# Tic-Tac-Toe Game with AI

This is a unique implementation of the classic Tic-Tac-Toe game using Python. The main idea behind this project is to create a challenging version of Tic-Tac-Toe where it is impossible for the player to win. 

## Game Overview

- **Game Settings**: The game is played on a canvas with a custom background and font style. Players are represented by 'O', and the AI opponent is 'X'.

- **Game Logic**: The code tracks the status of each position on the game board using a dictionary and handles player clicks, checking for wins, draws, and player strategies.

## Main Concept

The core concept behind this game is to make it impossible for the player to win. The AI always starts the game, and it selects the center position. This means that no matter how you play, you cannot beat the AI. In this implementation, it's not about winning but about the challenge of attempting to achieve a draw. 

In the future, the project aims to expand the concept to create larger game boards, such as a 9x9 grid, where the AI remains unbeatable. 

## Features

**AI Opponent**: The AI opponent always starts first in the bottom left corner. The player takes turns to click on empty positions to place their 'O'.

- **Win Detection**: The code checks for win conditions by analyzing the game state, and it disables further moves upon a win.

- **Draw Handling**: In case of a draw, the game automatically restarts.

- **Restart Button**: Players can manually restart the game using a "Restart" button.

- **Automatic Restart**: The game also automatically restarts after a brief countdown timer.

- **Image Loading**: Images for 'X', 'O', and game elements are loaded dynamically.

- **Error Handling**: The code handles image loading errors.

- **Code Comments**: The code is well-documented with comments explaining logic and functionality.

## How to Play

1. The AI opponent ('X') will make the first move in the bottom left corner.

2. Click on an empty position to place your 'O'.

3. The game will check for wins or draws after each move.

4. Enjoy the game!

## Future Development

In future iterations, the project aims to expand the game to feature larger game boards that remain unbeatable for the player. The ultimate challenge will be to achieve a draw on these larger boards, which presents a unique and intriguing problem.

## Prerequisites

- Python 3
- Tkinter library (usually included with Python)

## Usage

1. Clone the repository:

2. Run the game:

3. Play and have fun! Your goal is to either beat the AI or achieve a draw.

Enjoy the game! 
