from eckity.creators.creator import Creator
import EssentialClasses


class scheduleCreator(Creator):
    def __init__(self, events=None):
        super().__init__(events)

    def create_individuals(self, n_individuals, higher_is_better=False):
        individuals = []
        for i in range(n_individuals):
            sched = EssentialClasses.Schedule()
            individuals.append(sched.initialize_random())

        return individuals
