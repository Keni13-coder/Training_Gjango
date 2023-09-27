from django.db import models

# Create your models here.


class User(models.Model):
    # id django прописывает само
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField() 
    
    
    def __str__(self) -> str:
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    # pip install Pillow 
    image = models.ImageField(upload_to='products/')
    
    
class Order(models.Model):
    # on_delete=models.CASCADE отвечает за удаление данных елси удалить user то и заказ удалиться
    customer = models.ForeignKey('User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    # auto-data = auto_now_add=True
    date_ordered = models.DateTimeField(auto_now_add=True)
    totel_price = models.DecimalField(max_digits=8, decimal_places=2)
    
    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    date_birthday = models.DateField(auto_now_add=False)
    
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
    

    
class HeadsTails(models.Model):
    title = models.CharField(max_length=6)
    time = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def read_title(number: int):
        resp = HeadsTails.objects.all().order_by('-id')[:number]
        return {number: resp}
    
    def __str__(self):
        return f'title: {self.title}, id: {self.id} '
    
    
class Comments(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    create_data = models.DateTimeField(auto_now_add=True)
    update_data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'author: {self.author}, post: {self.post}, comment: {self.comment}'