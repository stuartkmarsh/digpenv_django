from django.conf.urls import patterns, include, url

urlpatterns = patterns('app.views',
    url(r'^$', 'home', name='home'),
    url(r'^item_detail/(?P<item_id>\d+)/$', 'item_detail', name='item_detail'),
    url(r'^upvote/(?P<item_id>\d+)/$', 'upvote', name='upvote')
)