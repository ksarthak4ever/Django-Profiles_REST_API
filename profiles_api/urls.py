from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter() #https://www.django-rest-framework.org/api-guide/routers/
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet) #registering with router so djangorestframework will take care of creating all the urls.WHhile registering a ModelsViewSet  we dont need to specify a base_name as django can automatically figure it out by looking at the serializer thats registered on our viewset
router.register('login',views.LoginViewSet, base_name='login')
router.register('feed',views.UserProfileFeedViewSet) #since it's a model viewset hence no need for base_name


urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),
	path('',include(router.urls))
]