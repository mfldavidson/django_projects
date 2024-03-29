from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template.loader import render_to_string

from cats.models import Cat, Breed
from cats.forms import CatForm, BreedForm

class CatView(LoginRequiredMixin, View) :
    def get(self, request):
        bc = Breed.objects.all().count();
        cl = Cat.objects.all();

        ctx = { 'breed_count': bc, 'cat_list': cl };
        return render(request, 'cats/cat_list.html', ctx)

class BreedView(View) :
    def get(self, request):
        bl = Breed.objects.all();
        ctx = { 'breed_list': bl };
        return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all_cats')
    def get(self, request) :
        form = BreedForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = BreedForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)

class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    success_url = reverse_lazy('cats:all_cats')
    template = 'cats/breed_form.html'
    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance = breed)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:all_cats')
    template = 'cats/breed_confirm_delete.html'

    def get(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = { 'breed': breed }
        return render(request, self.template, ctx)

    def post(self, request, pk) :
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)

# Take the easy way out on the main table
class CatCreate(LoginRequiredMixin,CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all_cats')
