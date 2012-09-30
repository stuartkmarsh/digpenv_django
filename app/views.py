from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from app.models import Item, UserVote

def home(request):
    items = Item.objects.all()
    
    return render_to_response('app/home.html', {'items':items}, context_instance=RequestContext(request))
    
def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    return render_to_response('app/item_detail.html', {'item':item}, context_instance=RequestContext(request))
  
@login_required
def upvote(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    
    user_votes = UserVote.objects.filter(user=request.user, item=item)
    
    if not user_votes:
        item.votes += 1
        item.save()
        
        UserVote.objects.create(user=request.user, item=item)
    
    return HttpResponseRedirect('/')    
    
    
    
    
