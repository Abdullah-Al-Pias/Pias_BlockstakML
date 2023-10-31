from django.urls import path
from .views import dt_recommender, nb_recommender


urlpatterns = [
    path('api/dt_recommender/', dt_recommender.as_view(), name='dt_recommender'),
    path('api/nb_recommender/', nb_recommender.as_view(), name='nb_recommender'),
]