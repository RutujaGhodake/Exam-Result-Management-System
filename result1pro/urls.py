
"""regpro URL Configuration

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
from result1app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login,name='Login'),
    path('data',views.generatedata,name='data'),
    path('hdata',views.generatehsc,name='hdata'),
    path('ddata',views.generatedegree,name='ddata'),
    path('d2data', views.generatedegree2, name='d2data'),
    path('d3data', views.generatedegree3, name='d3data'),
    path('bdata',views.generatebtech,name='bdata'),
    path('b2data', views.generatebtech2, name='b2data'),
    path('b3data', views.generatebtech3, name='b3data'),
    path('b4data', views.generatebtech4, name='b4data'),
    path('signup',views.signup,name='signup'),
    path('Logout',views.Logout,name='Logout'),
    path('ssc',views.ssc,name='ssc'),
    path('result/<d>',views.result,name='result'),
    path('hsc', views.hsc, name='hsc'),
    path('hscresult/<d>',views.hscresult,name='hscresult'),
    path('degree',views.degree,name='degree'),
    path('degreeresult/<d>',views.degreeresult,name='degreeresult'),
    path('degree2',views.degree2,name='degree2'),
    path('degree2result/<d>',views.degree2result,name='degree2result'),
    path('degree3', views.degree3, name='degree3'),
    path('degree3result/<d>', views.degree3result, name='degree3result'),
    path('btech',views.btech,name='btech'),
    path('btechresult/<d>',views.btechresult,name='btechresult'),
    path('btech2',views.btech2,name='btech2'),
    path('btech2result/<d>',views.btech2result,name='btech2result'),
    path('btech3',views.btech3,name='btech3'),
    path('btech3result/<d>',views.btech3result,name='btech3result'),
    path('btech4',views.btech4,name='btech4'),
    path('btech4result/<d>',views.btech4result,name='btech4result'),
    path('main',views.mainpage,name='mainpage')
]
