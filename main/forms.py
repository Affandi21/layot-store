from django.forms import ModelForm
from main.models import LayotStore

class LayotStoreForm(ModelForm):
    class Meta:
        model = LayotStore
        fields = ["name", "description", "total"]