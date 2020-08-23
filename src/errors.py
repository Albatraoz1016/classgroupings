class Errors:
    def __init__(self):
        self.all_errors = {}
        self.current_errors = []
        self.setup()

    def setup(self):
        self.all_errors[101] = "ERROR 101: An invalid response was specified in one of the following fields: \n" \
                               "             Desired # of Groups, Min Group Size or Max Group Size."
        self.all_errors[102] = "ERROR 102: Only one field can be specified to be used (the others must have 0 for " \
                               "response) among the following fields: \n" \
                               "             Desired # of Groups, Min Group Size, or Max Group Size."
        self.all_errors[103] = "ERROR 103: Exactly one field must be specified with a positive integer (not 0) among" \
                               "the following fields: \n" \
                               "             Desired # of Groups, Min Group Size, or Max Group Size."
        self.all_errors[104] = "ERROR 104: An invalid response was given for the field Avoid Trouble with Trouble." \
                               "           Only use values YES or NO to respond with."
        self.all_errors[105] = "ERROR 105: An invalid response was given for the field Avoid Trouble with Shy." \
                               "           Only use values YES or NO to respond with."
        self.all_errors[106] = "ERROR 106: An invalid response was given for the field Avg Based " \
                               "on Sociability rating." \
                               "           Only use values YES or NO to respond with."
        self.all_errors[107] = "ERROR 107: A YES response cannot be specified to Avg Based Sociability rating while " \
                               "also having a YES response for either Avoid Trouble with Trouble OR Avoid Trouble" \
                               "With Shy."
        self.all_errors[108] = "ERROR 108: The sociaibility rating assigned to a student was not a valid response." \
                               "Please only use an integer between 0 and 5."

    def currently_have_errors(self):
        if len(self.current_errors) > 0:
            return True
        return False

    def get_error_message(self, code):
        if code in  self.all_errors:
            return self.all_errors.get(code)
        return None

    def add_current_error(self, code):
        if code in self.all_errors:
            if code not in self.current_errors:
                self.current_errors.append(code)

    def get_all_messages(self):
        messages = []
        for code in self.current_errors:
            msg = self.get_error_message(code)
            messages.append(msg)
        return messages