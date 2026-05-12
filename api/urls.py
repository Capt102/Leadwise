
from django.urls import path
from api.views import LeadListCreateView,LeadRetrieveUpdateDestryView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns=[

    path("leads/",LeadListCreateView.as_view()),
    path("leads/<int:pk>/",LeadRetrieveUpdateDestryView.as_view()),
    path("token/",ObtainAuthToken.as_view()),


]