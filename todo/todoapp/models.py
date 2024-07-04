from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todo(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    todo_name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.todo_name
    



