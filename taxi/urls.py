from django.urls import path

from .views import (index,
                    ManufacturerListView,
                    CarListView,
                    DriverListView,
                    CarDetailView,
                    DriverDetailView)

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",
         ManufacturerListView.as_view(),
         name="manufacturers-list"),
    path("cars/", CarListView.as_view(),
         name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(),
         name="car-detail"),
    path("drivers/", DriverListView.as_view(),
         name="drive-list"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(),
         name="drive-detail"),

]

app_name = "taxi"
