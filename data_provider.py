import json
import pandas as pd

from typing import List

from constants import (
    CALORIES_DISH,
    CALORIES_MAX,
    CALORIES_MIN,
    CARBS_DISH,
    CARBS_MAX,
    CARBS_MIN,
    COST_DISH,
    FAT_DISH,
    FAT_MAX,
    FAT_MIN,
    PROTEIN_DISH,
    PROTEIN_MAX,
    PROTEIN_MIN,
    SUITABLE_MEAL,
    VEGAN,
    VEGAN_DISH,
    VEGETARIAN,
    VEGETARIAN_DISH,
)


def get_days_data() -> List[str]:
    """Get a list with the string that represents each day of the diet."""
    return ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def get_meals_data() -> List[str]:
    """Get a list for the different meals to be included in each day of the diet."""
    return ['breakfast', 'lunch', 'dinner']


def get_dishes_data() -> pd.DataFrame:
    """Get dishes data.

    The return data is structured as a dataframe, where the index is the name of the
    dish and each column represents information about the dish.

    Example of extract of output
                    calories_dish  suitable_meal  protein_dish  ...
    name
    Dish1           250            Lunch          15            ...
    Dish2           400            Dinner         25            ...
    """
    dishes_df = _read_dishes_data()
    dishes_df.set_index('name', inplace=True)
    dishes_df.rename(columns={
        'calories': CALORIES_DISH,
        'meal': SUITABLE_MEAL,
        'protein': PROTEIN_DISH,
        'carbs': CARBS_DISH,
        'fat': FAT_DISH,
        'vegetarian': VEGETARIAN_DISH,
        'vegan': VEGAN_DISH,
        'cost': COST_DISH,
    }, inplace=True)
    # dishes_df[VEGETARIAN_DISH] = dishes_df[VEGETARIAN_DISH].astype(int)
    # dishes_df[VEGAN_DISH] = dishes_df[VEGAN_DISH].astype(int)
    return dishes_df


def _read_dishes_data() -> pd.DataFrame:
    with open('dishes_db.json', 'r') as file:
        data = json.load(file)
    dishes_df = pd.DataFrame(data)
    return dishes_df


def get_diet_info_data() -> pd.DataFrame:
    """Get diet information data.

    The return data is structured as a dataframe with only one row and where each column
    represents information about the diet.

    Example of extract of output
    calories_min   calories_max   protein_min  ...
    250            500            100          ...
    """
    diet_information = {
        CALORIES_MIN: 100,
        CALORIES_MAX: 150,
        PROTEIN_MIN: 40,
        PROTEIN_MAX: 100,
        CARBS_MIN: 10,
        CARBS_MAX: 400,
        FAT_MIN: 10,
        FAT_MAX: 400,
        VEGETARIAN: 0,
        VEGAN: 0,
    }
    return pd.DataFrame.from_dict([diet_information])
