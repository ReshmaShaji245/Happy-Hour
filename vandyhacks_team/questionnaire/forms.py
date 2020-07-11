from django import forms

class InterestForm(forms.Form):
    hobbies = forms.CharField()
    genres = forms.CharField()
    material =forms.ChoiceField(choices=[('manga','Manga'),('music','Music')])
