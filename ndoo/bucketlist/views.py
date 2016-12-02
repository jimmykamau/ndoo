from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from bucketlist.forms import BucketListForm, BucketListItemForm
from bucketlist.models import BucketList, BucketListItem


class IndexView(TemplateView):
    """Handles the index URL, which is the authentication page"""

    def get(self, request):
        return render(request, "index.html")


class DashboardView(LoginRequiredMixin, TemplateView):
    """Handles the dashboard homepage"""
    login_url = '/login'

    def get(self, request):
        bucketlists = BucketList.objects.filter(created_by=request.user)
        context = {'bucketlists': bucketlists}
        return render(request, "dashboard.html", context)


class CreateBucketlistView(LoginRequiredMixin, View):

    def post(self, request):
        form = BucketListForm(request.POST)
        if form.is_valid():
            bucketlist = form.save(commit=False)
            bucketlist.created_by = request.user
            bucketlist.save()
            messages.success(request, 'Ndoo created successfully')
            return JsonResponse({'message': 'success'})
        else:
            return JsonResponse({'message': form.errors})


class EditBucketlistView(LoginRequiredMixin, View):

    def post(self, request):
        try:
            instance = BucketList.objects.get(
                pk=request.POST.get('id'), created_by=request.user)
            form = BucketListForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ndoo edited successfully')
                return JsonResponse({'message': 'success'})
            else:
                return JsonResponse({'message': form.errors})
        except ObjectDoesNotExist:
            return JsonResponse({'message': "Object Doesn't Exist"})


class DeleteBucketlistView(LoginRequiredMixin, View):

    def post(self, request):
        try:
            instance = BucketList.objects.get(
                pk=request.POST.get('id'), created_by=request.user)
            instance.delete()
            messages.success(request, 'Ndoo deleted successfully')
            return JsonResponse({'message': 'success'})
        except ObjectDoesNotExist as e:
            return JsonResponse({'message': "Object Doesn't Exist", 'log': e})


class CreateBucketlistItemView(LoginRequiredMixin, View):

    def post(self, request, id):
        print(id)
        form = BucketListItemForm(request.POST)
        if form.is_valid():
            try:
                bucketlist = BucketList.objects.get(
                    pk=int(id))
                bucketlist_item = form.save(commit=False)
                try:
                    bucketlist_item.done = True if request.POST.done == 'on' \
                        else False
                except AttributeError:
                    bucketlist_item.done = False
                bucketlist_item.bucketlist_id = bucketlist
                bucketlist_item.save()
                messages.success(request, 'Ndoo item created successfully')
                return JsonResponse({'message': 'success'})
            except ObjectDoesNotExist as e:
                return JsonResponse(
                    {'message': "Object Doesn't Exist", 'log': e})
        else:
            return JsonResponse({'message': form.errors})


class EditBucketlistItemView(LoginRequiredMixin, View):

    def post(self, request, item_id):
        try:
            instance = BucketListItem.objects.get(
                pk=item_id)
            form = BucketListItemForm(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                messages.success(request, 'Ndoo item edited successfully')
                return JsonResponse({'message': 'success'})
            else:
                return JsonResponse({'message': form.errors})
        except ObjectDoesNotExist:
            return JsonResponse({'message': "Object Doesn't Exist"})


class DeleteBucketlistItemView(LoginRequiredMixin, View):

    def post(self, request, item_id):
        try:
            instance = BucketListItem.objects.get(
                pk=item_id)
            instance.delete()
            messages.success(request, 'Ndoo item deleted successfully')
            return JsonResponse({'message': 'success'})
        except ObjectDoesNotExist as e:
            return JsonResponse({'message': "Object Doesn't Exist", 'log': e})
