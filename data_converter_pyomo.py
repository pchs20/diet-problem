import pandas as pd
from typing import Any, Dict, List, Optional

from constants import (
    CALORIES_DISH,
    CARBS_DISH,
    COST_DISH,
    FAT_DISH,
    PROTEIN_DISH,
    SUITABLE,
    SUITABLE_MEAL,
    VEGAN_DISH,
    VEGETARIAN_DISH
)


def dishes_to_pyomo_dict(
        dishes_df: pd.DataFrame,
        meals: List[str]
) -> Dict[Optional[str], Any]:
    """Convert dishes data to a pyomo dict.

    Example of extract of output:
    {
        'calories_dish': {
            'dish_0': 450,
            'dish_1': 300,
        },
        'protein_dish': {
            'dish_0': 35,
            'dish_1': 12,
        },
        'suitable': {
            ('dish_0', 'breakfast'): 0,
            ('dish_0', 'lunch'): 0,
            ('dish_0', 'dinner'): 1,
            ('dish_1', 'breakfast'): 0,
            ('dish_1', 'lunch'): 1,
            ('dish_1', 'dinner'): 0,
        },
        ...
    }
    """
    COMMON_COLUMNS = [
        CALORIES_DISH,
        PROTEIN_DISH,
        CARBS_DISH,
        FAT_DISH,
        VEGETARIAN_DISH,
        VEGAN_DISH,
        COST_DISH,
    ]
    dict_ = {
        param_name: dishes_df[param_name].to_dict() for param_name in COMMON_COLUMNS
    }
    dict_[SUITABLE] = {
        (dish, meal): int(dishes_df.loc[dish, SUITABLE_MEAL] == meal)
        for dish in dishes_df.index for meal in meals
    }
    return dict_
