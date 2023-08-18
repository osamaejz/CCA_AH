# -*- coding: utf-8 -*-

from django.urls import include, path
from . import views

app_name = "useraccounts"
urlpatterns = [
    # path('', views.signuppage, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('student/', views.student, name='student'),
    path('employee/', views.employee, name='employee'),
    path('register/', views.registerPage, name="registeruser"),
    path('', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('loginAPI/', views.loginAPI, name="loginAPI"),
    path('logout/', views.logoutUser, name="logout"),

    path('assessment/', views.assessment, name="assessment"),
    path('tmt/', views.tmt, name="tmt"),

    path('processDigitSpan/', views.processDigitSpan, name="processDigitSpan"),
    path('processSymmetrySpan/', views.processSymmetrySpan,
         name="processSymmetrySpan"),
    path('processVisualArray/', views.processVisualArray,
         name="processVisualArray"),

    path('results/', views.results, name="results"),

    path('table/', views.results, name="table")
]
