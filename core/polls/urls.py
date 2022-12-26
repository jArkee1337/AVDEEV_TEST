from django.urls import path, include
from .views import *

urlpatterns = [
    path("", index, name='polls'),
    path("questions/<int:question_id>/", question, name='one_question'),
    path("finish/<int:collection_id>/", finish, name='finish'),
    path("<int:collection_id>/", list_of_questions, name='questions'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]
