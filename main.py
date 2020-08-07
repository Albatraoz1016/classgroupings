import random
import subprocess

TEAMS = []
ERRORS = False

def read_in_teams():
    global TEAMS
    file = "/Users/wasecahodson/Desktop/classgroupings/teams.txt"
    with open(file, "r") as file:
        for line in file:
            line = line.rstrip()
            TEAMS.append(line)
    file.close()


class Student:
    def __init__(self, name, presence, sociability, gender):
        self.name = name
        self.presence = presence
        self.sociability = sociability
        self.gender = gender


NUM_DESIRED_GROUPS = 0
DESIRED_GROUP_SIZE = 0
MAX_GROUP_SIZE = 0
MIN_GROUP_SIZE = 0
AVOID_TROUBLE_WITH_TROUBLE = True
AVOID_SHY_WITH_TROUBLE = True
USE_SOC_SCALE = True
INCLUDE_ABSENT = False
BALANCE_GENDERS = False

TOTAL_NUM_STUDENTS = 0

#Absent or not
ALL_STUDENTS = []

# Only include students that are to be placed in a group (not absent if not including absents vice versa)
ALL_CONSIDERED_STUDENTS = []

# These contain list of students that are going to be used (so absent
# if including absent, not absent if not including them)
TROUBLE_STUDENTS = []
SHY_STUDENTS = []
FEMALE_STUDENTS = []
MALE_STUDENTS = []
TWO_STUDENTS = []
THREE_STUDENTS = []
FOUR_STUDENTS = []
FIVE_STUDENTS = []
NON_TROUBLE_STUDENTS = []
NON_SHY_STUDENTS = []


GROUPS = []

RANDOMIZED_CONSIDERED_STUDENTS = []
RANDOMIZED_NON_TROUBLE_STUDENTS = []
RANDOMIZED_NON_SHY_STUDENTS =[]
RANDOMIZED_FIVES = []
RANDOMIZED_FOURS = []
RANDOMIZED_THREES = []
RANDOMIZED_TWOS = []
RANDOMIZED_SHY = []
RANDOMIZED_TROUBLE = []


def get_file_location():
    with open("/Users/wasecahodson/Desktop/classgroupings/filelocation.txt", "r") as fff:
        for line in fff:
            filelocation = line
        fff.close()
    return filelocation


def read_file(file):
    fileContents = []
    with open(file, "r") as f:
        for line in f:
            line = line.rstrip()
            separatedline = line.split("\t")
            fileContents.append(separatedline)
        f.close()
    rowOne = fileContents.pop(0)
    rowTwo = fileContents.pop(0)
    rowThree = fileContents.pop(0)
    rowFour = fileContents.pop(0)
    rowFive = fileContents.pop(0)
    rowSix = fileContents.pop(0)
    rowSeven = fileContents.pop(0)
    rowEight = fileContents.pop(0)
    global NUM_DESIRED_GROUPS
    global NUM_DESIRED_GROUPS, DESIRED_GROUP_SIZE, MAX_GROUP_SIZE, MIN_GROUP_SIZE, AVOID_TROUBLE_WITH_TROUBLE
    global AVOID_SHY_WITH_TROUBLE, USE_SOC_SCALE, INCLUDE_ABSENT, BALANCE_GENDERS
    global TOTAL_NUM_STUDENTS, TROUBLE_STUDENTS, SHY_STUDENTS, MALE_STUDENTS, FEMALE_STUDENTS
    global NON_SHY_STUDENTS, NON_TROUBLE_STUDENTS, ALL_CONSIDERED_STUDENTS
    global TWO_STUDENTS, THREE_STUDENTS, FOUR_STUDENTS, FIVE_STUDENTS
    if rowOne[1] != "NA":
        NUM_DESIRED_GROUPS = int(rowOne[1])
    if rowOne[3] == 'Y':
        INCLUDE_ABSENT = True
    if rowThree[1] != 'NA':
        DESIRED_GROUP_SIZE = int(rowThree[1])
    if rowThree[3] == 'N':
        AVOID_TROUBLE_WITH_TROUBLE = False
    if rowFour[1] != 'NA':
        MAX_GROUP_SIZE = int(rowFour[1])
    if rowFour[3] == 'N':
        AVOID_SHY_WITH_TROUBLE = False
    if rowFive[1] != 'NA':
        MIN_GROUP_SIZE = int(rowFive[1])
    if rowFive[3] == 'N':
        USE_SOC_SCALE = False
    if rowSix[3] == 'Y':
        BALANCE_GENDERS = True

    for item in fileContents:
        absent = False
        if item[0] == "X":
            absent = True
        elif item[0] == 'x':
            absent = True
        name = item[1]
        sociability = int(item[2])
        gender = item[3]
        newstudent = Student(name, absent, sociability, gender)
        ALL_STUDENTS.append(newstudent)
        TOTAL_NUM_STUDENTS = TOTAL_NUM_STUDENTS + 1
        include = False
        if INCLUDE_ABSENT:
            include = True
        elif absent == False:
            include = True
        if include:
            ALL_CONSIDERED_STUDENTS.append(newstudent)
            if gender == 'M':
                MALE_STUDENTS.append(newstudent)
            else:
                FEMALE_STUDENTS.append(newstudent)
            if sociability == 0:
                TROUBLE_STUDENTS.append(newstudent)
                NON_SHY_STUDENTS.append(newstudent)
            elif sociability == 1:
                SHY_STUDENTS.append(newstudent)
                NON_TROUBLE_STUDENTS.append(newstudent)
            elif sociability == 2:
                TWO_STUDENTS.append(newstudent)
                NON_SHY_STUDENTS.append(newstudent)
                NON_TROUBLE_STUDENTS.append(newstudent)
            elif sociability == 3:
                THREE_STUDENTS.append(newstudent)
                NON_SHY_STUDENTS.append(newstudent)
                NON_TROUBLE_STUDENTS.append(newstudent)
            elif sociability == 4:
                FOUR_STUDENTS.append(newstudent)
                NON_SHY_STUDENTS.append(newstudent)
                NON_TROUBLE_STUDENTS.append(newstudent)
            elif sociability == 5:
                FIVE_STUDENTS.append(newstudent)
                NON_SHY_STUDENTS.append(newstudent)
                NON_TROUBLE_STUDENTS.append(newstudent)


def randomize():
    global RANDOMIZED_CONSIDERED_STUDENTS, RANDOMIZED_NON_SHY_STUDENTS, RANDOMIZED_NON_TROUBLE_STUDENTS
    global ALL_CONSIDERED_STUDENTS, NON_SHY_STUDENTS, NON_TROUBLE_STUDENTS
    global RANDOMIZED_FIVES, RANDOMIZED_FOURS, RANDOMIZED_THREES, RANDOMIZED_TWOS, RANDOMIZED_SHY, RANDOMIZED_TROUBLE
    RANDOMIZED_CONSIDERED_STUDENTS = ALL_CONSIDERED_STUDENTS.copy()
    RANDOMIZED_NON_SHY_STUDENTS = SHY_STUDENTS.copy()
    RANDOMIZED_NON_TROUBLE_STUDENTS = NON_TROUBLE_STUDENTS.copy()
    RANDOMIZED_FIVES = FIVE_STUDENTS.copy()
    RANDOMIZED_FOURS = FOUR_STUDENTS.copy()
    RANDOMIZED_THREES = THREE_STUDENTS.copy()
    RANDOMIZED_TWOS = TWO_STUDENTS.copy()
    RANDOMIZED_SHY = SHY_STUDENTS.copy()
    RANDOMIZED_TROUBLE = TROUBLE_STUDENTS.copy()
    random.shuffle(RANDOMIZED_CONSIDERED_STUDENTS)
    random.shuffle(RANDOMIZED_NON_SHY_STUDENTS)
    random.shuffle(RANDOMIZED_NON_TROUBLE_STUDENTS)
    random.shuffle(RANDOMIZED_FIVES)
    random.shuffle(RANDOMIZED_FOURS)
    random.shuffle(RANDOMIZED_THREES)
    random.shuffle(RANDOMIZED_TWOS)
    random.shuffle(RANDOMIZED_SHY)
    random.shuffle(RANDOMIZED_TROUBLE)


def group_making_algorithm_chooser():
    global TROUBLE_STUDENTS
    if USE_SOC_SCALE:
        if AVOID_TROUBLE_WITH_TROUBLE:
            if AVOID_SHY_WITH_TROUBLE:
                no_t_with_t_or_s()
            else:
                just_scale()
        else:
            just_scale()
    elif len(TROUBLE_STUDENTS) == 0:
        no_preferences()
    elif AVOID_TROUBLE_WITH_TROUBLE:
        if AVOID_SHY_WITH_TROUBLE:
            no_t_with_t_or_s()
        else:
            no_t_with_t()
    elif AVOID_SHY_WITH_TROUBLE:
        if AVOID_TROUBLE_WITH_TROUBLE:
            no_t_with_t_or_s()
        else:
            no_t_with_s()
    else:
        no_preferences()


def no_preferences():
    global NUM_DESIRED_GROUPS
    global DESIRED_GROUP_SIZE
    global RANDOMIZED_NON_SHY_STUDENTS
    global RANDOMIZED_NON_TROUBLE_STUDENTS
    global RANDOMIZED_CONSIDERED_STUDENTS
    global TROUBLE_STUDENTS
    if NUM_DESIRED_GROUPS != 0 and DESIRED_GROUP_SIZE == 0:
        # HAS DESIRED # OF GROUPS
        counter = 0
        while counter < NUM_DESIRED_GROUPS:
            counter = counter + 1
            group = []
            GROUPS.append(group)
        counter = 0
        while counter < len(ALL_CONSIDERED_STUDENTS):
            grp = GROUPS.pop(0)
            student = RANDOMIZED_CONSIDERED_STUDENTS.pop(0)
            grp.append(student)
            counter = counter + 1
            GROUPS.append(grp)
    elif DESIRED_GROUP_SIZE != 0 and NUM_DESIRED_GROUPS == 0:
        while len(RANDOMIZED_CONSIDERED_STUDENTS) > MIN_GROUP_SIZE:
            grp = RANDOMIZED_CONSIDERED_STUDENTS[:MIN_GROUP_SIZE - 1]
            del RANDOMIZED_CONSIDERED_STUDENTS[:MIN_GROUP_SIZE - 1]
            GROUPS.append(grp)
        while len(RANDOMIZED_CONSIDERED_STUDENTS) > 0:
            grp = GROUPS.pop(0)
            student = RANDOMIZED_CONSIDERED_STUDENTS.pop(0)
            grp.append(student)
            GROUPS.append(grp)


def just_scale():
    global NUM_DESIRED_GROUPS
    global DESIRED_GROUP_SIZE
    global RANDOMIZED_NON_SHY_STUDENTS
    global RANDOMIZED_NON_TROUBLE_STUDENTS
    global RANDOMIZED_CONSIDERED_STUDENTS
    global TROUBLE_STUDENTS
    global RANDOMIZED_FIVES, RANDOMIZED_FOURS, RANDOMIZED_THREES, RANDOMIZED_TWOS, RANDOMIZED_SHY, RANDOMIZED_TROUBLE
    if DESIRED_GROUP_SIZE != 0 and NUM_DESIRED_GROUPS == 0:
        num_of_groups = len(ALL_CONSIDERED_STUDENTS) // MIN_GROUP_SIZE
        counter = 0
        while counter < num_of_groups:
            grp = []
            GROUPS.append(grp)
            counter = counter + 1
    else:
        counter = 0
        while counter < NUM_DESIRED_GROUPS:
            counter = counter + 1
            group = []
            GROUPS.append(group)
    while len(RANDOMIZED_FIVES) > 0:
        student = RANDOMIZED_FIVES.pop(0)
        grp = GROUPS.pop(0)
        grp.append(student)
        GROUPS.append(grp)
    while len(RANDOMIZED_FOURS) > 0:
        student = RANDOMIZED_FOURS.pop(0)
        grp = GROUPS.pop(0)
        grp.append(student)
        GROUPS.append(grp)
    while len(RANDOMIZED_THREES) > 0:
        student = RANDOMIZED_THREES.pop(0)
        grp = GROUPS.pop(0)
        grp.append(student)
        GROUPS.append(grp)
    while len(RANDOMIZED_TWOS) > 0:
        student = RANDOMIZED_TWOS.pop(0)
        grp = GROUPS.pop(0)
        grp.append(student)
        GROUPS.append(grp)
    while len(RANDOMIZED_SHY) > 0:
        student = RANDOMIZED_SHY.pop(0)
        grp = GROUPS.pop(0)
        grp.append(student)
        GROUPS.append(grp)
    while len(RANDOMIZED_TROUBLE) > 0:
        student = RANDOMIZED_TROUBLE.pop(0)
        grp = GROUPS.pop(0)
        grp.append(student)
        GROUPS.append(grp)


def no_t_with_s():
    global NUM_DESIRED_GROUPS
    global DESIRED_GROUP_SIZE
    global RANDOMIZED_NON_SHY_STUDENTS
    global RANDOMIZED_NON_TROUBLE_STUDENTS
    global RANDOMIZED_CONSIDERED_STUDENTS
    global TROUBLE_STUDENTS
    min = 0
    if DESIRED_GROUP_SIZE != 0 and NUM_DESIRED_GROUPS == 0:
        num_of_groups = len(ALL_CONSIDERED_STUDENTS) // MIN_GROUP_SIZE
        counter = 0
        while counter < num_of_groups:
            grp = []
            GROUPS.append(grp)
            counter = counter + 1
    else:
        counter = 0
        while counter < NUM_DESIRED_GROUPS:
            counter = counter + 1
            group = []
            GROUPS.append(group)
        num_of_groups = len(GROUPS)
        min = len(ALL_CONSIDERED_STUDENTS) // num_of_groups

    sum_of_t_and_s = len(SHY_STUDENTS) + len(TROUBLE_STUDENTS)
    t = len(TROUBLE_STUDENTS)
    s = len(SHY_STUDENTS)
    if sum_of_t_and_s <= num_of_groups:
        for grp in GROUPS:
            if len(RANDOMIZED_SHY) > 0:
                student = RANDOMIZED_SHY.pop(0)
            else:
                student = RANDOMIZED_TROUBLE.pop(0)
            grp.append(student)
    else:
        if t > s:
            while len(RANDOMIZED_TROUBLE) > 0:
                student = RANDOMIZED_TROUBLE.pop(0)
                grp = GROUPS.pop(0)
                grp.append(student)
                GROUPS.append(grp)
            while len(RANDOMIZED_SHY) > 0:
                student = RANDOMIZED_SHY.pop(0)
                placed = False
                while not placed:
                    grp = GROUPS.pop(0)
                    no_trouble = True
                    for kid in grp:
                        if kid.sociability == 0:
                            no_trouble = False
                            GROUPS.append(grp)
                    if no_trouble:
                        grp.append(student)
                        placed = True
                        GROUPS.append(grp)
        else:
            while len(RANDOMIZED_SHY) > 0:
                student = RANDOMIZED_SHY.pop(0)
                grp = GROUPS.pop(0)
                grp.append(student)
                GROUPS.append(grp)
            while len(RANDOMIZED_TROUBLE) > 0:
                student = RANDOMIZED_TROUBLE.pop(0)
                placed = False
                while not placed:
                    grp = GROUPS.pop(0)
                    no_shy = True
                    for kid in grp:
                        if kid.sociability == 1:
                            no_shy = False
                            GROUPS.append(grp)
                    if no_shy:
                        grp.append(student)
                        placed = True
                        GROUPS.append(grp)
        while len(RANDOMIZED_FIVES) > 0:
            student = RANDOMIZED_FIVES.pop(0)
            added = False
            counter = 0
            while not added:
                grp = GROUPS.pop(0)
                if min == 0:
                    if len(grp) < MIN_GROUP_SIZE:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                else:
                    if len(grp) < min:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                if counter == len(GROUPS) - 1:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
        while len(RANDOMIZED_FOURS) > 0:
            student = RANDOMIZED_FOURS.pop(0)
            added = False
            counter = 0
            while not added:
                grp = GROUPS.pop(0)
                if min == 0:
                    if len(grp) < MIN_GROUP_SIZE:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                else:
                    if len(grp) < min:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                if counter == len(GROUPS) - 1:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
        while len(RANDOMIZED_THREES) > 0:
            student = RANDOMIZED_THREES.pop(0)
            added = False
            counter = 0
            while not added:
                grp = GROUPS.pop(0)
                if min == 0:
                    if len(grp) < MIN_GROUP_SIZE:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                else:
                    if len(grp) < min:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                if counter == len(GROUPS) - 1:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
        while len(RANDOMIZED_TWOS) > 0:
            student = RANDOMIZED_TWOS.pop(0)
            added = False
            counter = 0
            while not added:
                grp = GROUPS.pop(0)
                if min == 0:
                    if len(grp) < MIN_GROUP_SIZE:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                else:
                    if len(grp) < min:
                        grp.append(student)
                        GROUPS.append(grp)
                        added = True
                    else:
                        GROUPS.append(grp)
                        counter = counter + 1
                if counter == len(GROUPS) - 1:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True


def no_t_with_t_or_s():
    global NUM_DESIRED_GROUPS
    global DESIRED_GROUP_SIZE
    global RANDOMIZED_NON_SHY_STUDENTS
    global RANDOMIZED_NON_TROUBLE_STUDENTS
    global RANDOMIZED_CONSIDERED_STUDENTS
    global TROUBLE_STUDENTS
    min = 0
    if DESIRED_GROUP_SIZE != 0 and NUM_DESIRED_GROUPS == 0:
        num_of_groups = len(ALL_CONSIDERED_STUDENTS) // MIN_GROUP_SIZE
        counter = 0
        while counter < num_of_groups:
            grp = []
            GROUPS.append(grp)
            counter = counter + 1
    else:
        counter = 0
        while counter < NUM_DESIRED_GROUPS:
            counter = counter + 1
            group = []
            GROUPS.append(group)
        num_of_groups = len(GROUPS)
        min = len(ALL_CONSIDERED_STUDENTS) // num_of_groups
    t = len(TROUBLE_STUDENTS)
    s = len(SHY_STUDENTS)
    t_and_s = t + s
    if t_and_s <= len(ALL_CONSIDERED_STUDENTS):
        while len(RANDOMIZED_TROUBLE) > 0:
            student = RANDOMIZED_TROUBLE.pop(0)
            grp = GROUPS.pop(0)
            grp.append(student)
            GROUPS.append(grp)
        while len(RANDOMIZED_SHY) > 0:
            student = RANDOMIZED_SHY.pop(0)
            grp = GROUPS.pop(0)
            grp.append(student)
            GROUPS.append(grp)
    while len(RANDOMIZED_FIVES) > 0:
        student = RANDOMIZED_FIVES.pop(0)
        added = False
        counter = 0
        while not added:
            grp = GROUPS.pop(0)
            if min == 0:
                if len(grp) < MIN_GROUP_SIZE:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            else:
                if len(grp) < min:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            if counter == len(GROUPS) - 1:
                grp.append(student)
                GROUPS.append(grp)
                added = True
    while len(RANDOMIZED_FOURS) > 0:
        student = RANDOMIZED_FOURS.pop(0)
        added = False
        counter = 0
        while not added:
            grp = GROUPS.pop(0)
            if min == 0:
                if len(grp) < MIN_GROUP_SIZE:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            else:
                if len(grp) < min:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            if counter == len(GROUPS) - 1:
                grp.append(student)
                GROUPS.append(grp)
                added = True
    while len(RANDOMIZED_THREES) > 0:
        student = RANDOMIZED_THREES.pop(0)
        added = False
        counter = 0
        while not added:
            grp = GROUPS.pop(0)
            if min == 0:
                if len(grp) < MIN_GROUP_SIZE:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            else:
                if len(grp) < min:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            if counter == len(GROUPS) - 1:
                grp.append(student)
                GROUPS.append(grp)
                added = True
    while len(RANDOMIZED_TWOS) > 0:
        student = RANDOMIZED_TWOS.pop(0)
        added = False
        counter = 0
        while not added:
            grp = GROUPS.pop(0)
            if min == 0:
                if len(grp) < MIN_GROUP_SIZE:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            else:
                if len(grp) < min:
                    grp.append(student)
                    GROUPS.append(grp)
                    added = True
                else:
                    GROUPS.append(grp)
                    counter = counter + 1
            if counter == len(GROUPS) - 1:
                grp.append(student)
                GROUPS.append(grp)
                added = True
    else:
        with open("/Users/wasecahodson/Desktop/classgroupings/ERRORS.txt", "w") as er:
            er.write("You can't select both AVOID TROUBLE WITH SHY - AND - AVOID TROUBLE WITH TROUBLE if the sum of both"
              "TROUBLE AND SHY students is greater than the number of groups that are to be created")
        er.close()
        return


def no_t_with_t():
    global NUM_DESIRED_GROUPS
    global DESIRED_GROUP_SIZE
    global RANDOMIZED_NON_SHY_STUDENTS
    global RANDOMIZED_NON_TROUBLE_STUDENTS
    global RANDOMIZED_CONSIDERED_STUDENTS
    global TROUBLE_STUDENTS
    if NUM_DESIRED_GROUPS != 0 and DESIRED_GROUP_SIZE == 0:
        # HAS DESIRED # OF GROUPS
        counter = 0
        while counter < NUM_DESIRED_GROUPS:
            counter = counter + 1
            group = []
            GROUPS.append(group)
        # Do Ceiling Division of Total Number of students divded by number of trouble students to determine max number of trouble students that will be needed per group
        if len(TROUBLE_STUDENTS) > NUM_DESIRED_GROUPS:
            max_trouble_per_group = -(-int(len(ALL_CONSIDERED_STUDENTS)) // int(len(TROUBLE_STUDENTS)))
        else:
            max_trouble_per_group = 1
        counter = 0
        while counter < len(ALL_CONSIDERED_STUDENTS):
            grp = GROUPS.pop(0)
            trouble_in_group = 0
            for kid in grp:
                if kid.sociability == 0:
                    trouble_in_group = trouble_in_group + 1
            if trouble_in_group < max_trouble_per_group:
                student = RANDOMIZED_CONSIDERED_STUDENTS.pop(0)
                grp.append(student)
                counter = counter + 1
                GROUPS.append(grp)
            else:
                GROUPS.append(grp)
        # put this check for debugging in case i did something that causes not all the students
        # from the randomized array to be put in a group
        if len(RANDOMIZED_CONSIDERED_STUDENTS) > 0:
            print("ERROR CODE 1")
    elif DESIRED_GROUP_SIZE != 0 and NUM_DESIRED_GROUPS == 0:
        # HAS DESIRED GROUP SIZE
        preliminary_groups = []
        unaddable = []
        while len(RANDOMIZED_CONSIDERED_STUDENTS) > MIN_GROUP_SIZE:
            group = []
            num_trouble_students = 0
            grp_count = 0
            while grp_count < MIN_GROUP_SIZE:
                student = RANDOMIZED_CONSIDERED_STUDENTS.pop(0)
                if student.sociability == 0:
                    if num_trouble_students == 0:
                        group.append(student)
                        grp_count = grp_count + 1
                    else:
                        unaddable.append(student)
                else:
                    group.append(student)
                    grp_count = grp_count + 1
            preliminary_groups.append(group)
        if len(RANDOMIZED_CONSIDERED_STUDENTS) > 0:
            for group in preliminary_groups:
                if len(RANDOMIZED_CONSIDERED_STUDENTS) > 0:
                    student = RANDOMIZED_CONSIDERED_STUDENTS.pop(0)
                    if student.sociability == 0:
                        already_trouble_in_group = False
                        for kid in group:
                            if kid.sociability == 0:
                                already_trouble_in_group = True
                        if already_trouble_in_group:
                            unaddable.append(student)
                        else:
                            group.append(student)
                    else:
                        group.append(student)
                else:
                    break
        if len(unaddable) > 0:
            # array of arrays structured like [# of trouble students, # of students, pointer to position of array of students in the prelimary groups array]
            trouble = []
            counter = 0
            for group in preliminary_groups:
                trouble_count = 0
                for kid in group:
                    if kid.sociability == 0:
                        trouble_count = trouble_count + 1
                temp = []
                temp.append(trouble_count)
                temp.append(len(group))
                temp.append(counter)
                counter = counter + 1
                trouble.append(temp)
        while len(unaddable) > 0:
            sorted(trouble)
            group = trouble.pop(0)
            if group[1] < MAX_GROUP_SIZE:
                pointer = group[2]
                students = preliminary_groups[pointer]
                students.append(unaddable.pop(0))
                preliminary_groups.pop(pointer)
                GROUPS.append(students)
            else:
                GROUPS.append(group)
        for group in preliminary_groups:
            GROUPS.append(group)
    else:
        with open("/Users/wasecahodson/Desktop/classgroupings/ERRORS.txt", "w") as er:
            er.write("ERROR: Please put NA in either the Number of Desired Groups or the Desired Group Size field - Cannot have "
              "a value in both fields at the same time or no value in either field")
        er.close()
        return


def read_to_file():
    file = []
    empty = ""
    file.append(empty)
    title = "                                             ASSIGNED GROUPS"
    file.append(title)
    file.append(empty)
    file.append(empty)
    num_groups = len(GROUPS)
    if num_groups == 2:
        # 2 team format - A B
        first_team_row = "          {0:<36}{1:<36}".format(TEAMS[0], TEAMS[1])
        file.append(first_team_row)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            row = "                      {0:<25}           {1:<25}".format(nameA, nameB)
            file.append(row)
    elif num_groups == 3:
        # 3 team format - ABC
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
    elif num_groups == 4:
        # 2 TEAM FORMAT - ABCD
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        team_row_one = "                    {0:<36}{1:<36}".format(TEAMS[0], TEAMS[1])
        file.append(team_row_one)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            row = "                      {0:<25}           {1:<25}".format(nameA, nameB)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        team_row_one = "                    {0:<36}{1:<36}".format(TEAMS[2], TEAMS[3])
        file.append(team_row_one)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            row = "                      {0:<25}           {1:<25}".format(nameA, nameB)
            file.append(row)
    elif num_groups == 5:
        # 3 TEAM FORMAT - ABCDE
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = " "
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[3], TEAMS[4], " ")
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
    elif num_groups == 6:
        # 3 TEAM FORMAT - ABCDEF
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[3], TEAMS[4], TEAMS[5])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
    elif num_groups == 7:
        # 3 TEAM FORMAT - ABCDEFH
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[3], TEAMS[4], TEAMS[5])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = " "
        grpB = GROUPS.pop(0)
        grpC = " "
        team_row = "          {0:<31}{1:<31}{2:<31}".format(" ", TEAMS[6], " ")
        file.append(team_row)
        while len(grpB) > 0:
            kidB = grpB.pop(0)
            nameB = kidB.name
            nameA = " "
            nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
    elif num_groups == 8:
        # 2 TEAM FORMAT - ABCDEFGH
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        team_row_one = "                    {0:<36}{1:<36}".format(TEAMS[0], TEAMS[1])
        file.append(team_row_one)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            row = "                      {0:<25}           {1:<25}".format(nameA, nameB)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        team_row_one = "                    {0:<36}{1:<36}".format(TEAMS[2], TEAMS[3])
        file.append(team_row_one)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            row = "                      {0:<25}           {1:<25}".format(nameA, nameB)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        team_row_one = "                    {0:<36}{1:<36}".format(TEAMS[4], TEAMS[5])
        file.append(team_row_one)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            row = "                      {0:<25}           {1:<25}".format(nameA, nameB)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        team_row_one = "                    {0:<36}{1:<36}".format(TEAMS[6], TEAMS[7])
        file.append(team_row_one)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            row = "                      {0:<25}           {1:<25}".format(nameA, nameB)
            file.append(row)
    elif num_groups == 9:
        # 3 TEAM FORMAT - A THROUGH I
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[3], TEAMS[4], TEAMS[5])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[6], TEAMS[7], TEAMS[8])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
    elif num_groups == 10:
        # 3 TEAM FORMAT - A-I, K
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[3], TEAMS[4], TEAMS[5])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[6], TEAMS[7], TEAMS[8])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = " "
        grpB = GROUPS.pop(0)
        grpC = " "
        team_row = "          {0:<31}{1:<31}{2:<31}".format(" ", TEAMS[9], " ")
        file.append(team_row)
        while len(grpB) > 0:
            nameA = " "
            kidB = grpB.pop(0)
            nameB = kidB.name
            nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
    elif num_groups == 11:
        # 3 TEAM FORMAT - A-K
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[3], TEAMS[4], TEAMS[5])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[6], TEAMS[7], TEAMS[8])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = " "
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[9], TEAMS[10], " ")
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
    elif num_groups == 12:
        # 3 TEAM FORMAT - A -L
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[0], TEAMS[1], TEAMS[2])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[3], TEAMS[4], TEAMS[5])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[6], TEAMS[7], TEAMS[8])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
        grpA = GROUPS.pop(0)
        grpB = GROUPS.pop(0)
        grpC = GROUPS.pop(0)
        team_row = "          {0:<31}{1:<31}{2:<31}".format(TEAMS[9], TEAMS[10], TEAMS[11])
        file.append(team_row)
        while len(grpA) > 0 or len(grpB) > 0 or len(grpC) > 0:
            if len(grpA) > 0:
                kidA = grpA.pop(0)
                nameA = kidA.name
            else:
                nameA = " "
            if len(grpB) > 0:
                kidB = grpB.pop(0)
                nameB = kidB.name
            else:
                nameB = " "
            if len(grpC) > 0:
                kidC = grpC.pop(0)
                nameC = kidC.name
            else:
                nameC = " "
            row = "            {0:<25}      {1:<25}      {2:<25}".format(nameA, nameB, nameC)
            file.append(row)
        file.append(empty)
        file.append(empty)
    with open("RESULTS.txt", "w") as f:
        for item in file:
            f.write(item)
            f.write("\n")


def run_program():
    global ALL_CONSIDERED_STUDENTS
    global TROUBLE_STUDENTS
    read_in_teams()
    file = get_file_location()
    read_file(file)
    randomize()
    group_making_algorithm_chooser()
    read_to_file()
    result = "RESULTS.txt"
    subprocess.call(['open', '-a', 'TextEdit', result])


run_program()
