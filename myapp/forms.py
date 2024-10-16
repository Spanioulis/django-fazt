from django import forms

class CreateNewTask(forms.Form):
  title = forms.CharField(label="Título", max_length=100)
  description = forms.CharField(label="Descripción", widget=forms.Textarea)