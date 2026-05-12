from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from api.models import Lead
from api.serializers import LeadSerializer

from rest_framework import authentication,permissions

class LeadListCreateView(ListCreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    queryset = Lead.objects.all()

    serializer_class = LeadSerializer

class LeadRetrieveUpdateDestryView(RetrieveUpdateDestroyAPIView):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAdminUser]

    queryset = Lead.objects.all()
    serializer_class = LeadSerializer




