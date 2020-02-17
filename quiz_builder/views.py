
from django.http import JsonResponse
from .forms import ItemsForm
from django.views.decorators.csrf import csrf_exempt
from .quiz_builder import formatQuiz

def parse_string(string):
    items = string.split('\n')
    return items

def viewQuiz(request, quiz_id):
    quiz = formatQuiz()
    return JsonResponse(quiz, safe=False)

@csrf_exempt
def createQuiz(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            items = request.POST['items']
            items = parse_string(items)
            

            return JsonResponse({'success': True}, safe=False)
        else:
            return JsonResponse({})
