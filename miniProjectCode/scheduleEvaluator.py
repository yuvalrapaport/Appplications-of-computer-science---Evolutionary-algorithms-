from eckity.evaluators.simple_individual_evaluator import SimpleIndividualEvaluator
import EssentialClasses


class scheduleEvaluator(SimpleIndividualEvaluator):
    def __init__(self) -> None:
        super().__init__()

    def _evaluate_individual(self, schedule: EssentialClasses.Schedule):
        lectures = schedule.get_lectures()
        teachers_to_time = {}
        room_to_time = {}
        bugs = 0
        bug_list = []

        for lect in lectures:
            course = lect.get_course()
            max = course.get_max_students()
            room = lect.get_room()
            cap = room.get_capacity()
            if max > cap:
                bugs += 1
                bug_list.append([str(lect), "bug: capacity"])

            teacher = lect.get_teacher()
            wind = lect.get_window()

            if teachers_to_time.get(teacher) is not None and (wind.get_day(), wind.get_time()) in teachers_to_time.get(teacher):
                bugs += 1
                bug_list.append([str(lect), "bug: teacher double booked"])
            elif teachers_to_time.get(teacher) is not None:
                teachers_to_time[teacher].append(
                    (wind.get_day(), wind.get_time()))
            else:
                teachers_to_time[teacher] = [(wind.get_day(), wind.get_time())]

            if room_to_time.get(room.get_number()) is not None and (wind.get_day(), wind.get_time()) in room_to_time.get(room.get_number()):
                bugs += 1
                bug_list.append([str(lect), "bug: room double booked"])
            elif room_to_time.get(room.get_number()) is not None:
                room_to_time[room.get_number()].append(
                    (wind.get_day(), wind.get_time()))
            else:
                room_to_time[room.get_number()] = [(
                    wind.get_day(), wind.get_time())]

        schedule.set_bug_list(bug_list)

        return bugs
