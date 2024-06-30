from pyomo.environ import (
    AbstractModel,
    Binary,
    Constraint,
    NonNegativeReals,
    Param,
    RangeSet,
    Set,
    Var,
)
from pyomo.core.expr.relational_expr import EqualityExpression, InequalityExpression


def get_abstract_model() -> AbstractModel:
    model = AbstractModel(name='sudoku')

    # Sets: Indexes for parameters, variables and other sets.
    model.days = Set(
        name='days',
        doc='Days of the diet.',
    )
    model.meals = Set(
        name='meals',
        doc='Meal types that the diet includes per each day.',
    )
    # model.meals_day = Set(    # If we wanted to allow the user which meals to include.
    #     model.days,   # Indexed by meals maybe? And then binary?
    #     name='meals_day',
    #     doc='Meals of each day.',
    # )
    model.dishes = Set(
        name='dishes',
        doc='Dishes names that can be included in the diet.',
    )

    # Parameters: Values that you know prior to solving the problem, and will not change
    # during the execution.
    model.cal_min = Param(
        name='calories_min',
        doc='Minimum number of calories of the diet [kcal].',
        domain=NonNegativeReals
    )
    model.cal_max = Param(
        name='calories_max',
        doc='Maximum number of calories of the diet [kcal].',
        domain=NonNegativeReals
    )
    model.prote_min = Param(
        name='protein_min',
        doc='Minimum amount of protein that the diet can contain [g].',
        domain=NonNegativeReals
    )
    model.prote_max = Param(
        name='protein_max',
        doc='Maximum amount of protein that the diet can contain [g].',
        domain=NonNegativeReals
    )
    model.carbs_min = Param(
        name='carbs_min',
        doc='Minimum amount of carbs that the diet can contain [g].',
        domain=NonNegativeReals
    )
    model.carbs_max = Param(
        name='carbs_max',
        doc='Maximum amount of carbs that the diet can contain [g].',
        domain=NonNegativeReals
    )
    model.fat_min = Param(
        name='fat_min',
        doc='Minimum amount of fat that the diet can contain [g].',
        domain=NonNegativeReals,
    )
    model.fat_max = Param(
        name='fat_max',
        doc='Maximum amount of fat that the diet can contain [g].',
        domain=NonNegativeReals,
    )
    model.vegetarian = Param(
        name='vegetarian',
        doc='Equals 1 if the diet is vegetarian and 0 otherwise.',
        domain=Binary,
    )
    model.vegan = Param(
        name='vegan',
        doc='Equals 1 if the diet is vegan and 0 otherwise.',
        domain=Binary,
    )

    model.meal_dish = Param(
        model.dishes,
        name='meal_dish',
        doc='Meal to which each dish is suitable for.',
        domain=model.meals,
    )
    model.cal_dish = Param(
        model.dishes,
        name='calories_dish',
        doc='Calories of each dish [kcal].',
        domain=NonNegativeReals,
    )
    model.prote_dish = Param(
        model.dishes,
        name='protein_dish',
        doc='Protein that each dish contains [g].',
        domain=NonNegativeReals,
    )
    model.carbs_dish = Param(
        model.dishes,
        name='carbs_dish',
        doc='Carbs that each dish contains [g].',
        domain=NonNegativeReals,
    )
    model.fat_dish = Param(
        model.dishes,
        name='fat_dish',
        doc='Fat that each dish contains [g].',
        domain=NonNegativeReals,
    )
    model.vegetarian_dish = Param(
        model.dishes,
        name='vegetarian_dish',
        doc='Equals 1 if the dish is vegetarian and 0 otherwise.',
        domain=Binary,
    )
    model.vegan_dish = Param(
        model.dishes,
        name='vegan_dish',
        doc='Equals 1 if the dish is vegan and 0 otherwise.',
        domain=Binary,
    )

    # Variables: Values defined while solving the problem to get the best solution.
    model.use_dish_meal_day = Var(
        model.meals_day,
        model.dishes,
        name='use_dish_meal_day',
        doc='Binary variable: 1 if dish is used, 0 otherwise.',
        domain=Binary,
    )

    # Constraints: Requirements and forbidden actions to achieve a correct solution.
    model.constraint_dishes_per_meal = Constraint(
        model.meals_day,
        name='dishes_per_meal',
        doc=constraint_dishes_per_meal.__doc__,
        rule=constraint_dishes_per_meal,
    )

    # Objective: Function of variables that returns a value to be maximized or minimized.
    # There is no function to maximize or minimize, as one solution is no “better” than
    # another. Each solution that fulfills all the constraints is equally valid/optimal.
    # model.objective_function = 0

    return model


def _get_num_of_dishes_of_meal(meal: str):
    # ToDo: This is not correct!!!! Meal is not enough, index should be also by day...
    pass


# Constraints definition
def constraint_minimum_dishes_per_meal(
        model: AbstractModel,
        meal: str,
) -> InequalityExpression:
    """Each meal has at least 1 dish."""
    dishes_per_meal = sum(model.use_dish_meal_day[meal, dish] for dish in model.dishes)
    return dishes_per_meal >= 1


def constraint_value_used_once_per_column(
        model: AbstractModel,
        column: str,
        value: str,
) -> EqualityExpression:
    """In a column, each value must be used exactly once."""
    values_per_row = (
        sum(model.place_value_square[row, column, value] for row in model.rows)
    )
    return values_per_row == 1


def constraint_values_used_once_per_subgrid(
        model: AbstractModel,
        row_subgrid: int,
        column_subgrid: int,
        value: int,
) -> EqualityExpression:
    """In a subgrid, each value must be used exactly once."""
    n = model.n.value
    values_per_subgrid = (
        sum(
            model.place_value_square[i, j, value]
            for i in range(row_subgrid * n, (row_subgrid + 1) * n)
            for j in range(column_subgrid * n, (column_subgrid + 1) * n)
        )
    )
    return values_per_subgrid == 1


def constraint_one_value_per_square(
        model: AbstractModel,
        row: int,
        column: int
) -> EqualityExpression:
    """Each square must have exactly one value."""
    values_per_square = (
            sum(
                model.place_value_square[row, column, value]
                for value in model.grid_values
            )
    )
    return values_per_square == 1
