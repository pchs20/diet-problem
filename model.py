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

from constants import (
    CALORIES_DISH,
    CALORIES_MAX,
    CALORIES_MIN,
    CARBS_DISH,
    CARBS_MAX,
    CARBS_MIN,
    CONSTRAINT_MAXIMUM_CALORIES_PER_DAY,
    CONSTRAINT_MAXIMUM_CARBS_PER_DAY,
    CONSTRAINT_MAXIMUM_DISHES_PER_MEAL,
    CONSTRAINT_MAXIMUM_FAT_PER_DAY,
    CONSTRAINT_MAXIMUM_PROTEIN_PER_DAY,
    CONSTRAINT_MINIMUM_CALORIES_PER_DAY,
    CONSTRAINT_MINIMUM_CARBS_PER_DAY,
    CONSTRAINT_MINIMUM_DISHES_PER_MEAL,
    CONSTRAINT_MINIMUM_FAT_PER_DAY,
    CONSTRAINT_MINIMUM_PROTEIN_PER_DAY,
    CONSTRAINT_SUIT_MEAL_TYPE,
    CONSTRAINT_VEGETARIANISM,
    CONSTRAINT_VEGANISM,
    COST_DISH,
    DAYS,
    DIET,
    DISHES,
    FAT_DISH,
    FAT_MAX,
    FAT_MIN,
    MEALS,
    OBJECTIVE_FUNCTION,
    PROTEIN_DISH,
    PROTEIN_MAX,
    PROTEIN_MIN,
    SUITABLE,
    USE_DISH_MEAL_DAY,
    VEGAN,
    VEGAN_DISH,
    VEGETARIAN,
    VEGETARIAN_DISH
)


def get_abstract_model() -> AbstractModel:
    model = AbstractModel(name=DIET)

    # Sets: Indexes for parameters, variables and other sets.
    model.days = Set(
        name=DAYS,
        doc='Days of the diet.',
    )
    model.meals = Set(
        name=MEALS,
        doc='Meal types that the diet includes per each day.',
    )
    model.dishes = Set(
        name=DISHES,
        doc='Dishes names that can be included in the diet.',
    )

    # Parameters: Values that you know prior to solving the problem, and will not change
    # during the execution.
    model.calories_min = Param(
        name=CALORIES_MIN,
        doc='Minimum number of calories per day [kcal].',
        domain=NonNegativeReals
    )
    model.calories_max = Param(
        name=CALORIES_MAX,
        doc='Maximum number of calories per day [kcal].',
        domain=NonNegativeReals
    )
    model.protein_min = Param(
        name=PROTEIN_MIN,
        doc='Minimum amount of protein that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.protein_max = Param(
        name=PROTEIN_MAX,
        doc='Maximum amount of protein that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.carbs_min = Param(
        name=CARBS_MIN,
        doc='Minimum amount of carbs that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.carbs_max = Param(
        name=CARBS_MAX,
        doc='Maximum amount of carbs that a day can contain [g].',
        domain=NonNegativeReals
    )
    model.fat_min = Param(
        name=FAT_MIN,
        doc='Minimum amount of fat that a day can contain [g].',
        domain=NonNegativeReals,
    )
    model.fat_max = Param(
        name=FAT_MAX,
        doc='Maximum amount of fat that a day can contain [g].',
        domain=NonNegativeReals,
    )
    model.vegetarian = Param(
        name=VEGETARIAN,
        doc='Equals 1 if the diet is vegetarian and 0 otherwise.',
        domain=Binary,
    )
    model.vegan = Param(
        name=VEGAN,
        doc='Equals 1 if the diet is vegan and 0 otherwise.',
        domain=Binary,
    )

    model.suitable = Param(
        model.dishes,
        model.meals,
        name=SUITABLE,
        doc='Equals 1 if the dish is suitable for the meal and 0 otherwise.',
        domain=Binary,
    )
    model.calories_dish = Param(
        model.dishes,
        name=CALORIES_DISH,
        doc='Calories of each dish [kcal].',
        domain=NonNegativeReals,
    )
    model.protein_dish = Param(
        model.dishes,
        name=PROTEIN_DISH,
        doc='Protein that each dish contains [g].',
        domain=NonNegativeReals,
    )
    model.carbs_dish = Param(
        model.dishes,
        name=CARBS_DISH,
        doc='Carbs that each dish contains [g].',
        domain=NonNegativeReals,
    )
    model.fat_dish = Param(
        model.dishes,
        name=FAT_DISH,
        doc='Fat that each dish contains [g].',
        domain=NonNegativeReals,
    )
    model.vegetarian_dish = Param(
        model.dishes,
        name=VEGETARIAN_DISH,
        doc='Equals 1 if the dish is vegetarian and 0 otherwise.',
        domain=Binary,
    )
    model.vegan_dish = Param(
        model.dishes,
        name=VEGAN_DISH,
        doc='Equals 1 if the dish is vegan and 0 otherwise.',
        domain=Binary,
    )
    model.cost_dish = Param(
        model.dishes,
        name=COST_DISH,
        doc='Cost per serving of the dish [€].',
        domain=NonNegativeReals,
    )

    # Variables: Values defined while solving the problem to get the best solution.
    model.use_dish_meal_day = Var(
        model.dishes,
        model.meals,
        model.days,
        name=USE_DISH_MEAL_DAY,
        doc='Equals 1 if a dish is used in a meal of a day and 0 otherwise.',
        domain=Binary,
    )

    # Constraints: Requirements and forbidden actions to achieve a correct solution.
    model.constraint_minimum_dishes_per_meal = Constraint(
        model.meals,
        model.days,
        name=CONSTRAINT_MINIMUM_DISHES_PER_MEAL,
        doc=constraint_minimum_dishes_per_meal.__doc__,
        rule=constraint_minimum_dishes_per_meal,
    )
    model.constraint_maximum_dishes_per_meal = Constraint(
        model.meals,
        model.days,
        name=CONSTRAINT_MAXIMUM_DISHES_PER_MEAL,
        doc=constraint_maximum_dishes_per_meal.__doc__,
        rule=constraint_maximum_dishes_per_meal,
    )
    model.constraint_suit_meal_type = Constraint(
        model.dishes,
        model.meals,
        model.days,
        name=CONSTRAINT_SUIT_MEAL_TYPE,
        doc=constraint_suit_meal_type.__doc__,
        rule=constraint_suit_meal_type,
    )
    model.constraint_vegetarianism = Constraint(
        model.dishes,
        model.meals,
        model.days,
        name=CONSTRAINT_VEGETARIANISM,
        doc=constraint_vegetarianism.__doc__,
        rule=constraint_vegetarianism,
    )
    model.constraint_veganism = Constraint(
        model.dishes,
        model.meals,
        model.days,
        name=CONSTRAINT_VEGANISM,
        doc=constraint_veganism.__doc__,
        rule=constraint_veganism,
    )
    model.constraint_minimum_calories_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MINIMUM_CALORIES_PER_DAY,
        doc=constraint_minimum_calories_per_day.__doc__,
        rule=constraint_minimum_calories_per_day,
    )
    model.constraint_maximum_calories_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MAXIMUM_CALORIES_PER_DAY,
        doc=constraint_maximum_calories_per_day.__doc__,
        rule=constraint_maximum_calories_per_day,
    )
    model.constraint_minimum_protein_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MINIMUM_PROTEIN_PER_DAY,
        doc=constraint_minimum_protein_per_day.__doc__,
        rule=constraint_minimum_protein_per_day,
    )
    model.constraint_maximum_protein_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MAXIMUM_PROTEIN_PER_DAY,
        doc=constraint_maximum_protein_per_day.__doc__,
        rule=constraint_maximum_protein_per_day,
    )
    model.constraint_minimum_carbs_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MINIMUM_CARBS_PER_DAY,
        doc=constraint_minimum_carbs_per_day.__doc__,
        rule=constraint_minimum_carbs_per_day,
    )
    model.constraint_maximum_carbs_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MAXIMUM_CARBS_PER_DAY,
        doc=constraint_maximum_carbs_per_day.__doc__,
        rule=constraint_maximum_carbs_per_day,
    )
    model.constraint_minimum_fat_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MINIMUM_FAT_PER_DAY,
        doc=constraint_minimum_fat_per_day.__doc__,
        rule=constraint_minimum_fat_per_day,
    )
    model.constraint_maximum_fat_per_day = Constraint(
        model.days,
        name=CONSTRAINT_MAXIMUM_FAT_PER_DAY,
        doc=constraint_maximum_fat_per_day.__doc__,
        rule=constraint_maximum_fat_per_day,
    )

    # Objective: Function of variables that returns a value to be maximized or minimized.
    model.OBJECTIVE_FUNCTION = Objective(
        name=OBJECTIVE_FUNCTION,
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
