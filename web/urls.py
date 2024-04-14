from django.urls import path
from .views import *

urlpatterns = [
    path('', StudentsListView.as_view(), name='home'),
    path('create/', StudentsCreateView.as_view(), name='new_student'),
    path('detail/<int:pk>/', StudentsDetailView.as_view(), name='student_detail'),
    path('update/<int:pk>/', StudentsEditView.as_view(), name='edit_student'),
    path('delete/<int:pk>/', StudentsDeleteView.as_view(), name='delete_student')
]
