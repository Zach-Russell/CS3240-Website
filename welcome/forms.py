from allauth.account.forms import LoginForm
from django import forms
class MyCustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["login"].label = ""
        self.fields['type'] = forms.ChoiceField(widget=forms.RadioSelect, choices = [('1','Tutor'),('2','Student')], )
        del(self.fields["remember"])