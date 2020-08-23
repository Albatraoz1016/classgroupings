import random
from .group import Group


class Classroom:
    def __init__(self, kids, stngs):
        self.students = kids.copy()
        self.settings = stngs
        self.groups = []
        self.randomized_student_list = []
        self.closed_groups = []
        self.zero = []
        self.one = []
        self.two = []
        self.three = []
        self.four = []
        self.five = []
        self.setup()

    def setup(self):
        counter = 0
        while counter < self.settings.actual_num_groups:
            counter = counter + 1
            grp = Group(self.settings.actual_max, self.settings.actual_min)
            self.groups.append(grp)
        if self.settings.num_t_groups > 0:
            counter = 0
            while counter < self.settings.num_t_groups:
                counter = counter + 1
                grp = self.groups.pop(0)
                grp.set_trouble_only(self.settings.max_t_per_group)
                self.groups.append(grp)
        if self.settings.num_s_groups > 0:
            counter = 0
            while counter < self.settings.num_s_groups:
                grp = self.groups.pop(0)
                if grp.is_trouble_only:
                    self.groups.append(grp)
                else:
                    counter = counter + 1
                    grp.set_shy_only(self.settings.max_s_per_group)
                    self.groups.append(grp)
        self.randomize()
        if self.settings.report_type == 4:
            self.divide_by_rating()
            self.soc_scale_assigning()
        else:
            self.assign_students()

    def divide_by_rating(self):
        for kid in self.students:
            if kid.sociability == 0:
                self.zero.append(kid)
            elif kid.sociability == 1:
                self.one.append(kid)
            elif kid.sociability == 2:
                self.two.append(kid)
            elif kid.sociability == 3:
                self.three.append(kid)
            elif kid.sociability == 4:
                self.four.append(kid)
            elif kid.sociability == 5:
                self.five.append(kid)
        random.shuffle(self.zero)
        random.shuffle(self.one)
        random.shuffle(self.two)
        random.shuffle(self.three)
        random.shuffle(self.four)
        random.shuffle(self.five)

    def randomize(self):
        self.randomized_student_list = self.students.copy()
        random.shuffle(self.randomized_student_list)

    def assign_students(self):
        while len(self.randomized_student_list) > 0:
            added = False
            kid = self.get_rand_student()
            while not added:
                grp = self.groups.pop(0)
                if not grp.closed and grp.check_if_need_to_close():
                    grp.mark_closed()
                    self.closed_groups.append(grp)
                else:
                    if grp.check_if_addable(kid):
                        if grp.add_student(kid):
                            kid.mark_assigned()
                            added = True
                        else:
                            print("Add problem")
                        if not grp.closed and grp.check_if_need_to_close():
                            grp.mark_closed()
                            self.closed_groups.append(grp)
                        else:
                            self.groups.append(grp)
                    else:
                        self.groups.append(grp)
        for item in self.groups:
            item.mark_closed()
            self.closed_groups.append(item)

    def get_rand_student(self):
        if len(self.randomized_student_list) > 0:
            return self.randomized_student_list.pop(0)
        return None

    def soc_scale_assigning(self):
        for grp in self.groups:
            counter = 0
            while grp.get_current_size() < grp.max_size:
                if counter == 0:
                    if len(self.zero) > 0:
                        kid = self.zero.pop(0)
                        grp.direct_add(kid)
                       # print("Added " + kid.name)
                elif counter == 1:
                    if len(self.one) > 0:
                        kid = self.one.pop(0)
                        grp.direct_add(kid)
                        #print("Added " + kid.name)
                elif counter == 2:
                    if len(self.two) > 0:
                        kid = self.two.pop(0)
                        grp.direct_add(kid)
                        #print("Added " + kid.name)
                elif counter == 3:
                    if len(self.three) > 0:
                        kid = self.three.pop(0)
                        grp.direct_add(kid)
                        #print("Added " + kid.name)
                elif counter == 4:
                    if len(self.four) > 0:
                        kid = self.four.pop(0)
                        grp.direct_add(kid)
                        #print("Added " + kid.name)
                elif counter == 5:
                    if len(self.five) > 0:
                        kid = self.five.pop(0)
                        grp.direct_add(kid)
                        #print("Added " + kid.name)
                elif counter == 6:
                    counter = -1
                counter = counter + 1
                if len(self.zero) == 0 and len(self.one) == 0 and len(self.two) == 0 and len(self.three) == 0 and len(self.four) == 0 and len(self.five) == 0:
                        break
        for item in self.groups:
            item.mark_closed()
            self.closed_groups.append(item)
        kids_to_redistribute = []
        finalized_groups = []
        for g in self.closed_groups:
            if g.get_current_size() < g.min_size and self.settings.desired_min > 0:
                for kid in g.students:
                    kids_to_redistribute.append(kid)
            else:
                finalized_groups.append(g)
        change_closed_groups = False
        while len(kids_to_redistribute) > 0:
            print("Entered")
            change_closed_groups = True
            grp = finalized_groups.pop(0)
            kid = kids_to_redistribute.pop(0)
            if grp.check_if_addable_without_checking_max(kid):
                grp.direct_add(kid)
            else:
                kids_to_redistribute.append(kid)
            finalized_groups.append(grp)
        if change_closed_groups:
            self.closed_groups = finalized_groups.copy()


