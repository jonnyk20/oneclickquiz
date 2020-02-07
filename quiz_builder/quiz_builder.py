from .models import QuizType, Quiz, Question, Choice, ItemType, Item



def formatChoice(choice):
    item = choice.item
    formattedChoice = item.data
    return formattedChoice

def formatQuestion(question):
    formattedQuestion = {
        'correct_answer': question.correct_answer,
        'choices': [formatChoice(c) for c in question.choice_set.all()]
    }
    return formattedQuestion


def formatQuiz():
    quiz = Quiz.objects.first()
    formattedQuiz = {
        'id': quiz.id,
        'quiz_type': quiz.quiz_type.description,
        'questions': [formatQuestion(q) for q in quiz.question_set.all()],
        'max_score': quiz.question_set.count()
    }
    return formattedQuiz
