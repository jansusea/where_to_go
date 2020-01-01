from django.urls import path

from . import views


app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('house', views.house, name='house'),
    path('work', views.work, name='work'),
    path('test', views.test, name='test'),
    path('show', views.show, name='show'),
    path('home', views.home, name='home'),
    path('analysis', views.analysis, name='analysis'),

    # # /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]