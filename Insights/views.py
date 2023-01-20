from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView
from .forms import QuestionForm
from .models import Question


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'about.html'

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            question = form.save()

            return redirect('about', pk=question.id)

    def form_valid(self, form):
        return super().form_valid(form)
