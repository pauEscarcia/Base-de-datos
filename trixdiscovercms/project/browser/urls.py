
from django.conf.urls import url, patterns
import views

#urlpatterns = [
#    url(r'^$', views.index, name='index'),
#]

urlpatterns = patterns('',
    url(r'^latest/', views.latest_category, name='latest_category'),
)