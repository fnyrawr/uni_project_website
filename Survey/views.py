from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .forms import QuestionForm, QuestionSearchForm
from .models import Question


def question_list(request):
    all_questions = None
    questions_found = None
    search = False
    searchForm = QuestionSearchForm
    category = 'Project'
    data = None
    if request.method == "POST":
        search = True
        searchForm = QuestionSearchForm(request.POST)
        data = searchForm.data
        category = data['category']
        if category:
            questions_found = Question.objects.filter(category__contains=category).order_by('timestamp')
    else:
        all_questions = Question.objects.filter(category__contains=category).order_by('timestamp')

    context = {'all_questions': all_questions,
               'questions_found': questions_found,
               'search': search,
               'form': searchForm,
               'data': data,
               }
    return render(request, 'viewquestions.html', context)


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'newquestion.html'

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        print(request.POST.get('category'))
        if form.is_valid():
            question = form.save()

            return redirect('about')

    def form_valid(self, form):
        return super().form_valid(form)


class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy('viewquestions')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, **kwargs):
        question_id = kwargs['pk']
        question = Question.objects.get(id=question_id)
        category = question.category
        question.delete()
        all_questions = Question.objects.filter(category__contains=category).order_by('timestamp')
        context = {'all_questions': all_questions,
                   'questions_found': None,
                   'search': False,
                   'form': QuestionSearchForm,
                   'data': None,
                   }
        return render(request, 'viewquestions.html', context)
