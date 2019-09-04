from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from autos.models import *
from ads.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from autos.forms import *

class AutosListView(OwnerListView):
    model = Auto
    template_name = "autos/auto_list.html"

    def get(self, request) :
        auto_list = Auto.objects.all()
        ctx = {'auto_list' : auto_list}
        return render(request, self.template_name, ctx)

class AutosDetailView(OwnerDetailView):
    model = Auto
    template_name = "autos/auto_detail.html"

    def get(self, request, pk) :
        auto = Auto.objects.get(id=pk)
        comments = Comment.objects.filter(auto=auto).order_by('-updated_at').all()
        comment_form = CommentForm()
        context = { 'auto' : auto, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

# replaced this view with other view below
# class AutosCreateView(OwnerCreateView):
#     model = Auto
#     fields = ['title', 'price', 'text']
#     template_name = "auto_form.html"
#     success_url = reverse_lazy('all_autos')

class AutosCreateView(LoginRequiredMixin, View):
    template = 'autos/auto_form.html'
    success_url = reverse_lazy('all_autos')
    def get(self, request, pk=None) :
        form = CreateForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Autod owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)

# replaced this view with other view below
# class AutosUpdateView(OwnerUpdateView):
#     model = Auto
#     fields = ['title', 'price', 'text']
#     template_name = "auto_form.html"
#     success_url = reverse_lazy('all_autos')

class AutosUpdateView(LoginRequiredMixin, View):
    template = 'autos/auto_form.html'
    success_url = reverse_lazy('all_autos')
    def get(self, request, pk) :
        auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
        form = CreateForm(instance=auto)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        auto = get_object_or_404(Auto, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=auto)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        auto = form.save(commit=False)
        auto.save()

        return redirect(self.success_url)

class AutosDeleteView(OwnerDeleteView):
    model = Auto
    template_name = "autos/auto_delete.html"
    success_url = reverse_lazy('all_autos')

# views for managing comments on autos
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        a = get_object_or_404(Auto, id=pk)
        comment_form = CommentForm(request.POST)

        comment = Comment(text=request.POST['comment'], owner=request.user, auto=a)
        comment.save()
        return redirect(reverse_lazy('auto_detail', args=[pk]))

class CommentUpdateView(OwnerUpdateView):
    model = Comment
    template_name = "autos/comment_update.html"
    model = Auto
    fields = ['text']
    template_name = "comment_update.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        auto = self.object.auto
        return reverse_lazy('auto_detail', args=[auto.id])

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "autos/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        auto = self.object.auto
        return reverse_lazy('auto_detail', args=[auto.id])

# # https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.db.utils import IntegrityError
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AddFavoriteView(LoginRequiredMixin, View):
#     def post(self, request, pk) :
#         print("Autod PK",pk)
#         a = get_object_or_404(Auto, id=pk)
#         fav = Fav(user=request.user, auto=a)
#         try:
#             fav.save()  # In case of duplicate key
#         except IntegrityError as e:
#             pass
#         return HttpResponse()
#
# @method_decorator(csrf_exempt, name='dispatch')
# class DeleteFavoriteView(LoginRequiredMixin, View):
#     def post(self, request, pk) :
#         print("Delete PK",pk)
#         a = get_object_or_404(Auto, id=pk)
#         try:
#             fav = Fav.objects.get(user=request.user, auto=a).delete()
#         except Fav.DoesNotExist as e:
#             pass
#
#         return HttpResponse()
