from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'text', 'option_a', 'option_b', 'option_c', 'option_d',
            'correct_option', 'difficulty', 'points'
        ]


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super().__init__(*args, **kwargs)
        for q in questions:
            self.fields[f'question_{q.id}'] = forms.ChoiceField(
                label=q.text,
                choices=[
                    ('A', q.option_a),
                    ('B', q.option_b),
                    ('C', q.option_c),
                    ('D', q.option_d),
                ],
                widget=forms.RadioSelect,
                required=True
            )
