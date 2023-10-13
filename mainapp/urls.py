from mainapp.views import UserRegistrationView, PostView, CommentView, PostUserView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
   
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostView)
router.register('comments', CommentView)
router.register('post_user', PostUserView)
urlpatterns = [
    path('registration/', UserRegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

urlpatterns += router.urls