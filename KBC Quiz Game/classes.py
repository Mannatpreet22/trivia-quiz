class Question:
    def __init__(
        self, question, option_a, option_b, option_c, option_d, correct_option
    ):
        self.question = question
        self.options = [option_a, option_b, option_c, option_d]
        self.correct_option = correct_option

    def __repr__(self) -> str:
        return self.question

    def check_answer(self, option) -> bool:
        if self.correct_option == option:
            return True
        else:
            return False

    def get_data(self):
        return {
            "question": self.question,
            "options": self.options,
            "correct_option": self.correct_option,
        }
