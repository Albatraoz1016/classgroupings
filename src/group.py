class Group:
    def __init__(self, maxSize, minSize):
        self.students = []
        self.closed = False
        self.max_size = maxSize
        self.min_size = minSize
        self.max_trouble = maxSize
        self.max_shy = maxSize
        self.is_trouble_only = False
        self.is_shy_only = False

    def is_closed(self):
        return self.closed

    def mark_closed(self):
        self.closed = True

    def get_current_size(self):
        return len(self.students)

    def get_current_num_trouble(self):
        count = 0
        for kid in self.students:
            if kid.sociability == 0:
                count = count + 1
        return count

    def get_current_num_shy(self):
        count = 0
        for kid in self.students:
            if kid.sociability == 1:
                count = count + 1
        return count

    def check_if_addable(self, kid):
        t = False
        s = False
        if kid.sociability == 0:
            t = True
        if kid.sociability == 1:
            s = True
        if not self.closed:
            if self.get_current_size() < self.max_size:
                if t:
                    if self.get_current_num_trouble() < self.max_trouble:
                        if not self.is_shy_only:
                            return True
                elif s:
                    if self.get_current_num_shy() < self.max_shy:
                        if not self.is_trouble_only:
                            return True
                else:
                    if self.is_shy_only or self.is_trouble_only:
                        rem = self.get_non_t_or_s_spots_open()
                        if rem != None:
                            if rem > 0:
                                return True
                            elif rem == 0:
                                return False
                    else:
                        return True
        return False

    def check_if_addable_without_checking_max(self, kid):
        t = False
        s = False
        if kid.sociability == 0:
            t = True
        if kid.sociability == 1:
            s = True
        if t:
            if self.get_current_num_trouble() < self.max_trouble:
                if not self.is_shy_only:
                    return True
        elif s:
            if self.get_current_num_shy() < self.max_shy:
                if not self.is_trouble_only:
                    return True
        else:
            return True
        return False


    def add_student(self, kid):
        if self.check_if_addable(kid):
            self.students.append(kid)
            return True
        return False

    def direct_add(self, kid):
        self.students.append(kid)

    def check_if_need_to_close(self):
        if self.get_current_size() >= self.max_size:
            self.mark_closed()
            return True
        return False

    def set_trouble_only(self, max):
        self.is_trouble_only = True
        self.max_trouble = max
        self.max_shy = 0

    def set_shy_only(self, max):
        self.is_shy_only = True
        self.max_trouble = 0
        self.max_shy = max

    def get_non_t_or_s_spots_open(self):
        s = self.get_current_num_shy()
        t = self.get_current_num_trouble()
        if self.is_trouble_only:
            num_non_t_students_added = len(self.students) - t
            num_non_t_slots = self.max_size - self.max_trouble
            remaining = num_non_t_slots - num_non_t_students_added
            return remaining
        elif self.is_shy_only:
            num_non_s_students_added = len(self.students) - s
            num_non_s_slots = self.max_size - self.max_shy
            remaining = num_non_s_slots - num_non_s_students_added
            return remaining

    def get_rating_sum(self):
        sum = 0
        for kid in self.students:
            sum = sum + kid.sociability
        return sum
