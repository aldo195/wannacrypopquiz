from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_question_list': "1",
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
