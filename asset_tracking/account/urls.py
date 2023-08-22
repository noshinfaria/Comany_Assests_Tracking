from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SignupViewSet, Login

signup_view = SignupViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('signup/', signup_view),
    path('login/', Login.as_view(), name='login'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
