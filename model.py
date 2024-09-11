from pyomo.environ import (
    AbstractModel,
    Binary,
    Constraint,
    Expression,
    InequalityExpression,
    Objective,
    minimize,
    NonNegativeReals,
    Param,
    Set,
    Var,
)


def get_abstract_model() -> AbstractModel:
    model = AbstractModel(name='diet')

    # Sets: Indexes for parameters, variables and other sets.
    model.days = Set(
        name='days',
        doc='Days of the diet.',
    )
    model.meals = Set(
        name='meals',
        doc='Meal types that the diet includes per each day.',
    )
    model.dishes = Set(
        name='dishes',
        doc='Dishes names that can be included in the diet.',
    )

    # Parameters: Values that you know prior to solving the problem, and will not change
    # during the execution.
    model.calories_min = Param(
        name='calories_min',
        doc='Minimum number of calories per day [kcal].',
        domain=NonNegativeReals
    )
    model.calories_max = Param(
        name='calories_max',
        doc='Maximum number of calories per day [kcal].',
        domain=NonNegativeReals
    )
    model.protein_min = Param(
        name='protein_min',
        doc='Minimum amount of protein that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.protein_max = Param(
        name='protein_max',
        doc='Maximum amount of protein that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.carbs_min = Param(
        name='carbs_min',
        doc='Minimum amount of carbs that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.carbs_max = Param(
        name='carbs_max',
        doc='Maximum amount of carbs that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.fat_min = Param(
        name='fat_min',
        doc='Minimum amount of fat that a day can contain [g].',
        domain=NonNegativeReals,
    )
    model.fat_max = Param(
        name='fat_max',
        doc='Maximum amount of fat that a day can contain [g].',
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

    model.suitable = Param(
        model.dishes,
        model.meals,
        name='suitable',
        doc='Equals 1 if the dish is suitable for the meal and 0 otherwise.',
        domain=Binary,
    )
    model.calories_dish = Param(
        model.dishes,
        name='calories_dish',
        doc='Calories of each dish [kcal].',
        domain=NonNegativeReals,
    )
    model.protein_dish = Param(
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
    model.cost_dish = Param(
        model.dishes,
        name='cost_dish',
        doc='Cost per serving of the dish [€].',
        domain=NonNegativeReals,
    )

    # Variables: Values defined while solving the problem to get the best solution.
    model.use_dish_meal_day = Var(
        model.dishes,
        model.meals,
        model.days,
        name='use_dish_meal_day',
        doc='Equals 1 if a dish is used in a meal of a day and 0 otherwise.',
        domain=Binary,
    )

    # Constraints: Requirements and forbidden actions to achieve a correct solution.
    model.constraint_minimum_dishes_per_meal = Constraint(
        model.meals,
        model.days,
        name='constraint_minimum_dishes_per_meal',
        doc=constraint_minimum_dishes_per_meal.__doc__,
        rule=constraint_minimum_dishes_per_meal,
    )
    model.constraint_maximum_dishes_per_meal = Constraint(
        model.meals,
        model.days,
        name='constraint_maximum_dishes_per_meal',
        doc=constraint_maximum_dishes_per_meal.__doc__,
        rule=constraint_maximum_dishes_per_meal,
    )
    model.constraint_suit_meal_type = Constraint(
        model.dishes,
        model.meals,
        model.days,
        name='constraint_suit_meal_type',
        doc=constraint_suit_meal_type.__doc__,
        rule=constraint_suit_meal_type,
    )
    model.constraint_vegetarianism = Constraint(
        model.dishes,
        model.meals,
        model.days,
        name='constraint_vegetarianism',
        doc=constraint_vegetarianism.__doc__,
        rule=constraint_vegetarianism,
    )
    model.constraint_veganism = Constraint(
        model.dishes,
        model.meals,
        model.days,
        name='constraint_veganism',
        doc=constraint_veganism.__doc__,
        rule=constraint_veganism,
    )
    model.constraint_minimum_calories_per_day = Constraint(
        model.days,
        name='constraint_minimum_calories_per_day',
        doc=constraint_minimum_calories_per_day.__doc__,
        rule=constraint_minimum_calories_per_day,
    )
    model.constraint_maximum_calories_per_day = Constraint(
        model.days,
        name='constraint_maximum_calories_per_day',
        doc=constraint_maximum_calories_per_day.__doc__,
        rule=constraint_maximum_calories_per_day,
    )
    model.constraint_minimum_protein_per_day = Constraint(
        model.days,
        name='constraint_minimum_protein_per_day',
        doc=constraint_minimum_protein_per_day.__doc__,
        rule=constraint_minimum_protein_per_day,
    )
    model.constraint_maximum_protein_per_day = Constraint(
        model.days,
        name='constraint_maximum_protein_per_day',
        doc=constraint_maximum_protein_per_day.__doc__,
        rule=constraint_maximum_protein_per_day,
    )
    model.constraint_minimum_carbs_per_day = Constraint(
        model.days,
        name='constraint_minimum_carbs_per_day',
        doc=constraint_minimum_carbs_per_day.__doc__,
        rule=constraint_minimum_carbs_per_day,
    )
    model.constraint_maximum_carbs_per_day = Constraint(
        model.days,
        name='constraint_maximum_carbs_per_day',
        doc=constraint_maximum_carbs_per_day.__doc__,
        rule=constraint_maximum_carbs_per_day,
    )
    model.constraint_minimum_fat_per_day = Constraint(
        model.days,
        name='constraint_minimum_fat_per_day',
        doc=constraint_minimum_fat_per_day.__doc__,
        rule=constraint_minimum_fat_per_day,
    )
    model.constraint_maximum_fat_per_day = Constraint(
        model.days,
        name='model.constraint_maximum_fat_per_day',
        doc=constraint_maximum_fat_per_day.__doc__,
        rule=constraint_maximum_fat_per_day,
    )

    # Objective: Function of variables that returns a value to be maximized or minimized.
    model.objective_function = Objective(
        name='objective_function',
        doc='Minimize the total cost of the diet.',
        rule=diet_cost,
        sense=minimize,
    )

    return model


# Constraints definition
def constraint_minimum_dishes_per_meal(
        model: AbstractModel,
        meal,
        day,
) -> InequalityExpression:
    """Each meal has at least 1 dish."""
    dishes_per_meal = _get_num_of_dishes_in_meal(model, meal, day)
    return dishes_per_meal >= 1


def constraint_maximum_dishes_per_meal(
        model: AbstractModel,
        meal,
        day,
) -> InequalityExpression:
    """Each meal has at most 3 dishes."""
    dishes_per_meal = _get_num_of_dishes_in_meal(model, meal, day)
    return dishes_per_meal <= 1


def constraint_suit_meal_type(
        model: AbstractModel,
        dish,
        meal,
        day,
) -> InequalityExpression:
    """Dishes can only be selected for the meal type they are suitable for."""
    return model.use_dish_meal_day[dish, meal, day] <= model.suitable[dish, meal]


def constraint_vegetarianism(
        model: AbstractModel,
        dish,
        meal,
        day,
) -> InequalityExpression:
    """Respect vegetarian diet.

    If the diet is vegetarian, all dishes must be vegetarian. If the diet is not
    vegetarian, dishes can be either vegetarian or not.

    Note
    ----
    It is assumed that all vegan dishes are also vegetarian.
    """
    return (
        model.use_dish_meal_day[dish, meal, day] * (1 - model.vegetarian_dish[dish])
        <= (1 - model.vegetarian)
    )


def constraint_veganism(
        model: AbstractModel,
        dish,
        meal,
        day,
) -> InequalityExpression:
    """Respect vegan diet.

    If the diet is vegan, all dishes must be vegan. If the diet is not vegan, dishes can
    be either vegan or not.
    """
    return (
        model.use_dish_meal_day[dish, meal, day] * (1 - model.vegan_dish[dish])
        <= (1 - model.vegan)
    )


def constraint_minimum_calories_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Calorie count per day is lower bounded."""
    daily_calorie_count = _get_daily_metric_count(model, day, model.calories_dish)
    return daily_calorie_count >= model.calories_min


def constraint_maximum_calories_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Calorie count per day is upper bounded."""
    daily_calorie_count = _get_daily_metric_count(model, day, model.calories_dish)
    return daily_calorie_count <= model.calories_max


def constraint_minimum_protein_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Protein count per day is lower bounded."""
    daily_protein_count = _get_daily_metric_count(model, day, model.protein_dish)
    return daily_protein_count >= model.protein_min


def constraint_maximum_protein_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Protein count per day is upper bounded."""
    daily_protein_count = _get_daily_metric_count(model, day, model.protein_dish)
    return daily_protein_count <= model.protein_max


def constraint_minimum_carbs_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Carbs count per day is lower bounded."""
    daily_carbs_count = _get_daily_metric_count(model, day, model.carbs_dish)
    return daily_carbs_count >= model.carbs_min


def constraint_maximum_carbs_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Carbs count per day is upper bounded."""
    daily_carbs_count = _get_daily_metric_count(model, day, model.carbs_dish)
    return daily_carbs_count <= model.carbs_max


def constraint_minimum_fat_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Fat count per day is lower bounded."""
    daily_fat_count = _get_daily_metric_count(model, day, model.fat_dish)
    return daily_fat_count >= model.fat_min


def constraint_maximum_fat_per_day(
        model: AbstractModel,
        day,
) -> InequalityExpression:
    """Fat count per day is upper bounded."""
    daily_fat_count = _get_daily_metric_count(model, day, model.fat_dish)
    return daily_fat_count <= model.fat_max


# Objective function definition
def diet_cost(model: AbstractModel) -> Expression:
    return sum(
        model.use_dish_meal_day[dish, meal, day] * model.cost_dish[dish]
        for dish in model.dishes
        for meal in model.meals
        for day in model.days
    )


# Private auxiliary util functions
def _get_num_of_dishes_in_meal(model: AbstractModel, meal, day):
    """Returns number of dishes that have been selected for a certain meal of a day."""
    return sum(model.use_dish_meal_day[dish, meal, day] for dish in model.dishes)


def _get_daily_metric_count(model: AbstractModel, day, metric):
    """Return the daily count of a certain metric (calories, protein, carb or fat)."""
    return sum(
        model.use_dish_meal_day[dish, meal, day] * metric[dish]
        for dish in model.dishes
        for meal in model.meals
    )
