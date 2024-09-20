# Diet problem

The diet problem is a classic example of a linear programming problem that aims to 
determine the optimal quantities of different foods to include in a diet, minimizing the 
total cost while satisfying the required nutritional needs.

In this version of the diet problem, we consider a diet plan spanning multiple days, 
where each day consists of different meals (e.g. breakfast, lunch, dinner). Each meal 
includes a selection of dishes, and each dish is characterized by certain nutritional 
attributes, such as the amount of protein, carbohydrates and fats. Additionally, each 
dish has properties that indicate whether it is vegetarian or vegan, and its associated 
cost.

The goal of the problem is to find a combination of dishes for each mean and each day 
that minimizes the total cost, meets the daily nutritional requirements and adheres to 
the vegetarian or vegan dietary restrictions.

Find [here](modeling.pdf) the model expressed mathematically.

## Installation

- Base enviornment: You should have installed Python and pip.
- Miniconda (or Conda): It provides the most straightforward installation of the solver, already compiled. Check out [this](https://conda.io/projects/conda/en/latest/user-guide/install/index.html#term-Miniconda) page.


## Development tools

- Type checking with flake8:
```bash
$ flake8 --max-line-length=89
```

## Running
```bash
$ python main.py
```

## Code structure
- `main.py`: Main execution file. It orchestrates the execution.
- `model.py`: Model definition and construction.
- `solver.py`: Defines the solver and its functions.
- `concrete_model_dump.txt`: Internal structure of the model (for debugging)
- `conda-env.yml`: Environment for Conda/Miniconda.
- `requirements.txt`: Requirements of the project.

## Attributions
- Definition of the diet problem extracted from [here](https://ampl.com/colab/notebooks/diet-lecture.html).
