from django.urls import path,include
from rest_framework.routers import DefaultRouter    #2
from profiles_api import views  #2

router = DefaultRouter()    #2
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')   #2
router.register('profile',views.UserProfileViewSet) #3
router.register('feed',views.UserProfileFeedViewSet) #4

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))  #2
]


# ลองกำหนด รับค่า localhost:8000
#path('', views.Home.index,name='index'),
