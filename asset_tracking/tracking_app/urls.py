from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CompanyViewSet, EmployeeViewSet, DeviceViewSet, DeviceLogViewSet


company_view = CompanyViewSet.as_view({'post': 'create'})
employee_view = EmployeeViewSet.as_view({'post': 'create'})
device_view = DeviceViewSet.as_view({'post': 'create'})
devicelog_view = DeviceLogViewSet.as_view({'get': 'list', 'post': 'create'})

urlpatterns = [
    path('company/', company_view),
    path('employee/', employee_view),
    path('device/', device_view),
    path('devicelog/', devicelog_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)
