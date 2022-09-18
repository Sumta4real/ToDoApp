from turtle import title
from .models import Task, User
from distutils.command.clean import clean
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','target_date','target_time','content','status']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        #check if the title inputed is already in the database 
        query_title = Task.objects.filter(title__icontains=title)
        # the primary key is not None(indicating the task is not newly created)
        if self.instance.pk is not None:
            print(self.instance.pk)
            #exclude the task from the validation
            query_title = query_title.exclude(pk=self.instance.pk)
        #if there is any value in query_title object
        elif query_title.exists():
            #display an error with the containing string
            self.add_error("title", f'\'{title}\' is already in use. Please pick another title')
        return data


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname','lastname','username','Password','gender','email']


class TaskFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    target_date = forms.DateField()
    target_time = forms.TimeField()

    #Set up Validation for the inputs
    # def clean_title(self):
    #     #cleaned_data is an attribute that return a dictionary containing the form data
    #     cleaned_data = self.cleaned_data #dictionary
    #     #print(cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'another task':
    #         raise forms.ValidationError('This title is taken')
    #     #print(title)
    #     return title
 
    def clean(self):
        cleaned_data = self.cleaned_data
        print('all data', cleaned_data)
        title = cleaned_data.get('content').lower().strip()
        if title == 'another content':
            self.add_error('title','This title is taken')
            raise forms.ValidationError("You can't use this content")
        return cleaned_data