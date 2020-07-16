class Addition:
    def __init__(self,page):


    def __add__(self, other):
        return (self.page+other)


    def __sub__(self, other):
        return (self.page-other)


ob=Addition()
