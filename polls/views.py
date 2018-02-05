from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.template import Template, Context
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Choice, Question


def test(request):
    return HttpResponse('Your are good')

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}  # 是一个字典
    return render(request, 'polls/index.html', context)
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context))

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = Template("""
#     <img src="/static/django.png">
#     {% if latest_question_list %}
#     <ul>
#     View中使⽤用模板
#     {% for question in latest_question_list %}
#     <li><a href="/polls/{{ question.id }}/">{{ question.question_text }} </a></li
#     >
#     {% endfor %}
#     </ul>
#     {% endif %}
#     """)
#     context = Context({'latest_question_list': latest_question_list})
#     return HttpResponse(template.render(context))    # t.render(c)

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = [{q.id: q.question_text} for q in latest_question_list]
#     # output =  [{q.id,q.question_text} for q in latest_question_list]
#     # output = ', '.join([ q.question_text  for q in latest_question_list])
#     return HttpResponse(output)



def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'polls/detail.html', {"question": question})
# def detail(request, question_id):
#     return HttpResponse('Your are looking at question {}'.format(question_id))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
# def results(request, question_id):
#     response = "You are looking at results of question {}".format(question_id)
#     return HttpResponse(response)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice', 0)     ##form表单提交 封装为一个字典
        try:
            selected_choice = question.choice_set.get(pk=choice_id)         #choice_set是一个管理器（model管理器） 和 object一样的，调用这个属性才会去查外键的值
        except Choice.DoesNotExist:
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:   ##else 子句， 没有发生异常的情况下
            selected_choice.votes += 1
            selected_choice.save()
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# def vote(request, question_id):
#     return HttpResponse('Your are voting on question {}'.format(question_id))
