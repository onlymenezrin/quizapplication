from django.urls import path
from quizweb import views

urlpatterns=[
    path("register",views.SignUpView.as_view(),name="signup"),
    path("login",views.SignInView.as_view(),name="signin"),
    path("home",views.HomeView.as_view(),name="home"),
    path("quizes/home",views.QuizHomeView.as_view(),name="quiz-home"),
    path("questions/all/<str:cat>/<str:mode>/",views.QuestionListView.as_view(),name="question-list"),
    path("quiz/record/",views.QuizRecordView.as_view(),name="quiz-record"),

]