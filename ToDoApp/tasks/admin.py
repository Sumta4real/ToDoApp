from django.contrib import admin
from .models import Task,User

# Register your models here.
admin.site.register(Task) #register the task model


class UserAdmin(admin.ModelAdmin):
    #specify how the details in the table should be displayed
    list_display = ['id','firstname','lastname']
    #create a serch box in to enable search inside the admin page 
    search_fields = ['firstname']

#REgister the model 'User' while specifying the admin class created for it 
admin.site.register(User,UserAdmin) 
