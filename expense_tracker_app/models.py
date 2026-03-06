from django.db import models
import uuid
from django.contrib.auth.models import  User
# Create your models here.

class usre_register(models.Model):
    user_id = models.UUIDField( primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    user_name = models.CharField( max_length=50)
    user_email = models.EmailField( max_length=254)
    password = models.CharField( max_length=50)
    created_at = models.DateTimeField( auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'usre_register'
        
        



class Transactions(models.Model):
    
    
    TYPE_CHOICE = (
        ('Income','INCOME'),
        ('Expense','EXPENSE'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    category = models.CharField( max_length=50)
    amount = models.DecimalField( max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(choices=TYPE_CHOICE, max_length=20)
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Transactions'