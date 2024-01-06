# CS50p-Final-Project | Little Professor Game

#### Video Demo:  <URL HERE>

![image](https://github.com/Aladin-bit01/CS50p-Final-Project/assets/144846441/5c7d1517-1647-48e6-b94b-ade36ca04e59)


## Real Little Professor:
As you can see in the previous image, this calculator, AKA Little Professor, is one of the coolest educational games that appeared during the late 20th century.
In fact, in 1976, The Little Professor was released by Texas Instruments and was sold for 20 $ a piece. One year later, already one million piece of this game 
had been sold.For more information about this educational tool, press on [Little Professor](https://en.wikipedia.org/wiki/Little_Professor) .

## Code:
For this project, I recreated an online version of the Little Professor using the Pygame library. This library is installable using the following command on the terminal page of your IDE: `pip install pygame` .

### operations.py:
Ultimately, thus file has for goal to return a mathematical equation (Addition, Substraction, Multiplication, Division) that the player of the game will have to solve.
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

The `division` function return back the equation if the modulo of the operation equals zero. If not, it picks randomly an equation from the `Division_Operations` 
folder and returns it. 

  
