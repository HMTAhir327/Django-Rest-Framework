from django.urls import path,include
from .views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV


urlpatterns = [
    path('list/', WatchListAV.as_view() ,name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view() ,name='movie-detail'),
    path('stream/', StreamPlatformAV.as_view() ,name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view() ,name='streamplatform-detail'),
]


# before apiview (5. serializers requests and status code)

# from .views import movie_list,movie_detail

# urlpatterns = [
#     path('list/', movie_list,name='movie-list'),
#     path('<int:pk>', movie_detail,name='movie-detail')
# ]
