from django.conf.urls import url,include
from .views import Suggestion_View,Home
from .import views

urlpatterns=[

   url(r'^$',views.Home,name='Home'),
url(r'^fillform$',views.Suggestion_View,name='fillform'),
url(r'^signup/$',views.signup,name='signup')

]