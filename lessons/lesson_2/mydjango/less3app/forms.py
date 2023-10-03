from django.forms import Form, IntegerField, CharField, DateField
from django.forms import Textarea, DateTimeInput, DateInput

import datetime

'''
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now_add=True)
'''

class CreateComment(Form):
    author = IntegerField(min_value=1)
    post = IntegerField(min_value=1)
    comment = CharField(min_length=3, max_length=100, widget=Textarea())
    create_data = DateField(initial=datetime.datetime.now, widget=DateTimeInput(attrs={'type':'datetime-local'}))
    
    



