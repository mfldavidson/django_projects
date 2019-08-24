from django.shortcuts import render
from django.views import View, generic
from django.conf import settings
from django.urls import reverse_lazy
from ads.models import *
from ads.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class AdsListView(OwnerListView):
    model = Ad
    template_name = "ad_list.html"

class AdsDetailView(OwnerDetailView):
    model = Ad
    template_name = "ad_detail.html"

class AdsCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ad_form.html"
    success_url = reverse_lazy('ads')

class AdsUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    template_name = "ad_form.html"
    success_url = reverse_lazy('ads')

class AdsDeleteView(OwnerDeleteView):
    model = Ad
    template_name = "ad_delete.html"
    success_url = reverse_lazy('ads')
