import EssentialClasses
from eckity.genetic_operators.genetic_operator import GeneticOperator
from random import randrange, sample


class scheduleCrossover(GeneticOperator):
    def __init__(self, probability=1, arity=2, k=1, events=None):
        self.individuals = None
        self.applied_individuals = None
        self.k = k
        super().__init__(probability, arity, events)

    def apply(self, individuals: list[EssentialClasses.Schedule]):
        self.points = sorted(sample(range(0, individuals[0].size()), self.k))
        start_index = 0
        self.individuals = individuals

        for i in range(0, len(self.points), 2):
            individuals[0].get_lectures()[start_index:self.points[i]], individuals[1].get_lectures()[start_index:self.points[i]] = individuals[1].get_lectures()[
                start_index:self.points[i]], individuals[0].get_lectures()[start_index:self.points[i]]
            start_index = self.points[i+1] if i+1 < len(self.points) else 0

        if len(self.points) % 2 == 0:
            end_index = individuals[0].size()
            individuals[0].get_lectures()[start_index:end_index], individuals[1].get_lectures()[start_index:end_index] = individuals[1].get_lectures()[
                start_index:end_index], individuals[0].get_lectures()[start_index:end_index]

        self.applied_individuals = individuals
        return individuals
