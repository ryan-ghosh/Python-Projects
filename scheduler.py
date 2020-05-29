

class Node:
    def __init__(self, date:int, schedule:dict):
        self.date = date
        self.schedule = schedule

    def add_task(self, time:int, task:str):
        self.schedule[time] = task
    
    def print_task(self, time:int):
        print(self.schedule[time])
    
    def print_schedule(self):
        for i in self.schedule:
            print("{}:".format(i), self.schedule[i])

class Queue:
    def __init__(self, list: list, capacity: int):
        self.list = list
        self.capacity = capacity

    def isEmpty(self):
        if self.list == []:
            return True
        return False

    def isFull(self):
        length = len(self.list)
        if length == self.capacity:
            return True
        else:
            return False

    def enqueue(self, data):
        if self.isFull():
            print("Max capacity reached")
        else:
            self.list.append(data)

    def dequeue(self):
        if self.isEmpty():
            print("Empty")
        else:
            self.list.pop(0)
    def print_Nodes(self):
        for i in self.list:
            i.print_schedule()

## initializing schedule

sunday = Node(26, {})
sunday.add_task(9, "wake up")
sunday.add_task(9.30, "eat breakfast")
sunday.add_task(10.30, "exercise")
sunday.add_task(13, "scholarships, Corona funding, Wealthsimple")
sunday.print_schedule()

## initialize Queue
days = []



