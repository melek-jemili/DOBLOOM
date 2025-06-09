from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Todo (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    to_be_done_before = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Order by creation date, newest first
        
    

# This model defines a Todo item with fields for title, description, completion status,
# and timestamps for creation and last update. The `__str__` method returns the title of the Todo item,
# and the `Meta` class specifies that Todo items should be ordered by their creation date in descending order.
# This allows for easy retrieval of the most recently created Todo items.
# The `ordering` attribute in the `Meta` class ensures that when querying Todo items,
# they will be returned in the order of their creation date, with the most recent items appearing first.
# This is useful for displaying Todo items in a user interface, where users typically want to see their most recent tasks first.


