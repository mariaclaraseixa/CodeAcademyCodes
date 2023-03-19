import random

class Magic8Ball:
    def __init__(self):
        self.userName = ""
        self.question = ""
        self.answer = ""

    def generate_answer(self):
        random_number = random.randint(1, 9)
        if random_number == 1:
            self.answer = "Yes - definitely"
        elif random_number == 2:
            self.answer = "It is decidely so"
        elif random_number == 3:
            self.answer = "Without a doubt"
        elif random_number == 4:
            self.answer = "Reply hazy, try again"
        elif random_number == 5:
            self.answer = "Ask again later"
        elif random_number == 6:
            self.answer = "Better not tell you now"
        elif random_number == 7:
            self.answer = "My sources say no"
        elif random_number == 8:
            self.answer = "Outlook not so good"
        elif random_number == 9:
            self.answer = "Very doubtful"

        if self.answer == "":
            raise ValueError("Error")

    def get_answer(self):
        return self.answer

    def ask_question(self, userName, question):
        self.userName = userName
        self.question = question
        self.generate_answer()

if __name__ == '__main__':
    print("[Code Academy] Sal's Shipping")
    magic_8_ball = Magic8Ball()
    magic_8_ball.ask_question("John", "Will I win the lottery?")
    print("Magic 8-Ball's answer: [" + magic_8_ball.get_answer() + "]")
