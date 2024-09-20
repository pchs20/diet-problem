import json
import pandas as pd

from constants import (
    CALORIES_DISH,
    CARBS_DISH,
    COST_DISH,
    FAT_DISH,
    PROTEIN_DISH,
    SUITABLE_MEAL,
    VEGAN_DISH,
    VEGETARIAN_DISH
)


def get_dishes_data() -> pd.DataFrame:
    """Get dishes data.

    The return data is structured as a dataframe, where the index is the name of the
    dish and each column represent information about the dish.
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
    })
    dishes_df[VEGETARIAN_DISH] = dishes_df[VEGETARIAN_DISH].astype(int)
    dishes_df[VEGAN_DISH] = dishes_df[VEGAN_DISH].astype(int)
    return dishes_df


def _read_dishes_data() -> pd.DataFrame:
    with open('dishes_db.json', 'r') as file:
        data = json.load(file)
    dishes_df = pd.DataFrame(data)
    return dishes_df
