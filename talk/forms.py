from django.forms import ModelForm
from.models import Promt

#My forms:

class PromtForm(ModelForm):
    class Meta:
        model=Promt
        fields=['prompt_text']