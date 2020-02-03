
from django.http import JsonResponse
from .forms import ItemsForm
from django.views.decorators.csrf import csrf_exempt


def parse_string(string):
    items = string.split('\n')
    return items


@csrf_exempt
def createQuiz(request):
    print('>>>>>>>>>>>>>')
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            items = request.POST['items']
            items = parse_string(items)

            return JsonResponse({'items': items}, safe=False)
        else:
            print('FAIL')
            return JsonResponse({})
