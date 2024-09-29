from typing import Optional

from pyomo.environ import ConcreteModel, SolverFactory, SolverStatus, value
from pyomo.opt.results import SolverResults


class Solver:
    def __init__(self, concrete_model: ConcreteModel):
        self.concrete_model: ConcreteModel = concrete_model
        self._solution: Optional[SolverResults] = None

    def solve(self) -> None:
        solver = SolverFactory('scip')
        self._solution = solver.solve(self.concrete_model, tee=True)

    def solution_exists(self) -> bool:
        solution_found = (
            self._solution.solver.status == SolverStatus.ok or
            self._solution.solver.status == SolverStatus.warning
        )
        return solution_found

    def print_solution(self) -> None:
        assert self.solution_exists(), 'The solver did not find any solution!'

        print()
        print('Diet cost: ' + str(value(self.concrete_model.objective_function)) + '€')
        print()

        model = self.concrete_model
        for day in model.days:
            print('--------' + day.upper() + '--------')
            calories_day = protein_day = carbs_day = fat_day = 0
            for meal in model.meals:
                print('----' + meal.upper() + '----')
                for dish in model.dishes:
                    if model.use_dish_meal_day[dish, meal, day].value:
                        calories_day += model.calories_dish[dish]
                        protein_day += model.protein_dish[dish]
                        carbs_day += model.carbs_dish[dish]
                        fat_day += model.fat_dish[dish]
                        print(dish)
                print()
            print('----STATS DAY----')
            print('Calories: ' + str(calories_day))
            print('Protein: ' + str(protein_day))
            print('Carbs: ' + str(carbs_day))
            print('Fat: ' + str(fat_day))
            print()
