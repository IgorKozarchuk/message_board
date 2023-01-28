from django.urls import path

from .views import HomePageView


urlpatterns = [
	path("", HomePageView.as_view(), name="home"),
]

# Deployed at:
# http://igork.pythonanywhere.com/
