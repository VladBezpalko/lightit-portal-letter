from django_filters import FilterSet

from letter.models import Letter


class LetterFilter(FilterSet):

    class Meta:
        model = Letter
        fields = {
            'response': ['isnull'],
        }
