from django import forms

class userForms(forms.Form):
    num1=forms.CharField(label="Value 1",required=False)
    num2=forms.CharField(label="Value 2",required=True)