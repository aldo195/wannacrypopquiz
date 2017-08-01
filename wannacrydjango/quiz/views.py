from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Drill
from .forms import PostForm


def index(request):
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_question_list': "1",
    }
    return HttpResponse(template.render(context, request))


def post_list(request):
    return render(request, 'quiz/post_list.html', {})


def post_new(request):
    form = PostForm()
    return render(request, 'quiz/post_edit.html', {'form': form})