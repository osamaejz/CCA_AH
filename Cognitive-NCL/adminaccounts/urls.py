# -*- coding: utf-8 -*-
from django.urls import include, path
from . import views


app_name = "adminaccounts"
urlpatterns = [
    path('', views.index, name='index'),


    path('table/', views.tables_view, name='table'),
    path('download/', views.download_pdf, name='download_pdf'),
    path('email/', views.send_email, name='semd_email'),
    path('pdf_list/', views.pdf_list, name='pdf_list'),
    path('adminaccounts/pdf/<path:file_path>/',
         views.view_pdf, name='view_pdf'),
]
