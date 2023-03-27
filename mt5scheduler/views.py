from rest_framework import generics
from .models import AccountsModel
from .serializers import CreateAccountSerializer
from .serializers import ViewAccountSerializer
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to the API")

class CreateAccountViewSet(generics.ListCreateAPIView):
    queryset = AccountsModel.custom_objects.all()
    serializer_class = CreateAccountSerializer

class ListAccountsViewSet(generics.ListAPIView):
    queryset = AccountsModel.custom_objects.all()
    serializer_class = ViewAccountSerializer

class RetrieveAccountsViewSet(generics.RetrieveAPIView):
    queryset = AccountsModel.custom_objects.all()
    serializer_class = ViewAccountSerializer

class DestroyAccountsViewSet(generics.DestroyAPIView):
    queryset = AccountsModel.custom_objects.all()
    serializer_class = ViewAccountSerializer

class UpdateAccountsViewSet(generics.UpdateAPIView):
    queryset = AccountsModel.custom_objects.all()
    serializer_class = ViewAccountSerializer