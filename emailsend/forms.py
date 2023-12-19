from django import forms


class EmailForm(forms.Form):
    name=forms.CharField(max_length=150)
    email=forms.EmailField(max_length=200)
    message=forms.CharField(widget=forms.Textarea)

    