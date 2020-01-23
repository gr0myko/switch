# Switch-case statement in Python 
Implementation of switch-case statement in Python using decorators 

The idea of switch-case statement support was realized without changing the inner structure of Python language, but was based on the functionality of decorators. 

## Switch-case in docstring of function

To use switch-case syntax in Python, place your statement in a docstring of a function. Apply @switch_support decorator from swicth_support.py. 


## Switch-case in exec

Exec function takes string as an argument, it allows you to use switch-case structure as an imput of your exec function. To do this, please apply exec_switch_support decorator from exec_switch.py on your exec fuction.
