from django import forms
class ArgumentForm(forms.Form):
    test_value=forms.CharField(
        label='enter name',
        max_length=30,
        widget=forms.TextInput(attrs={'class':"input"})
    )
