# GitHub Workflow

Created based on [this repo](https://github.com/learn-co-curriculum/dsc-chi-warmup-py-files) by Ben Oren

## Agenda

1. README edits with basic branching workflow
2. Creating Python modules
3. Bonus: Resolving a merge conflict

Let's say we have a team of 3:

 - Teammate A: project manager
 - Teammate B: working on visualizations
 - Teammate C: working on data cleaning and preparation

## README Edits with Basic Branching Workflow

 - [x] Teammate A: change the README title and add an image from [Unsplash](https://unsplash.com/)
 - [] Teammate B: add a graph to the README under Data Understanding

^ with proper Git workflow, these two things can be done at the same time

## Creating Python Modules

There are two exploratory notebooks, `01_data_cleaning.ipynb` and `02_visualizations.ipynb`. Teammate C made the data cleaning notebook, and Teammate B made the visualizations notebook. Let's extract the code from those into `.py` files in order to make a final presentation notebook

The goal here is to reuse code by importing it rather than copying and pasting it

"Magic incantation":

```python
%load_ext autoreload
%autoreload 2
```

```python
import os
import sys
module_path = os.path.abspath(os.path.join(os.pardir, os.pardir))
if module_path not in sys.path:
    sys.path.append(module_path)
```

 - [] Teammate A: create the `src` module (with a `__init__.py`)

^ this must be done before anyone can add import-able code

 - [] Teammate C: add a file `data_cleaning.py`, containing `load_clean_fight_songs` and all needed dependencies
 - [] Teammate B: add a file `visualizations.py`, containing `plot_highest_from_col`

^ with proper Git workflow, these two things can be done at the same time

 - [] Teammate A: integrate the code from the `src` module into a new `report/final_notebook.ipynb` notebook
    - Include relevant imports
    - Load cleaned data into `df`
    - Make a plot of the top 10 songs by "number_fights"

## Bonus: Resolving a Merge Conflict

This is a tutorial on what *not* to do, then how to resolve it if it happens

 - [] Teammate A: add a markdown cell to the end of the final notebook highlighting the fact that Texas has the highest `number_fights`, and a code cell showing more information about Texas
 - [] Teammate B: add a code cell to the end of the final notebook that plots the top 15 songs by "bpm"

^ this will create a merge conflict when they try to merge, since they have edited the same part of the same file

 - [] Teammate B: resolve the merge conflict, and add their new code below the information about Texas
