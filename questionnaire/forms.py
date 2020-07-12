from django import forms

class InterestForm(forms.Form):
    interests=forms.CharField()
    hobbies = forms.CharField()
    genres = forms.CharField()
    material =forms.ChoiceField(choices=[('anime','Anime'),('music','Music')])
