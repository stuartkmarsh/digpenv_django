from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=30)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.name
        
class UserVote(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    
    class Meta:
        unique_together = ('user', 'item')
        
    def __unicode__(self):
        return '%s: %s' % (self.user, self.item)
