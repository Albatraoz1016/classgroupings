# break trouble with shy before trouble with trouble
from .student import Student
# REPORT TYPES:
# 0 = NO PREFERENCE
# 1 = NO T WITH T
# 2 = NO T WITH S
# 3 = NO T WITH T AND NO T WITH S
# 4 = SOC SCALE


class Settings:
    def __init__(self, reportLocation, ers):
        self.errors = ers
        self.roll_call_file_location = reportLocation
        self.desired_num_groups = 0
        self.desired_min = 0
        self.desired_max = 0
        self.actual_num_groups = 0
        self.actual_min = 0
        self.actual_max = 0
        self.report_type = 0
        self.created_students = []
        self.num_t_groups = 0
        self.num_s_groups = 0
        self.max_t_per_group = 0
        self.max_s_per_group = 0
        self.setup()

    def setup(self):
        file_contents = self.read_file()
        temp = file_contents.copy()
        settings = file_contents[:17]
        student_lines = temp[18:]
        self.check_settings(settings)
        self.check_students(student_lines)
        self.calculate_actuals()

    def read_file(self):
        lines = []
        with open(self.roll_call_file_location, "r") as file:
            for line in file:
                line = line.rstrip()
                separatedline = line.split("\t")
                lines.append(separatedline)
        file.close()
        return lines

    def check_settings(self, settings_lines):
        line = settings_lines[0]
        num_grps = line[1]
        line = settings_lines[2]
        min = line[1]
        line = settings_lines[4]
        max = line[1]
        line = settings_lines[6]
        notwitht = line[1]
        line = settings_lines[7]
        notwiths = line[1]
        line = settings_lines[9]
        socscale = line[1]

        if not num_grps.isdigit() or not min.isdigit() or not max.isdigit():
            self.errors.add_current_error(101)
            return
        count = 0
        if num_grps.isdigit():
            num_grps = int(num_grps)
            if num_grps > 0:
                count = count + 1
        if min.isdigit():
            min = int(min)
            if min > 0:
                count = count + 1
        if max.isdigit():
            max = int(max)
            if max > 0:
                count = count + 1
        if count > 1:
            self.errors.add_current_error(102)
            return
        elif count == 0:
            self.errors.add_current_error(103)
            return
        elif count == 1:
            self.desired_num_groups = num_grps
            self.desired_min = min
            self.desired_max = max
        if notwitht == "YES" or notwitht == "yes" or notwitht == "Yes":
            notwitht = True
        elif notwitht == "NO" or notwitht == "no" or notwitht == "No":
            notwitht = False
        else:
            self.errors.add_current_error(104)
            return
        if notwiths == "YES" or notwiths == "yes" or notwiths == "Yes":
            notwiths = True
        elif notwiths == "NO" or notwiths == "no" or notwiths == "No":
            notwiths = False
        else:
            self.errors.add_current_error(105)
            return
        if socscale == "YES" or socscale == "Yes" or socscale == "yes":
            socscale = True
        elif socscale == "NO" or socscale == "no" or socscale == "No":
            socscale = False
        else:
            self.errors.add_current_error(106)
            return
        if notwitht or notwiths:
            if socscale:
                self.errors.add_current_error(107)
                return
            elif notwitht:
                if notwiths:
                    self.report_type = 3
                else:
                    self.report_type = 1
            elif notwiths:
                self.report_type = 2
        elif socscale:
            self.report_type = 4
        else:
            self.report_type = 0


    def check_students(self, students_lines):
        for item in students_lines:
            if item[0] == 'X' or item[0] == 'x':
                pass
            else:
                if item[2].isdigit():
                    kid = Student(item[1], int(item[2]))
                    self.created_students.append(kid)
                else:
                    self.errors.add_current_error(108)
                    return

    def get_num_students(self):
        return len(self.created_students)

    def get_num_trouble(self):
        count = 0
        for kid in self.created_students:
            if kid.sociability == 0:
                count = count + 1
        return count

    def get_num_shy(self):
        count = 0
        for kid in self.created_students:
            if kid.sociability == 1:
                count = count + 1
        return count


    def calculate_actuals(self):
        num_students = len(self.created_students)
        num_trouble = self.get_num_trouble()
        num_shy = self.get_num_shy()

        if self.desired_num_groups > 0:
            self.actual_num_groups = self.desired_num_groups
            self.actual_min = num_students // self.actual_num_groups
            self.actual_max = self.actual_min
            if num_students % self.actual_num_groups != 0:
                self.actual_max = self.actual_min + 1
        elif self.desired_min > 0:
            self.actual_min = self.desired_min
            self.actual_num_groups = num_students // self.actual_min
            self.actual_max = self.actual_min
            if num_students % self.actual_min != 0:
                self.actual_max = self.actual_min + 1
        elif self.desired_max > 0:
            self.actual_max = self.desired_max
            self.actual_num_groups = num_students // self.actual_max
            if num_students % self.actual_max != 0:
                self.actual_num_groups = self.actual_num_groups + 1
                self.actual_min = num_students % self.actual_max
            else:
                self.actual_min = self.actual_max

        if self.report_type == 0:   # no preference
            self.max_s_per_group = self.actual_max
            self.max_t_per_group = self.actual_max
        elif self.report_type == 1: #  no t with t
            self.max_s_per_group = self.actual_max
            if num_trouble <= self.actual_num_groups:
                self.max_t_per_group = 1
            else:
                self.max_t_per_group = num_trouble // self.actual_num_groups
                if num_trouble % self.actual_num_groups != 0:
                    self.max_t_per_group = self.max_t_per_group + 1
        elif self.report_type == 2: # no t with s
            self.num_s_groups = self.actual_num_groups // 2
            self.num_t_groups = self.actual_num_groups - self.num_s_groups
            self.max_s_per_group = self.actual_max
            self.max_t_per_group = self.actual_max
        elif self.report_type == 3: # no t with t and no t with s
            # avoid t with t before avoiding t with s
            if num_shy == 0 and num_trouble <= self.actual_num_groups:
                # S = 0, T <= G
                self.max_t_per_group = 1
                self.max_s_per_group = self.actual_max
                self.num_t_groups = num_trouble
            elif num_shy == 0 and num_trouble > self.actual_num_groups:
                # S = 0, T > G
                self.max_s_per_group = self.actual_max
                self.num_t_groups = self.actual_num_groups
                self.max_t_per_group = -(num_trouble // -self.actual_num_groups)
            elif num_trouble == 0 and num_shy <= self.actual_num_groups:
                # T = 0, S <= G
                self.max_s_per_group = 1
                self.max_t_per_group = self.actual_max
                self.num_s_groups = num_shy
            elif num_trouble == 0 and num_shy > self.actual_num_groups:
                # T = 0, S > G
                self.max_t_per_group = self.actual_max
                self.num_s_groups = self.actual_num_groups
                self.max_s_per_group = -(num_shy // -self.actual_num_groups)
            elif num_trouble + num_shy <= self.actual_num_groups:
                # T + S <= G, T != 0, S != 0
                self.num_t_groups = num_trouble
                self.num_s_groups = num_shy
                self.max_s_per_group = 1
                self.max_t_per_group = 1
            elif num_trouble + num_shy > self.actual_num_groups:
                # T + S > G, T != 0, S != 0
                self.num_s_groups = self.actual_num_groups // 2
                self.num_t_groups = self.actual_num_groups - self.num_s_groups
                if num_shy <= self.num_s_groups:
                    self.max_s_per_group = 1
                else:
                    self.max_s_per_group = -(num_shy // -self.num_s_groups)
                if num_trouble <= self.num_t_groups:
                    self.max_t_per_group = 1
                else:
                    self.max_t_per_group = -(num_trouble // -self.num_t_groups)
        elif self.report_type == 4: # soc scale
            self.max_s_per_group = self.actual_max
            self.max_t_per_group = self.actual_max


    def printable_report_type(self):
        if self.report_type == 0:
            return "NO PREFERENCE"
        elif self.report_type == 1:
            return "Avoid Trouble with Trouble"
        elif self.report_type == 2:
            return "Avoid Trouble with Shy"
        elif self.report_type == 3:
            return "Avoid Trouble with Shy and Trouble with Trouble"
        elif self.report_type == 4:
            return "Based on Social Scale"
        else:
            return "Undetermined Report Type"

