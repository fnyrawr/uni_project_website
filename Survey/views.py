from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from .forms import SurveyForm, SurveySearchForm, QuestionForm, QuestionSearchForm
from .models import Survey, Question
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io, base64


def survey_list(request):
    all_surveys = None
    surveys_found = None
    search = False
    searchForm = SurveySearchForm
    data = None
    if request.method == "POST":
        search = True
        searchForm = SurveySearchForm(request.POST)
        data = searchForm.data
        name = data['name']
        review = data['review']
        wishes = data['wishes']
        if name:
            surveys_found = Survey.objects.filter(name__contains=name).order_by('timestamp')
        if review:
            surveys_found = Survey.objects.filter(review__contains=review).order_by('timestamp')
        if wishes:
            surveys_found = Survey.objects.filter(wishes__contains=wishes).order_by('timestamp')
    else:
        all_surveys = Survey.objects.order_by('timestamp')

    context = {'all_surveys': all_surveys,
               'surveys_found': surveys_found,
               'search': search,
               'form': searchForm,
               'data': data,
               }
    return render(request, 'viewsurveys.html', context)


class SurveyCreateView(CreateView):
    model = Survey
    form_class = SurveyForm
    template_name = 'newsurvey.html'

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save()

            return redirect('about')


class SurveyDeleteView(DeleteView):
    model = Survey
    success_url = reverse_lazy('viewsurveys')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, **kwargs):
        survey_id = kwargs['pk']
        survey = Survey.objects.get(id=survey_id)
        survey.delete()
        all_surveys = Question.objects.order_by('timestamp')
        context = {'all_surveys': all_surveys,
                   'questions_found': None,
                   'search': False,
                   'form': SurveySearchForm,
                   'data': None,
                   }
        return render(request, 'viewsurveys.html', context)


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

    # create chart to display questions per category
    labels = 'Project\nManagement', 'Mechanics', 'Multiplayer', 'Assets\nUI\nAudio', 'Website'
    sizes = [
        Question.objects.filter(category__contains='Project').count(),
        Question.objects.filter(category__contains='Mechanics').count(),
        Question.objects.filter(category__contains='Multiplayer').count(),
        Question.objects.filter(category__contains='Assets').count(),
        Question.objects.filter(category__contains='Website').count(),
    ]
    explode = (0.1, 0, 0, 0, 0)
    if category == 'Mechanics': explode = (0, 0.1, 0, 0, 0)
    if category == 'Multiplayer': explode = (0, 0, 0.1, 0, 0)
    if category == 'Assets': explode = (0, 0, 0, 0.1, 0)
    if category == 'Website': explode = (0, 0, 0, 0, 0.1)
    colors = ['#E65100', '#EF6C00', '#F57C00', '#FB8C00', '#FF9800']
    fig, ax = plt.subplots()
    fig.set_facecolor('black')
    ax.pie(sizes, labels=labels, explode=explode, autopct=lambda x: '{:.0f}'.format(x * sum(sizes) / 100),
           colors=colors, startangle=-270, counterclock=False, pctdistance=0.85, textprops={'color':'#FFFFFF'})
    centre_circle = plt.Circle((0, 0), 0.70, fc='black')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    flike = io.BytesIO()
    fig.savefig(flike)
    b64 = base64.b64encode(flike.getvalue()).decode()

    context = {'all_questions': all_questions,
               'questions_found': questions_found,
               'search': search,
               'form': searchForm,
               'data': data,
               'chart': b64,
               }
    return render(request, 'viewquestions.html', context)


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'newquestion.html'

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
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
