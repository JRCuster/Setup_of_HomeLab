from django import forms

class SetupForm(forms.Form):
    db_name = forms.CharField(label='Database Name', max_length=100)
    db_user = forms.CharField(label='Database User', max_length=100)
    db_pass = forms.CharField(label='Database Password', widget=forms.PasswordInput)
    db_host = forms.CharField(label='Database Host', max_length=100)
    db_port = forms.CharField(label='Database Port', max_length=100)