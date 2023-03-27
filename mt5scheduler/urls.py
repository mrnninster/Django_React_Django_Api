from django.urls import path
from . import views

app_name = "mt5scheduler"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.CreateAccountViewSet.as_view(), name="create"),
    path("accounts/", views.ListAccountsViewSet.as_view(), name="list"),
    path("account/<int:pk>", views.RetrieveAccountsViewSet.as_view(), name="retrieve"),
    path("account/delete/<int:pk>", views.DestroyAccountsViewSet.as_view(), name="delete"),
    path("account/update/<int:pk>", views.UpdateAccountsViewSet.as_view(), name="update"),
]