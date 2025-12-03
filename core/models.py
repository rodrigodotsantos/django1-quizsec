from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('COMUM', 'Comum'),
        ('ADMIN', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='COMUM')

    def __str__(self):
        return f'{self.user.username} ({self.role})'


class Question(models.Model):
    DIFFICULTY_CHOICES = (
        ('F', 'Fácil'),
        ('M', 'Média'),
        ('D', 'Difícil'),
    )
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(
        max_length=1,
        choices=(('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'))
    )
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, default='M')
    points = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.text


class QuestionStat(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='stats')
    times_answered = models.PositiveIntegerField(default=0)
    times_correct = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Stats: {self.question.id}'


class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attempts')
    score = models.IntegerField(default=0)
    correct_count = models.PositiveIntegerField(default=0)
    wrong_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.score}'


class AnsweredQuestion(models.Model):
    attempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chosen_option = models.CharField(max_length=1)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.attempt.id} - {self.question.id}'
