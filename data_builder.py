from typing import Any, Dict, Optional

from data_converter_pyomo import dishes_to_pyomo_dict
from data_provider import get_dishes_data


def get_problem_data() -> Dict[Optional[str], Any]:
    """Build the problem data, as a pyomo dict."""

    # Dishes data
    dishes_df = get_dishes_data()
    dishes_dict = dishes_to_pyomo_dict(dishes_df)
