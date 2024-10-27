from django.views.generic import ListView
from django.shortcuts import render
from . import models

class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
