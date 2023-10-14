from django.forms import ModelForm
from .models import *

class TaskForm(ModelForm):

    class Meta:
        Model = Task
        fields = '__all__'

    