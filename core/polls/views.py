from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import *
from .models import *


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'polls/login.html'

    def get_success_url(self):
        return reverse_lazy('polls')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'polls/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('polls')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


def logout_user(request):
    logout(request)
    return redirect('polls')


def index(request):
    qs = SetOfQuestions.objects.all()
    context = {'polls': qs}
    print(request)
    return render(request, 'polls/index.html', context=context)


def question(request, question_id):
    if request.method == 'GET':
        question = get_object_or_404(Question, pk=question_id)

        context = {"question": question, }
        return render(request, 'polls/question_page.html', context=context)

    elif request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)

        right_answers_number = question.check_amount_of_right_answers()

        try:
            selected_answers = question.answers.filter(pk__in=dict(request.POST)['answer'])

            print(selected_answers)
        except KeyError as exception:

            return render(request, 'polls/question_page.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            collection = question.collection

            right_select_answers_number = 0
            for answer in selected_answers:
                if answer.right_or_wrong:
                    right_select_answers_number += 1
            if right_answers_number == right_select_answers_number and len(selected_answers) == right_answers_number:
                collection.right_answers += 1
                collection.save()

            all_questions = collection.questions.all()
            all_questions_list = list(all_questions)
            try:
                next_question_index_in_list = all_questions_list.index(question) + 1
                next_question_id = all_questions_list[next_question_index_in_list].id
                return redirect('one_question', question_id=next_question_id)
            except IndexError:
                return redirect('finish', collection_id=collection.id)


def finish(request, collection_id):
    qs = SetOfQuestions.objects.get(pk=collection_id)
    len_of_collection = len(qs.questions.all())
    right_answers = qs.right_answers
    percent_of_right_answers = f'{right_answers / len_of_collection * 100}%'
    context = {'collection': qs, 'right': right_answers, 'percent': percent_of_right_answers}
    qs.right_answers = 0
    qs.save()
    return render(request, 'polls/finish.html', context)


def list_of_questions(request, collection_id):
    qs = Question.objects.filter(collection=collection_id)
    context = {"list_of_questions": qs}

    return render(request, 'polls/list_of_questions.html', context=context)
