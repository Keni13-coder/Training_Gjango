from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    date_birthday = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'
    
    def full_name(self):
        return f'{self.name} {self.second_name}'
    
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Title is {self.title}, id {self.id}'
    
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'
    
    
class Comments(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'author: {self.author}, post: {self.post}, comment: {self.comment}'
