from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.db.models import Avg
from .forms import SurveyForm, SurveySearchForm, QuestionForm, QuestionSearchForm
from .models import Survey, Question
import matplotlib
import seaborn as sns

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


def reviews_wishes_list(request):
    all_surveys = Survey.objects.order_by('timestamp')

    context = {'all_surveys': all_surveys}
    return render(request, 'viewreviewswishes.html', context)


def statistics_diagrams(request):
    global gameidea_b64, gamedesign_b64, gameplay_b64, website_b64
    all_surveys = Survey.objects.order_by('timestamp')

    # create charts for ratings grouped by category
    avg_gameidea = Survey.objects.aggregate(Avg('gameidea')).get('gameidea__avg')
    avg_gamedesign = Survey.objects.aggregate(Avg('gamedesign')).get('gamedesign__avg')
    avg_gameplay = Survey.objects.aggregate(Avg('gameplay')).get('gameplay__avg')
    avg_website = Survey.objects.aggregate(Avg('website')).get('website__avg')
    fig1, ax1 = plt.subplots()
    labels = ['Gameidea', 'Gamedesign', 'Gameplay', 'Website']
    ratings = [avg_gameidea, avg_gamedesign, avg_gameplay, avg_website]
    colors = ['#FF9800', '#FB8C00', '#F57C00', '#EF6C00']
    ax1.barh(labels, ratings, color=colors, zorder=3)
    sns.despine(left=True, bottom=True)
    ax1.tick_params(axis='x', which='both', bottom=False)
    ax1.tick_params(axis='y', which='both', left=False)
    ax1.xaxis.label.set_color('#BDBDBD')
    ax1.tick_params(colors='#BDBDBD', which='both')
    ax1.set_xlabel('Average rating')
    fig1.suptitle('Average ratings by keyword', color='#FB8C00', fontweight='bold')
    for c in ax1.containers:
        # customize the label to account for cases when there might not be a bar section
        labels = [f'{w:.2f}' if (w := v.get_width()) > 0.49 else '' for v in c]
        # set the bar label
        ax1.bar_label(c, labels=labels, label_type='center', color='white', padding=3, fontsize=10)
    plt.grid(axis='x', which='both', color='#616161', linewidth=1, zorder=0)
    plt.gca().invert_yaxis()
    ax1.set_facecolor('#212121')
    fig1.set_facecolor('black')
    fig1.tight_layout()
    flike1 = io.BytesIO()
    fig1.savefig(flike1)
    avg_b64 = base64.b64encode(flike1.getvalue()).decode()

    # create charts for ratings grouped by category
    for i in range(0, 4):
        fig2, ax2 = plt.subplots()
        labels = ['1 - Meh', '2 - Lame', '3 - Mid', '4 - Good', '5 - Awesome']
        if i == 0:
            ratings = [
                Survey.objects.filter(gameidea__contains='1').count(),
                Survey.objects.filter(gameidea__contains='2').count(),
                Survey.objects.filter(gameidea__contains='3').count(),
                Survey.objects.filter(gameidea__contains='4').count(),
                Survey.objects.filter(gameidea__contains='5').count()
            ]
            fig2.suptitle('Ratings for Gameidea', color='#FB8C00', fontweight='bold')
        elif i == 1:
            ratings = [
                Survey.objects.filter(gamedesign__contains='1').count(),
                Survey.objects.filter(gamedesign__contains='2').count(),
                Survey.objects.filter(gamedesign__contains='3').count(),
                Survey.objects.filter(gamedesign__contains='4').count(),
                Survey.objects.filter(gamedesign__contains='5').count()
            ]
            fig2.suptitle('Ratings for Gamedesign', color='#FB8C00', fontweight='bold')
        elif i == 2:
            ratings = [
                Survey.objects.filter(gameplay__contains='1').count(),
                Survey.objects.filter(gameplay__contains='2').count(),
                Survey.objects.filter(gameplay__contains='3').count(),
                Survey.objects.filter(gameplay__contains='4').count(),
                Survey.objects.filter(gameplay__contains='5').count()
            ]
            fig2.suptitle('Ratings for Gameplay', color='#FB8C00', fontweight='bold')
        else:
            ratings = [
                Survey.objects.filter(website__contains='1').count(),
                Survey.objects.filter(website__contains='2').count(),
                Survey.objects.filter(website__contains='3').count(),
                Survey.objects.filter(website__contains='4').count(),
                Survey.objects.filter(website__contains='5').count()
            ]
            fig2.suptitle('Ratings for Website', color='#FB8C00', fontweight='bold')
        colors = ['#EF6C00', '#F57C00', '#FB8C00', '#FF9800']
        ax2.barh(labels, ratings, color=colors, zorder=3)
        sns.despine(left=True, bottom=True)
        ax2.tick_params(axis='x', which='both', bottom=False)
        ax2.tick_params(axis='y', which='both', left=False)
        ax2.xaxis.label.set_color('#BDBDBD')
        ax2.tick_params(colors='#BDBDBD', which='both')
        ax2.set_xlabel('Count votes')
        for c in ax2.containers:
            # customize the label to account for cases when there might not be a bar section
            labels = [f'{w:.0f}' if (w := v.get_width()) > 0.49 else '' for v in c]
            # set the bar label
            ax2.bar_label(c, labels=labels, label_type='center', color='white', padding=3, fontsize=10)
        plt.grid(axis='x', which='both', color='#616161', linewidth=1, zorder=0)
        ax2.set_facecolor('#212121')
        fig2.set_facecolor('black')
        fig2.tight_layout()
        flike2 = io.BytesIO()
        fig2.savefig(flike2)
        if i == 0:
            gameidea_b64 = base64.b64encode(flike2.getvalue()).decode()
        elif i == 1:
            gamedesign_b64 = base64.b64encode(flike2.getvalue()).decode()
        elif i == 2:
            gameplay_b64 = base64.b64encode(flike2.getvalue()).decode()
        else:
            website_b64 = base64.b64encode(flike2.getvalue()).decode()

    context = {'all_surveys': all_surveys,
               'average_ratings_chart': avg_b64,
               'gameidea_ratings_chart': gameidea_b64,
               'gamedesign_ratings_chart': gamedesign_b64,
               'gameplay_ratings_chart': gameplay_b64,
               'website_ratings_chart': website_b64,
               }
    return render(request, 'statistics.html', context)


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
           colors=colors, startangle=-270, counterclock=False, pctdistance=0.85, textprops={'color': '#FFFFFF'},
           wedgeprops={'edgecolor': '#000000', 'linewidth': 3})
    centre_circle = plt.Circle((0, 0), 0.70, fc='black')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    fig.tight_layout()
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
