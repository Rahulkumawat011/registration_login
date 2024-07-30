from django.db import models

# Create your models here.

class TestField(models.Model):
    id= models.AutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')
    # big_id = models.BigAutoField(serialize = False,verbose_name ='ID')
    big_int = models.BigIntegerField(serialize = False, verbose_name ='ID')
    binary_field = models.BinaryField(null=True)
    boolean_field = models.BooleanField(null=True, blank=True)
    char = models.CharField(max_length=255,null=True)
    date_fields = models.DateField(null=True)
    datetime = models.DateTimeField(null=True)
    decimal = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    duration = models.DurationField(null=True)
    email = models.EmailField(null=True)
    file = models.FileField(null=True)
    float = models.FloatField(null=True)
    image = models.ImageField(null=True)
    integer = models.IntegerField(null=True)
    ipaddress = models.GenericIPAddressField(null=True)
    # null_boolean = models.NullBooleanField(null=True,blank=True)
    positive_integer = models.PositiveIntegerField(null=True)
    positive_small_integer = models.PositiveSmallIntegerField(null=True)
    slug_fields = models.SlugField(max_length=200, null=True)
    small_integer = models.SmallIntegerField(null=True)
    Text_fields = models.TextField(null=True)
    time_field = models.TimeField(null=True)
    url = models.URLField(null=True)
    uuid = models.UUIDField(null=True)

# first letter small in class wrong
class SchoolManagementSystam(models.Model):
    name = models.CharField(max_length=255,null=True)
    opening = models.DateTimeField(null=True)
    Principal = models.IntegerField(null=True)
    teaches = models.IntegerField(null=True)
    students = models.IntegerField(null=True)
    building = models.IntegerField(null=True)
    campus = models.IntegerField(null=True)
    bus = models.IntegerField(null=True)
    about = models.TextField(null=True)
    time = models.TimeField(null=True)
    website = models.URLField(null=True)





class Staff(models.Model):
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    mobile_number = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    # qualification = models.CharField(null=True)
    experience = models.FloatField(null=True)
    salary = models.IntegerField(null=True)
    about = models.TextField(null=True)
    # teaches = models.CharField(null=True)



class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    mobile_number = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    class_name = models.IntegerField(null=True)
    roll_no = models.IntegerField(null=True)
    subject = models.CharField(max_length=100, null=True)
    fees = models.IntegerField(null=True)
    standard = models.IntegerField(null=True)


class User(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone_number = models.IntegerField(null=True)
    age = models.IntegerField(null=True)


class Student(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone_number = models.IntegerField(null=True)
    age = models.IntegerField(null=True)








