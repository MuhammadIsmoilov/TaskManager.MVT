from django.shortcuts import render
from django.views import generic
from .models import Students
from django.urls import reverse_lazy
# Create your views here.


class StudentsListView(generic.ListView):
    model = Students
    template_name = 'index.html'

class StudentsCreateView(generic.CreateView):
    model = Students
    template_name = 'create_student.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class StudentsDetailView(generic.DetailView):
    model = Students
    template_name = 'detail.html'

class StudentsEditView(generic.UpdateView):
    model = Students
    template_name = 'post_edit.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class StudentsDeleteView(generic.DeleteView):
    model = Students
    template_name = 'student_delete.html'
    success_url = reverse_lazy('home')

       
    
