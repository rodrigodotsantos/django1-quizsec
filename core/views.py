from django.shortcuts import render

# Views de autenticação e home
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Count, Sum
from .forms import SignUpForm, QuestionForm, QuizForm
from .models import Question, QuestionStat, QuizAttempt, AnsweredQuestion, Profile

def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'ADMIN'

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def home(request):
    return render(request, 'home.html')

#View do quiz (usuário comum)
@login_required
def play_quiz(request):
    # Seleciona 15 perguntas (pode melhorar para sortear aleatório)
    questions = Question.objects.all()[:15]
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            attempt = QuizAttempt.objects.create(user=request.user)
            score = 0
            correct_count = 0
            wrong_count = 0

            for q in questions:
                chosen = form.cleaned_data.get(f'question_{q.id}')
                is_correct = (chosen == q.correct_option)
                if is_correct:
                    score += q.points
                    correct_count += 1
                else:
                    wrong_count += 1

                AnsweredQuestion.objects.create(
                    attempt=attempt,
                    question=q,
                    chosen_option=chosen,
                    is_correct=is_correct
                )

                stats, created = QuestionStat.objects.get_or_create(question=q)
                stats.times_answered += 1
                if is_correct:
                    stats.times_correct += 1
                stats.save()

            attempt.score = score
            attempt.correct_count = correct_count
            attempt.wrong_count = wrong_count
            attempt.save()

            return render(request, 'quiz_result.html', {
                'attempt': attempt,
                'questions': questions,
            })
    else:
        form = QuizForm(questions=questions)

    return render(request, 'play_quiz.html', {
        'form': form,
        'questions': questions,
    })


@user_passes_test(is_admin)
def question_list_admin(request):
    questions = Question.objects.all().select_related('stats')
    return render(request, 'admin/question_list.html', {
        'questions': questions,
    })


@user_passes_test(is_admin)
def question_create_admin(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            QuestionStat.objects.get_or_create(question=question)
            return redirect('admin_question_list')
    else:
        form = QuestionForm()
    return render(request, 'admin/question_form.html', {'form': form})

#Views de administração (role ADMIN)
@user_passes_test(is_admin)
def users_performance_admin(request):
    users_stats = (
        QuizAttempt.objects
        .values('user__username')
        .annotate(
            attempts_count=Count('id'),
            total_score=Sum('score'),
            total_correct=Sum('correct_count'),
            total_wrong=Sum('wrong_count'),
        )
        .order_by('-total_score')
    )
    return render(request, 'admin/users_performance.html', {
        'users_stats': users_stats,
    })

# Filtros e seleção das perguntas
# core/views.py
import random

@login_required
def play_quiz(request):
    # Exemplo: pegar todas e sortear 15 aleatórias
    all_ids = list(Question.objects.values_list('id', flat=True))
    random.shuffle(all_ids)
    selected_ids = all_ids[:15]
    questions = list(Question.objects.filter(id__in=selected_ids))

    # Opcional: ordenar na mesma ordem do sorteio
    questions.sort(key=lambda q: selected_ids.index(q.id))

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            attempt = QuizAttempt.objects.create(user=request.user)
            score = 0
            correct_count = 0
            wrong_count = 0

            for q in questions:
                chosen = form.cleaned_data.get(f'question_{q.id}')
                is_correct = (chosen == q.correct_option)
                if is_correct:
                    score += q.points
                    correct_count += 1
                else:
                    wrong_count += 1

                AnsweredQuestion.objects.create(
                    attempt=attempt,
                    question=q,
                    chosen_option=chosen,
                    is_correct=is_correct
                )

                stats, created = QuestionStat.objects.get_or_create(question=q)
                stats.times_answered += 1
                if is_correct:
                    stats.times_correct += 1
                stats.save()

            attempt.score = score
            attempt.correct_count = correct_count
            attempt.wrong_count = wrong_count
            attempt.save()

            return render(request, 'quiz_result.html', {
                'attempt': attempt,
                'questions': questions,
            })
    else:
        form = QuizForm(questions=questions)

    return render(request, 'play_quiz.html', {
        'form': form,
        'questions': questions,
    })

# teste diagnostico
def debug_auth(request):
    return render(request, 'debug_auth.html', {
        'user': request.user,
        'is_authenticated': request.user.is_authenticated,
        'profile': getattr(request.user, 'profile', None)
    })
