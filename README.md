# CS50p-Final-Project | Little Professor Game

#### Video Demo:  <URL HERE>

![image](https://github.com/Aladin-bit01/CS50p-Final-Project/assets/144846441/5c7d1517-1647-48e6-b94b-ade36ca04e59)


## Real Little Professor:
As you can see in the previous image, this calculator, AKA Little Professor, is one of the coolest educational games that appeared during the late 20th century.
In fact, in 1976, The Little Professor was released by Texas Instruments and was sold for 20 $ a piece. One year later, already one million piece of this game 
had been sold.For more information about this educational tool, press on [Little Professor](https://en.wikipedia.org/wiki/Little_Professor) .

## Code:
For this project, I recreated an online version of the Little Professor using the Pygame library. This library is installable using the following command on the terminal page of your IDE: `pip install pygame` .

### Assets:
To create the graphical interface of the game multiple assets are used including images, a special font and some audio files. Three folders contain the assets used in this project: **Audio**, **Graphics** and **font**.
### operations.py:
Ultimately, this file has for goal to return a mathematical equation (Addition, Substraction, Multiplication, Division) that the player of the game will have to solve.
Two functions `add_sub_operands` and `mult_div_operands` have for goal to return the two operands that will be displayed in the math equation. Those functions take one argument (The Level chosen by the player from 1 to 3). 

In `add_sub_operands`:
    Level 1: returns two random numbers between 1 and 9
    Level 2: returns two random numbers between 10 and 99
    Level 3: returns two random numbers between 100 and 999
    
In `mult_div_operands`:
    Level 1: returns two random numbers between 1 and 9
    Level 2: returns one random number between 10 and 99 and an other random number between 1 and 9
    Level 3: returns two random numbers between 10 and 99

The `addition`, `substraction` and `multiplication` functions return back an equation using these numbers : X (+|-|x) Y =

The `division` function return back the equation if the modulo of the operation equals zero. If not, it picks randomly an equation from the **Division_Operations**
folder and returns it. 

### classes.py:
In this file, we have three classes: `Operations`, `Levels` and `Display_Operation`. Those classes have for goal to encapsulate the process of creating the buttons and
equations that will be shown on the screen during the game. 

### project.py:
This file is actually the main file of the game. It contains all the logic behind the functioning of this game including mutliple functions, constants, the intializatiion of pygame, the events' loop and the game's loop itself. Let's start by explaining briefly the logic and the goal of each function:

`display_operation`: This function takes a list containing two elements: the level (1,2,3) as well as the operation (+,-,*,/) chosen by the player and calls the proper function from **operations.py** and pass to it the level chosen by the player. It then returns the equation returned by the chosen function from **operations.py** .

`correct_answer`: This function takes two arguments: the mathematicla equation and the answer of the user. It then return after some cleaning and conversions a boolean (True or False) telling if the answer given by the user is actually the right result of the mathematical question. 

`image_surface`: This function encapsulate simply the pygame method `pygame.image.load(image_path)`

`image_rect`: This function takes the surface returned by the `image_surface` function as well as the (x,y) position of the top left point of the surface. It then creates the rectangle of the given surface. 

`phrase_rect`: This function takes as arguments: a string to display on the the display surface, the (x,y) position of the top left point of the surface, the font to write the string with, as well as the color of the string (black:(64,64,64) by default). It then returns a text_surface and a text_rectangle. This function encapsulates the pygame methods, `pygame.font.render()` and `surface.get_rect()`.

`events_loop`: This function handles the userinput (keyboard keys pressed and mouse buttons pressed). It helps as well to make the transition between the different states of the game.

  
