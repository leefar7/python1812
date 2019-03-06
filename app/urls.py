from django.conf.urls import url

from app import views

urlpatterns= [

    url(r'^home/', views.home,name='home'),
    url(r'^market/', views.market,name='market'),

]