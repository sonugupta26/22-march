from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register', views.register, name='register'),
    
]



# app_name='quizapp'

# urlpatterns = [
#     path('', home, name='home'),
    
# ]


# app_name="quiz"

# urlpatterns = [
#     path("", home, name="home"),
#     path("take-quiz/<int:courseid>/", take_quiz, name="take_quiz"),
# ]
