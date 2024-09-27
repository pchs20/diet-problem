import pandas as pd
from typing import Any, Dict, List, Optional

from constants import (
    CALORIES_DISH,
    CARBS_DISH,
    COST_DISH,
    DISHES,
    FAT_DISH,
    PROTEIN_DISH,
    SUITABLE,
    SUITABLE_MEAL,
    VEGAN_DISH,
    VEGETARIAN_DISH
)


def unindexed_component_to_pyomo(
        key: str,
        to_convert: List[str],
) -> Dict[Optional[str], Any]:
    return {key: {None: to_convert}}


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
    dishes_names = list(dishes_df.index.values)
    dict_ = unindexed_component_to_pyomo(key=DISHES, to_convert=dishes_names)

    COLUMNS_INDEXED_BY_DISH = [
        CALORIES_DISH,
        PROTEIN_DISH,
        CARBS_DISH,
        FAT_DISH,
        VEGETARIAN_DISH,
        VEGAN_DISH,
        COST_DISH,
    ]
    dict_.update({
        param_name: dishes_df[param_name].to_dict()
        for param_name in COLUMNS_INDEXED_BY_DISH
    })

    # Parameter 'suitable' needs a special treatment.
    dict_[SUITABLE] = {
        (dish, meal): int(dishes_df.loc[dish, SUITABLE_MEAL] == meal)
        for dish in dishes_df.index for meal in meals
    }

    return dict_


def diet_info_to_pyomo_dict(diet_info_df: pd.DataFrame) -> Dict[Optional[str], Any]:
    """Convert diet information to pyomo.

    Example of extract of output:
    {
        'calories_min': {
            None: 250,
        },
        'calories_max': {
            None: 500,
        },
        'protein_min': {
            None: 100,
        },
        ...
    }
    """
    diet_info = diet_info_df.iloc[0]
    dict_ = {key: {None: info} for key, info in diet_info.items()}
    return dict_
