from random import randint


class Game:
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    POWER = 4
    DIVIDE = 5

    def __init__(self):
        self.level = 0
        self.difficulty = 1

    # 1 - '+', 2 - '-', 3 - '*', 4 - '/', 5 - '^'
    def generate_quiz(self):
        operation = randint(1, 4)
        if operation is self.ADD:
            result = self.generate_add_quiz()
        elif operation is self.SUBTRACT:
            result = self.generate_sub_quiz()
        elif operation is self.MULTIPLY:
            result = self.generate_mul_quiz()
        elif operation is self.POWER:
            result = self.generate_pow_quiz()
        elif operation is self.DIVIDE:
            result = self.generate_div_quiz()

        return result

    def generate_add_quiz(self):
        first = randint(1, 100 * self.difficulty)
        second = randint(1, 50 * self.difficulty)
        return (first, self.ADD, second)

    def generate_sub_quiz(self):
        first = randint(1, 50 * self.difficulty)
        second = randint(1, 50 * self.difficulty)
        return (first, self.SUBTRACT, second)

    def generate_mul_quiz(self):
        first = randint(1, 10 * self.difficulty)
        second = randint(1, 10 * self.difficulty)
        return (first, self.MULTIPLY, second)

    def generate_pow_quiz(self):
        first = randint(1, 10 * self.difficulty)
        second = randint(1, 2 * self.difficulty)
        return (first, self.POWER, second)

    def generate_div_quiz(self):
        first = randint(1, 10 * self.difficulty)
        second = randint(1, 2 * self.difficulty)
        return (first, self.DIVIDE, second)

    def quiz_to_string(self, quiz):
        if quiz[1] is self.ADD:
            operator = "+"
        elif quiz[1] is self.SUBTRACT:
            operator = "-"
        elif quiz[1] is self.MULTIPLY:
            operator = "x"
        elif quiz[1] is self.POWER:
            operator = "^"
        elif quiz[1] is self.DIVIDE:
            operator = "/"
        return "{} {} {}".format(quiz[0], operator, quiz[2])

    def solve_quiz(self, quiz):
        first = quiz[0]
        operator = quiz[1]
        second = quiz[2]
        if operator is self.ADD:
            return first + second
        elif operator is self.SUBTRACT:
            return first - second
        elif operator is self.MULTIPLY:
            return first * second
        elif operator is self.POWER:
            return first ** second
        elif operator is self.DIVIDE:
            return first / second
        else:
            pass
            #sad

    def insert_answer(self):
        answer = input("?>")
        return int(answer)

    def is_correct(self, correct_answer, user_answer):
        return correct_answer == user_answer

    def increase_difficulty(self):
        if self.level % 10 == 0:
            self.difficulty += 1

    def level_up(self):
        self.level += 1
        self.increase_difficulty()
