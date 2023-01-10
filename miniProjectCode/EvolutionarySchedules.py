from mutateSchedule import mutateSchedule
from scheduleCrossover import scheduleCrossover
from scheduleEvaluator import scheduleEvaluator
from scheduleCreator import scheduleCreator
from eckity.algorithms.simple_evolution import SimpleEvolution
from eckity.subpopulation import Subpopulation
from eckity.genetic_operators.selections.tournament_selection import TournamentSelection
from eckity.breeders.simple_breeder import SimpleBreeder
from eckity.termination_checkers.threshold_from_target_termination_checker import ThresholdFromTargetTerminationChecker
from eckity.statistics.best_average_worst_statistics import BestAverageWorstStatistics

algo = SimpleEvolution(
    Subpopulation(creators=scheduleCreator(),
                  population_size=300,
                  # user-defined fitness evaluation method
                  evaluator=scheduleEvaluator(),
                  # minimization problem, so higher fitness is worse
                  higher_is_better=False,
                  elitism_rate=1/300,
                  # genetic operators sequence to be applied in each generation
                  operators_sequence=[
        scheduleCrossover(probability=0.8, k=1),
        mutateSchedule(probability=0.2)
    ],
        selection_methods=[
        # (selection method, selection probability) tuple
        (TournamentSelection(
            tournament_size=3, higher_is_better=False), 1)
    ]
    ),
    breeder=SimpleBreeder(),
    max_workers=4,
    max_generation=100,
    termination_checker=ThresholdFromTargetTerminationChecker(
        optimal=0, threshold=0.0),
    statistics=BestAverageWorstStatistics()
)

algo.evolve()
