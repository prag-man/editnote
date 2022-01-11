"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('about', views.about, name='about'),
    # path('hello', views.hello, name='hello'),
    # path('capitalize' ,views.capitalize, name='cap'),
    # path('capitalizefirst', views.capitalizefirst, name='cap1'),
    # path('smallcase' ,views.smallcase, name='small'),
    # path('removepunc', views.removepunc, name='remove punc'),
    # path('spaceremove' ,views.spaceremove, name='space remove'),
    # path('charcount' ,views.charcount, name='charcount'),
    # path('name' ,views.name, name='name'),
    # path('tell' ,views.tell, name='tell'),
    path('analyzer' ,views.analyzer, name='analyze'), # the first param declares site add. i.e page in website, second param is the name of func in views.py, third param is the name of this element
    path('rando', views.rando, name='random'),
    path('rando/tasks', views.tasks, name='tasks'),
    path('rando/sites', views.sites, name='sites'),
]
