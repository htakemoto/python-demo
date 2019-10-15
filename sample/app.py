"""
Sample
App Class implementation
"""

from random import choice
from sample.person import Person

class App():
    'app'

    def __init__(self):
        'init app'
        print("app.init")

    def run(self):
        'run'
        print("app.Run")
        people = [
            Person('Jane'),
            Person('Jill'),
            Person('Bob')
        ]
        # randomly pick one person
        person = choice(people)
        print(person)
