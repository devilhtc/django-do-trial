from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
print(views)
urlpatterns = [
# ex: /polls/
	url(r'^$', views.indexView.as_view(), name = 'index'),
    #url(r'^polls/$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^polls/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^polls/(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^polls/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]