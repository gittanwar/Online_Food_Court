from django.forms import ModelForm

from .models import Restaurant


class RestroForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"
