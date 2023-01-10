from eckity.genetic_operators.genetic_operator import GeneticOperator
import EssentialClasses
from random import uniform


class mutateSchedule(GeneticOperator):
    def __init__(self, probability=1, arity=1, events=None):
        super().__init__(probability, 1, events)

    def apply(self, individuals):
        schedule: EssentialClasses.Schedule = individuals[0]
        newSched = EssentialClasses.Schedule()
        newSched.initialize_random()
        for i in range(0, len(schedule.get_lectures())):
            if uniform(0, 1) <= 0.3:
                schedule.get_lectures()[i] = newSched.get_lectures()[i]

        self.applied_individuals = individuals
        return individuals
