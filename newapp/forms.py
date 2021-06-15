from django.forms import ModelForm
from .models import Test


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['GraphInterval', 'GraphDt', 'GraphFunction']
        labels = {
            'GraphInterval': 'Интервал t, дней',
            'GraphDt': 'Шаг t, часы',
            'GraphFunction': 'Функция'
        }
