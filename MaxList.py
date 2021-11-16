class MaxList:
    min_primary = 0
    list = []
    length = 0

    def __init__(self, length):
        self.list = [None] * length
        self.length = length

    def insert(self, plan):
        for i in range(self.length):
            if(self.list[i] == None):
                self.list.insert(i, plan)
                self.list.pop(self.length)
                return

        if plan.score_primary < self.min_primary:
            return

        if ((plan.score_primary > self.list[i].score_primary) or
                (plan.score_primary == self.list[i].score_primary and plan.score_secondary > self.list[i].score_secondary)):
            self.list.insert(i, plan)
            self.list.pop(self.length)
            return
    
    def best(self):
        return self.list[0]