from datetime import timezone

from django.db import models

# Create your models here.
from django.urls import reverse

class Student(models.Model):
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.CharField(max_length=50)
    d = models.CharField(max_length=50)
    start_date = models.DateField('place', null=True, blank=True)
    end_date = models.DateField('place', null=True, blank=True)
    image_profile = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)



class User(models.Model):
    firstname = models.CharField(max_length=50)
    midlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    password = models.CharField(max_length=50)
    confoirmpassword = models.CharField(max_length=50)
    date_a= models.DateField('place', null=True, blank=True)
    def __str__(self):
        return self.firstname

class Book(models.Model):
    Auther=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=50)
    # def __str__(self):
    #     return self.subject

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    # def get_absolute_url(self):
    #     """Returns the url to access a particular author instance."""
    #     return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name},{self.date_of_death}'

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin."""
    #     return ', '.join(genre.name for genre in self.genre.all()[:3])
    #
    # # display_genre.short_description = 'Genre'