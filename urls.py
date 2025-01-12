"""SPEECH_RECOGNITION_SYSTEM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path,include


from . import views
urlpatterns = [

    path('', views.fpage),
    path('logout', views.logout),
    path('forgot_password', views.forgot_password),
    path('logincode', views.logincode),
    path('admin_home', views.admin_home),
    path('manage_expert', views.manage_expert),
    path('add_expert', views.add_expert),
    path('addex', views.addex),
    path('delete_expert/<int:id>', views.delete_expert),
    path('edit_expert/<int:id>', views.edit_expert),
    path('editex', views.editex),
    path('manage_complaint', views.manage_complaint),
    path('send_reply/<id>', views.send_reply),
    path('sendr', views.sendr),
    path('manage_instructions', views.manage_instructions),
    path('add_instruction', views.add_instruction),
    path('addi', views.addi),
    path('delete_instruction/<id>', views.delete_instruction),
    path('block/<id>', views.block),
    path('unblock/<id>', views.unblock),
    path('view_user', views.view_user),
    path('view_feedback', views.view_feedback),
    path('view_rating', views.view_rating),



    path('expert_home', views.expert_home),
    path('manage_classvideo', views.manage_classvideo),
    path('add_classvideo', views.add_classvideo),
    path('addc', views.addc),
    path('delete_classvideos/<id>', views.delete_classvideos),
    path('manage_exams', views.manage_exams),
    path('add_exam', views.add_exam),
    path('adde', views.adde),
    path('delete_exam/<id>', views.delete_exam),
    path('edit_exam/<id>', views.edit_exam),
    path('editexam', views.editexam),
    path('questionss/<id>', views.questionss),
    path('Add_questions', views.Add_questions),
    path('addq', views.addq),
    path('delete_questions/<id>', views.delete_questions),
    path('Instructions', views.Instructions),

]
