from django.urls import path
from .views import dashboard_admin, dashboard_farmer, login, register,logout_view
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("logout/", logout_view, name="logout"),
    path("admin-dashboard/" , dashboard_admin , name="dashboard_admin"),
    path("farmer-dashboard/" , dashboard_farmer , name="dashboard_farmer"),
]
