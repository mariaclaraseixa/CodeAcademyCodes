import random

class MagicEightBall:
    def __init__(self):
        self.responses = {
            1: "Yes - definitely",
            2: "It is decidely so",
            3: "Without a doubt",
            4: "Reply hazy, try again",
            5: "Ask again later",
            6: "Better not tell you now",
            7: "My sources say no",
            8: "Outlook not so good",
            9: "Very doubtful"
        }

    def get_answer(self):
        random_number = random.randint(1, 9)
        return self.responses.get(random_number, "Error")


if __name__ == '__main__':
    print("[Code Academy] Sal's Shipping")
    userName = " "
    question = " "
    magic_ball = MagicEightBall()
    answer = magic_ball.get_answer()

    print("Magic 8-Ball's answer: [" + answer + "]")
    print(userName + " asks: " + question)
