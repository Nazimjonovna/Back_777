from django.db import models
from django.core.validators import RegexValidator
from rest_framework.validators import ValidationError
from rest_framework.response import Response

# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=20, unique=True)
    parol = models.CharField(max_length=9)


    def __str__(self):
        return self.username



class User(models.Model):
    ism = models.CharField(max_length=50)
    phone_regex = [RegexValidator(regex="d{0,9}", message="Iltimos davom eting: +998XXXXXXXXX"),]
    phone = models.CharField(max_length=20, validators=phone_regex, unique=True)
    adress = models.TextField()

    def __str__(self):
        return self.ism


def validate_image(self, image):
    product = Product.objects.filter(image = image)
    if product.exists():
        raise ValidationError('Bu rasm bor')
    else:
        if image.endswith(".png") or image.endswith(".jpg") or image.endswith(".pdf"):
            return image
        else:
            return Response("Rasm formati mos emas")


class Product(models.Model):
    name = models.CharField(max_length=23)
    image = models.FileField(upload_to='rasmlar', validators=[validate_image])
    hajm = models.IntegerField()
    cost = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE) #id

    def __str__(self):
        return self.name














