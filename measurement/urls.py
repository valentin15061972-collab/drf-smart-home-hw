from django.urls import path

from measurement.views import SensorListView, MeasurementCreateView, SensorDetailView, SensorUpdateView

urlpatterns = [
    path('sensors/', SensorListView.as_view(), name='sensor-list'),
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('sensors/<int:pk>/update/', SensorUpdateView.as_view(), name='sensor-update'),
]