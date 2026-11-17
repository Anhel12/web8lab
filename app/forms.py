from django import forms
from .models import Comment, Blog


class FeedbackForm(forms.Form):

    name = forms.CharField(
        label='Ваше имя',
        min_length=2,
        max_length=50
    )

    email = forms.EmailField(
        label='Email'
    )

    course = forms.ChoiceField(
        label='Какое направление вам интересно?',
        choices=[
            ('programming', 'Программирование'),
            ('design', 'Дизайн'),
            ('languages', 'Иностранные языки'),
        ]
    )

    rating = forms.ChoiceField(
        label='Оцените сайт',
        choices=[
            ('5', 'Отлично'),
            ('4', 'Хорошо'),
            ('3', 'Удовлетворительно'),
            ('2', 'Плохо'),
            ('1', 'Очень плохо'),
        ],
        widget=forms.RadioSelect
    )

    topics = forms.MultipleChoiceField(
        label='Какие темы вы хотели бы изучать?',
        choices=[
            ('python', 'Python'),
            ('web', 'Web-разработка'),
            ('design', 'Дизайн'),
            ('languages', 'Иностранные языки'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    wishes = forms.CharField(
        label='Ваши пожелания',
        widget=forms.Textarea,
        required=False,
        max_length=500
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': ''
        }
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Введите ваш комментарий'
            })
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'content']

        labels = {
            'title': 'Заголовок',
            'description': 'Краткое содержание',
            'image': 'Картинка статьи',
            'content': 'Полное содержание'
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите заголовок статьи'
            }),

            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Введите краткое содержание'
            }),

            'content': forms.Textarea(attrs={
                'rows': 10,
                'placeholder': 'Введите текст статьи'
            })
        }