import subprocess

from src.classroom import Classroom
from src.settings import Settings
from src.errors import Errors

location_file = "/Users/wasecahodson/Desktop/classgrouping/filelocation.txt"
results_file = "/Users/wasecahodson/Desktop/classgrouping/output/RESULTS.txt"
errors_file = "/Users/wasecahodson/Desktop/classgrouping/output/ERRORS.txt"
testing_results_file = "/Users/wasecahodson/Desktop/classgrouping/output/TESTING_RESULTS.txt"


def write_results(croom):
    sets = []
    while len(croom.closed_groups) > 0:
        set = []
        if len(croom.closed_groups) >= 3:
            grpA = croom.closed_groups.pop(0)
            grpB = croom.closed_groups.pop(0)
            grpC = croom.closed_groups.pop(0)
            while len(grpA.students) > 0 or len(grpB.students) > 0 or len(grpC.students) > 0:
                studentA = ""
                studentB = ""
                studentC = ""
                if len(grpA.students) > 0:
                    kidA = grpA.students.pop(0)
                    studentA = kidA.name
                if len(grpB.students) > 0:
                    kidB = grpB.students.pop(0)
                    studentB = kidB.name
                if len(grpC.students) > 0:
                    kidC = grpC.students.pop(0)
                    studentC = kidC.name
                set.append(studentA)
                set.append(studentB)
                set.append(studentC)
        elif len(croom.closed_groups) == 2:
            grpA = croom.closed_groups.pop(0)
            grpB = croom.closed_groups.pop(0)
            while len(grpA.students) > 0 or len(grpB.students) > 0:
                studentA = ""
                studentB = ""
                studentC = ""
                if len(grpA.students) > 0:
                    kidA = grpA.students.pop(0)
                    studentA = kidA.name
                if len(grpB.students) > 0:
                    kidB = grpB.students.pop(0)
                    studentB = kidB.name
                set.append(studentA)
                set.append(studentB)
                set.append(studentC)
        elif len(croom.closed_groups) == 1:
            grpA = croom.closed_groups.pop(0)
            while len(grpA.students) > 0:
                studentA = ""
                studentB = ""
                studentC = ""
                if len(grpA.students) > 0:
                    kidA = grpA.students.pop(0)
                    studentA = kidA.name
                set.append(studentA)
                set.append(studentB)
                set.append(studentC)
        sets.append(set)
    with open(results_file, "w") as file:
        file.write("\n")
        file.write("                                             ASSIGNED GROUPS" + "\n")
        file.write("\n")
        for item in sets:
            while len(item) > 0:
                aa = item.pop(0)
                ba = item.pop(0)
                ca = item.pop(0)
                a = f'{aa: <{25}}'
                b = f'{ba: <{25}}'
                c = f'{ca: <{25}}'
                file.write("            " + a + "     " + b + "     " + c + "\n")
            file.write("\n")
            file.write("\n")
    file.close()


def print_testing_report(stgs):
    towrite = []
    towrite.append("--------------------------------------------------------------------\n")
    towrite.append("\n")
    towrite.append("Desired / Actual # Groups:     " + str(stgs.desired_num_groups) + " / " + str(stgs.actual_num_groups) + "\n")
    towrite.append("Desired / Actual Max Size:     " + str(stgs.desired_max) + " / " + str(stgs.actual_max) + "\n")
    towrite.append("Desired / Actual Min Size:     " + str(stgs.desired_min) + " / " + str(stgs.actual_min) + "\n")
    towrite.append("\n")
    towrite.append("Report Type:   " + str(stgs.printable_report_type()) + "\n")
    towrite.append("\n")
    towrite.append("Total # of Students:     " + str(stgs.get_num_students()) + "\n")
    towrite.append("Number of Trouble Kids:  " + str(stgs.get_num_trouble()) + "\n")
    towrite.append("Number of Shy Kids:      " + str(stgs.get_num_shy()) + "\n")
    towrite.append("\n")
    towrite.append("# of Trouble Specific Groups:    " + str(stgs.num_t_groups) + "\n")
    towrite.append("# of Shy Specific Groups:        " + str(stgs.num_s_groups) + "\n")
    towrite.append("Max Trouble Per Group:           " + str(stgs.max_t_per_group) + "\n")
    towrite.append("Max Shy Per Group:               " + str(stgs.max_s_per_group) + "\n")
    towrite.append("\n")
    towrite.append("--------------------------------------------------------------------" + "\n")
    towrite.append("\n")
    with open(testing_results_file, "w") as file:
        for entry in towrite:
            file.write(entry)
    file.close()


def write_errors(errors):
    if errors.currently_have_errors():
        messages = errors.get_all_messages()
        with open(errors_file, "w") as file:
            file.writelines(messages)
        file.close()
        return True
    else:
        with open(errors_file, "w") as file:
            file.write("")
        file.close()
        return False

def run():
    with open(location_file, "r") as file:
        location = file.readline()
    file.close()
    ers = Errors()
    settings = Settings(location, ers)
    if write_errors(ers):
        return
    classroom = Classroom(settings.created_students, settings)
    print_testing_report(settings)
    write_results(classroom)
    subprocess.call(['open', '-a', 'TextEdit', results_file])


run()
