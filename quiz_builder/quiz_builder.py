from .models import QuizType, Quiz, Question, Choice, ItemType, Item


def buildQuiz():
    output = {}
    quiz = Quiz.objects.first()
    print('QUIZ', quiz)
    return quiz
