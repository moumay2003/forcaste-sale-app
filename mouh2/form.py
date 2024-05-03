from django import forms
from mouh2.models import Message


class NumberForm(forms.Form):
    number = forms.IntegerField()
    
    


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']