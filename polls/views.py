from django.http import HttpResponse
from .models import Question
from django.shortcuts import render
def index(request):

    return render(request,'polls/index.html')

# Leave the rest of the views (detail, results, vote) unchanged


    # Leave the rest of the views (detail, results, vote) unchanged
def detail(request, question_id):
    return render(request, 'polls/ali.html')


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)