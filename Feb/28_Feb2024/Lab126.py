from abc import ABC, abstractmethod

class ATB(ABC):

    def perform_task1(self):
        pass
    def perform_task2(self):
        pass

class Amit(ATB):
    def perform_task1(self):
        return "done task1"

    def perform_task2(self):
        return "done task2"

amit = Amit()
print(amit.perform_task1())
amit.perform_task2()