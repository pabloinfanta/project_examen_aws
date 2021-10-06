from django.db import models
from apps.app_users.models import User
from datetime import datetime
# Create your models here.

class TravelManager(models.Manager):
  def basic_validator(self, postData):
    errors = {}
    if len(postData['destination']) < 2:
      errors["destination"] = "Travel item should be at least 3 characters"
    if len(postData['desc']) < 1:
      errors["desc"] = "Travel description must be provided"
    if len(postData['start_date']) < 1:
      errors["start_date"] = "Travel start date must be provided"
    elif len(postData['end_date']) < 1:
      errors["end_date"] = "Travel end date must be provided"
    else:
      today = datetime.now().date()
      start_date = datetime.strptime(postData['start_date'], '%Y-%m-%d').date()
      end_date = datetime.strptime(postData['end_date'], '%Y-%m-%d').date()
      if start_date < today or end_date < today :
        errors["start_date"] = "Travel Dates should be future-dated"  
      elif start_date > end_date:
         errors["end_date"] = "Travel Date To should be before the Travel Date From" 
    return errors

# Create your models here.
class Travel(models.Model):
  destination = models.CharField(max_length=255)
  desc = models.TextField()
  start_date = models.DateField()
  end_date = models.DateField()
  owner_user = models.ForeignKey(User, related_name="my_travels", on_delete = models.CASCADE)
  users = models.ManyToManyField(User, related_name="travels")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = TravelManager() 