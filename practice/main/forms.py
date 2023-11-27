from django.forms import ModelForm, TextInput
from . models import Word


class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ["english_word", "russian_word"]
        widgets = {
            "english_word": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input an eng word'
            }),
            "russian_word": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input a rus word'
            }),
        }
