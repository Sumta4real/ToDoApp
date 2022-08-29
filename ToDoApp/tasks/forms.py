from turtle import title
from .models import Task
from distutils.command.clean import clean
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','target_date','target_time','content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        #check if the title inputed is already in the database 
        query_title = Task.objects.filter(title__icontains=title)
        #if there is any value in query_title object
        if query_title.exists():
            #display an error with the containing string
            self.add_error("title", f'\'{title}\' is already in use. Please pick another title')
        return data



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