from typing import Any, Dict, Optional

from constants import DAYS, MEALS
from data_converter_pyomo import (
    diet_info_to_pyomo_dict,
    dishes_to_pyomo_dict,
    unindexed_component_to_pyomo,
)
from data_provider import (
    get_days_data,
    get_diet_info_data,
    get_dishes_data,
    get_meals_data,
)


def get_problem_data() -> Dict[Optional[str], Any]:
    """Build the problem data, as a pyomo dict."""

    days_list = get_days_data()
    days_dict = unindexed_component_to_pyomo(key=DAYS, to_convert=days_list)

    meals_list = get_meals_data()
    meals_dict = unindexed_component_to_pyomo(key=MEALS, to_convert=meals_list)

    dishes_df = get_dishes_data()
    dishes_dict = dishes_to_pyomo_dict(dishes_df, meals_list)

    diet_info_df = get_diet_info_data()
    diet_info_dict = diet_info_to_pyomo_dict(diet_info_df)

    return {
        **days_dict,
        **meals_dict,
        **dishes_dict,
        **diet_info_dict,
    }
