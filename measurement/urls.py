from django.urls import path

from measurement.views import SensorListView, MeasurementCreateView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
]