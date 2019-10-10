from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404


# Create your views here.
# http://127.0.0.1:8000/polls/
# def index(request):
#     lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # output = ','.join([q.question_text for q in lastest_question_list])
#     # return HttpResponse(output)
#     template = loader.get_template('polls/index.html')
#     context = {
#         'lastest_question_list': lastest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


# http://127.0.0.1:8000/polls/1/
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# http://127.0.0.1:8000/polls/1/results/
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


# http://127.0.0.1:8000/polls/1/vote/
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
