from django.urls import path
from .views import (
    HabitListView,
    HabitDetailView,
    HabitCreateView,
    HabitUpdateView,
    HabitDeleteView,
    PublicHabitListView
)

app_name = 'habits'

urlpatterns = [
    path('list/', HabitListView.as_view(), name='habit_list'),
    path('public/', PublicHabitListView.as_view(), name='public_habit_list'),
    path('create/', HabitCreateView.as_view(), name='habit_create'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit_detail'),
    path('<int:pk>/update/', HabitUpdateView.as_view(), name='habit_update'),
    path('<int:pk>/delete/', HabitDeleteView.as_view(), name='habit_delete'),
]
