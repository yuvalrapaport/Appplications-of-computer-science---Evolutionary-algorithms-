from random import randrange
import pandas as pd
from eckity.individual import Individual
from eckity.fitness.simple_fitness import SimpleFitness
from prettytable import PrettyTable


class Data:

    excel_file = 'data.xlsx'
    course_sheet = pd.read_excel(excel_file, sheet_name="Courses")
    room_sheet = pd.read_excel(excel_file, sheet_name="Rooms")

    COURSES = []
    ROOMS = []

    for ind, row in course_sheet[0:].iterrows():
        course = []
        course.append(row["name"])
        course.append(row["teachers"].split(', '))
        course.append(row["max_students"])
        course.append(row["windows"])
        COURSES.append(course)

    for ind, row in room_sheet[0:].iterrows():
        room = []
        room.append(row["number"])
        room.append(row["capacity"])
        ROOMS.append(room)

    WINDOWS = []
    for i in range(5):
        for j in range(5):
            time = [i, j]
            WINDOWS.append(time)

    def __init__(self):
        self._rooms = []
        for room in self.ROOMS:
            newRoom = Room(room[0], room[1])
            self._rooms.append(newRoom)

        self._windows = []
        for wind in self.WINDOWS:
            newWind = CourseWindow(wind[0], wind[1])
            self._windows.append(newWind)

        self._courses = []
        for course in self.COURSES:
            winds = course[3]
            while winds > 0:
                newCourse = Course(course[0], course[1], course[2])
                self._courses.append(newCourse)
                winds -= 1

    def get_courses(self):
        return self._courses

    def get_rooms(self):
        return self._rooms

    def get_windows(self):
        return self._windows


class Course:
    def __init__(self, name, teachers, max_students):
        self._name = name
        self._teachers = teachers
        self._max_students = max_students

    def get_name(self):
        return self._name

    def get_teachers(self):
        return self._teachers

    def get_max_students(self):
        return self._max_students


class CourseWindow:
    def __init__(self, day, time):
        self._day = day
        self._time = time

    def get_day(self):
        return self._day

    def get_time(self):
        return self._time

    def __str__(self) -> str:
        time = ""
        if self._day == 0:
            time += "SUN "
        elif self._day == 1:
            time += "MON "
        elif self._day == 2:
            time += "TUE "
        elif self._day == 3:
            time += "WED "
        else:
            time += "THU "

        if self._time == 0:
            time += "08-10"
        elif self._time == 1:
            time += "10-12"
        elif self._time == 2:
            time += "12-14"
        elif self._time == 3:
            time += "14-16"
        else:
            time += "16-18"

        return time


class Room:
    def __init__(self, number, capacity):
        self._number = number
        self._capacity = capacity

    def get_number(self):
        return self._number

    def get_capacity(self):
        return self._capacity


class Lecture:
    def __init__(self, course):
        self._course: Course = course

    def __str__(self) -> str:
        return str([self._course.get_name(), self._teacher, str(self._window), "room: " + str(self._room.get_number())])

    def get_lect_as_list(self):
        return [self._course.get_name(), self._teacher, str(self._window), str(self._room.get_number())]

    def get_course(self):
        return self._course

    def set_teacher(self, teacher):
        self._teacher = teacher

    def set_window(self, window):
        self._window: CourseWindow = window

    def set_room(self, room):
        self._room: Room = room

    def get_course(self):
        return self._course

    def get_teacher(self):
        return self._teacher

    def get_window(self):
        return self._window

    def get_room(self):
        return self._room


class Schedule(Individual):
    def __init__(self):
        super().__init__(SimpleFitness())
        self._lectures = []
        self._bug_list = []

    def initialize_random(self):
        courses = data.get_courses()
        rooms = data.get_rooms()
        windows = data.get_windows()
        for i in range(len(courses)):
            course: Course = courses[i]
            teachers = course.get_teachers()
            lecture = Lecture(course)
            lecture.set_teacher(teachers[randrange(len(teachers))])
            lecture.set_room(rooms[randrange(len(rooms))])
            lecture.set_window(windows[randrange(len(windows))])
            self._lectures.append(lecture)
        return self

    def __str__(self) -> str:
        res = []
        for lect in self._lectures:
            res.append(str(lect))
        return res

    def get_lectures(self):
        return self._lectures

    def show(self):
        res = PrettyTable()
        bugs = PrettyTable()
        res.field_names = ["Course Name", "Teacher", "Time", "Room"]
        bugs.field_names = ["Lecture", "Bug"]
        for lect in self._lectures:
            res.add_row(lect.get_lect_as_list())

        for bug in self._bug_list:
            bugs.add_row(bug)

        print(res, "\nbugs:\n", bugs, "\nBest Fitness:")

    def size(self):
        return len(self._lectures)

    def execute(self, *args, **kwargs):
        return self._lectures

    def set_bug_list(self, bugs):
        self._bug_list = bugs


global data
data = Data()
