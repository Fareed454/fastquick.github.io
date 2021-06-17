from django.db import models
from django.core.exceptions import ValidationError 
# Create your models here.

def check_Email_validations(value):
    if "@gmail.com" is value:
        return value
    elif "@outlook.com" is value:
        return value
    elif "@yahoo.com" is value:
        return value
    elif "@hotmail.com" is value:
        return value
    else:
        raise ValidationError("Do Not Matche Our Validation")

class Gmail_data(models.Model):
    mail = models.EmailField(
        null = False,
        blank = False,
        max_length = 20,
        validators = [check_Email_validations]
    )

    def __str__(self):
        return self.mail