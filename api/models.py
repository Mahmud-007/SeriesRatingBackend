from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Series(models.Model):
    title=models.CharField(max_length=200);
    genre=models.CharField(max_length=200);
    description=models.TextField(max_length=1000);

    def rated_times(self):
        rating=Rating.objects.filter(series=self)
        return len(rating)
    def avg_rating(self):
        sum=0
        ratings=Rating.objects.filter(series=self)
        len_rating=len(ratings)
        for i in ratings:
            sum+=i.stars
        if (len_rating):
            return sum/len_rating
        else:
            return 0

class Rating(models.Model):
    series=models.ForeignKey(Series, on_delete=models.CASCADE);
    user=models.ForeignKey(User, on_delete=models.CASCADE);
    stars=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)])
    class Meta:
        unique_together=(('user', 'series'))
        index_together=(('user', 'series'))