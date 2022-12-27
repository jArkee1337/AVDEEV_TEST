from django.urls import path
from polls import views

urlpatterns = [
    path("", views.index, name='polls'),
    path("questions/<int:question_id>/", views.question, name='one_question'),
    path("finish/<int:collection_id>/", views.finish, name='finish'),
    path("<int:collection_id>/", views.list_of_questions, name='questions'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
]
