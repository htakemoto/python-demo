"""
Sample
Person Class implementation
"""

class Person:
    'Person'

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Hello {name}'.format(name=self.name)
