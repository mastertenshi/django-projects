from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.db import connection

from django.views import generic


from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by('-published_date')[:5]

# def index(request):
#     latest_question_list = Question.objects.order_by('-published_date')[:5]
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     return render(request, 'polls/index.html', {
#         'latest_question_list': latest_question_list,
#     })


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {
#         'question': question,
#     })


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {
#         'question': question
#     })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    with connection.cursor() as c:
        c.execute(f'''
            UPDATE polls_choice
            SET votes = votes + 1
            WHERE question_id={question_id}
                AND id={selected_choice.id}''')

    return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))
