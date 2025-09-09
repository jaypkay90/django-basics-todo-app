from django.urls import path
from . import views


urlpatterns = [
    path('addTask', views.addTask, name='addTask'),
    path('completeTask/<int:task_id>', views.completeTask, name='completeTask'),
    path('deleteTask/<int:task_id>', views.deleteTask, name='deleteTask'),
    path('markTaskUndone/<int:task_id>', views.markTaskUndone, name='markTaskUndone'),
    path('editTask/<int:task_id>', views.editTask, name='editTask'),
    # path('updateTask/<int:task_id>', views.updateTask, name='updateTask'),
]
