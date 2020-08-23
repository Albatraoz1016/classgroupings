class Student:
    def __init__(self, name, rating):
        self.name = name
        self.sociability = int(rating)
        self.assigned = False

    def get_name(self):
        return self.name

    def is_trouble(self):
        if self.sociability == 0:
            return True
        return False

    def is_shy(self):
        if self.sociability == 1:
            return True
        return False

    def mark_assigned(self):
        self.assigned = True

    def get_sociability(self):
        return self.sociability

    def printable(self):
        return str(self.name)

    def printable_with_details(self):
        if self.assigned:
            temp = "PLACED"
        else:
            temp = "UNPLACED"
        result = (str(self.name) + "      [" + str(self.sociability) + "]          " + temp)
        return result
