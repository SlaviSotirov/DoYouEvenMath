from connection import Base
from game import Game
from player import Player
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import func


class GameInterface:

    def __init__(self):
        self.player_name = None
        self.score = 0
        self.game = Game()

        engine = create_engine("sqlite:///do_you_even_math.db")
        Base.metadata.create_all(engine)

        self.session = Session(bind=engine)

    def insert_playername(self):
        self.playername = input("Type your name: ")

    def get_score(self):
        return self.game.level ** 2

    def save_score(self, player):
        self.session.add(player)
        self.session.commit()

    def get_top10(self):
        print("Top 10\n")
        for player in self.session.query(Player).order_by(Player.score.desc()).limit(10):
            print(player)

    def get_player_score(self):
        return Player(name=self.player_name, score=self.get_score())

    def play(self):
        self.insert_playername()
        while True:
            quiz = self.game.generate_quiz()
            print("What is the answer to {}".format(self.game.quiz_to_string(quiz)))
            user_answer = self.game.insert_answer()
            correct_answer = self.game.solve_quiz(quiz)
            if self.game.is_correct(correct_answer, user_answer):
                print("Correct!")
                self.game.level_up()
            else:
                print("Ending game, your score is {}".format(self.get_score()))
                self.save_score(self.get_player_score())
                break

    def start_game(self):
        while True:
            command = input('Type "play" to play or "highscore" to see top 10 players \n>? ')
            if command == "play":
                self.play()
            elif command == "highscore":
                self.get_top10()
            elif command == "exit":
                return
            else:
                print("Invalid command! Please try again")


def main():
    asd = GameInterface()
    asd.start_game()

if __name__ == '__main__':
    main()
