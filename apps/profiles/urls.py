from django.urls import URLPattern, path

from.views import (AgentListAPIView, GetProfileAPIView, TopAgentsListAPIView, UpdateProfileAPIView)

urlpatterns = [
    path('me/', GetProfileAPIView.as_view(), name='get_profile'),
    path('update/<strLusername>/', UpdateProfileAPIView.as_view(), name='update_view'),
    path('agents/all/', AgentListAPIView.as_view(), name='all-agents'),
    path('top-agents/all/', TopAgentsListAPIView.as_view(), name='top-agents'),
]