# main page of Antycaptcha
from locust import HttpLocust, TaskSet

from main_page import MainPageSteps
# exercises
from exercises.exercise1 import Exercise1Steps
from exercises.exercise2 import Exercise2Steps
from exercises.exercise3 import Exercise3Steps
from exercises.exercise4 import Exercise4Steps

import listeners.csv_listener


class LFTaskSet(TaskSet):
    tasks = [MainPageSteps, Exercise1Steps, Exercise2Steps, Exercise3Steps, Exercise4Steps]


class LocustFile(HttpLocust):
    task_set = LFTaskSet
    min_wait = 4000
    max_wait = 4000
