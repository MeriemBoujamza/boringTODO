from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from .models import Task
from django.urls import reverse_lazy
# Create your views here.
def home(request):
    return render(request,"list_app/base.html")

class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title']
    success_url = '/home/mylist'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CreateTask, self).form_valid(form)

    def get_context_data(self, **kwargs):
            kwargs['tasks'] = Task.objects.filter(owner = self.request.user)
            return super(CreateTask, self).get_context_data(**kwargs)

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home')
    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(DeleteTask, self).form_valid(form)

  
#TODO: base.html is done u should work on the first list.html