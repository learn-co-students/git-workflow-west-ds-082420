# Quick .py File Example Warmup 

Feel free to do what you need to do for the code challenge (ie, rest), but go through this at some point before you start the project in earnest

![](viz/rest.gif)

## Efficient Data Science Workflows Use Functions in .py Files

In order to avoid the clutter of jupyter notebooks and to aid collaboration, an efficient data science workflow puts most of its work into **functions**.  

These functions are then put inside **.py files** and called to run through whole chunks of processing at a time

We'll run through an example below

### Imports


```python
#run this cell w/o changes

#data manip
import pandas as pd
import numpy as np

#tests
from test_background import pkl_dump, test_obj_dict, run_test_dict, run_test
```

**Load in** fight_songs.csv from the data folder as a dataframe

Notice that the `Year` column has **some weird values** in it, and is an object dtype (specifically, a string)


```python
print(fight_songs.year.value_counts().head())

type(fight_songs['year'][0])
```

    Unknown    5
    1912       4
    1915       4
    1919       3
    1909       3
    Name: year, dtype: int64





    str



Write a quick function to **turn the value `"Unknown"` into `np.nan`**, wherever it appears in the dataframe.  

**Include two parameters** (objects inside the parens of the function that are inputs used inside the function): 
- the dataframe 
- the value being replaced as `np.nan`

(but it's ok to hardcode `np.nan` as what's replacing the value)

*Don't forget the docstring!*

Run it with the correct arguments as inputs and assign it to `fight_songs`


```python
def turn_value_null(#your code here):
    '''
    write a docstring!
    '''
    #your code here 
    #that creates a variable 
    #named `frame`
    
    
    return frame
    
fight_songs = turn_value_null(#your code here)
```

Now, write a function that **removes all the nulls**.

Again, use the dataframe as a parameter to the function 

Run it with the correct arguments as inputs and assign it to `fight_songs`


```python
def drop_nulls(#your code here):
    '''
    write a docstring
    '''
    
    frame = #your code here
    
    return frame

fight_songs = drop_nulls(#your code here)
```

Finally, write a function to **turn the `type` of the `year` column into an `int`**

This time, have the column be a parameter

Call the function and assign it to `fight_songs['year']` (written out for you)


```python
def turn_column_int(#your code here):
    '''
    your docstring here
    '''
    
    column = #your code here
    return column

fight_songs['year'] = turn_column_int(fight_songs['year'])
```


```python
#run this to check you work

run_test(fight_songs, 'fight_songs')
```

Now, write a function that **loads fight_songs.csv** into a dataframe and returns it. *(It doesn't need any parameters!)*


```python
def load_fight_songs():
    
    '''
    write your docstring here
    '''
    
    df = #your code here
    
    return df
```

## Now the fun part:

**Write a function** (which doesn't take in any parameters) that:
- **calls** `load_fight_songs`, `turn_value_null`, `drop_nulls`, and `turn_column_int` **sequentially**
    - (make sure to include all the specific parameters of those functions called above which are necessary to make them run)
    
    
- **returns** a dataframe at the end

It should be ***the same columns, rows and data*** as the dataframe we ended up with above


```python
def load_clean_fight_songs():
    '''
    write your docstring here!
    '''
    
    
    #write your code here
```


```python
#run this cell to test your code!

fight_songs_function_test = load_clean_fight_songs()

run_test(fight_songs_function_test, 'fight_songs')
```

## Now the *really* fun part:


Open a new **text file**, and **save it** as `data_cleaning.py`

**Write out import statements for pandas and numpy**, using the same aliases we always do, in the same manner we always do

**Write out** (in order to get your fingers some muscle memory time) **all five functions** you made above, in the order you made them

At the top of `data_cleaning.py`, **write** (again, don't copy) in triple-quotes (like a docstring) the following:

'''
These functions are used to clean the fight_songs.csv dataset

load_clean_fight_songs can be used without parameters to load the csv into a dataframe, run cleaning functions, and return a clean frame

Individually, they are used to:

\- load_fight_songs: load the csv into a dataframe

\- turn_value_null: change values of "Unknown" into np.nan

\- drop_nulls: drop the rows with np.nan values

\- turn_column_int: change the 'year' column into an int type


\- load_clean_fight_songs calls the above functions sequentially and returns the frame
'''

### Now the ***REALLY*** fun part

Switch .py files with someone from the cohort

***Windows note:*** the path for navigating folders is different in Windows than in Mac, so cross-os switching means altering the path load_fight_songs() uses to load the csv in the .py file. 

Save it in this repo as `testing_data_cleaning.py`

***Restart your kernal***

Run the cell below to test your fellow student's work!


```python
from testing_data_cleaning import load_clean_fight_songs
from test_background import pkl_dump, test_obj_dict, run_test_dict, run_test

test_frame = load_clean_fight_songs()

run_test(test_frame, 'fight_songs')
```

# Why This Matters

The workflow that will make you an efficient data scientist goes something like this:

- **Write preliminary code** in Jupyter Notebooks
- Complete a **small** section of code that you know completes a necessary task
- **Write that code into a function** in a .py file
- In another notebook, **import that function** and run it

#### There are -several- advantages to doing this

- **Jupyter Notebooks are MeSsY**
    - Easy to jump around cells and **lose track** of what you're doing
    - Easy to **change the value of a variable** and not remember it later
    - Not that easy to **combine work**
    
    
- Importing functions through **.py files** into another book **helps mitigate** those problems
    - Your important work is all in **one spot without the clutter** of producing that work
    - Everything's in a tidy package, and so it's **harder for variables to get re-named**
    - **Combining work becomes easier**. Instead of sharing code through Jupyter Notebooks, and having to figure out which cells to run in what order, we can share .py files where we've already put in the work of figuring out what to run in what order as we've been working
    
    
- **Saves time in the long run**
    - Might not seem worth the time investment at first, but as your projects become bigger and more sprawling the problems it helps mitigate will become laRG**ER**
    - Doing this forces a **marathon mentality over a sprint mentality**, and helps keep one focused on small, necessary tasks


![](viz/siren.gif)     ![](viz/siren.gif)
# Is This Required for the Project?
![](viz/siren.gif)     ![](viz/siren.gif)

No


### Should we try it?

Sure!  But if it seems like it's becoming a hinderance to getting stuff done, go ahead and skip it


```python

```
