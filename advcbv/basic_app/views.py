from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, 
                                  DetailView, CreateView,
                                  UpdateView, DeleteView)
from django.urls import reverse_lazy
from . import models

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'



class SchoolListView(ListView):
    # if you don't provide context_object_name = 'schools'
    # Then it by default give name as Classname_list
    context_object_name = 'schools_list'
    model = models.School
    template_name = 'basic_app/school_list.html'


class SchoolDetailView(DetailView):
    # if you don't provide context_object_name = 'school_detail'
    # Then it by default give name as classname (with first word lowercased)
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'
 
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
