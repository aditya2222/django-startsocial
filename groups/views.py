from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import *
from groups.models import Group,GroupMember
from django.shortcuts import get_object_or_404

# Create Groups Here

class CreateGroupView(CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(DetailView):
    model=Group

class ListGroups(ListView):
    model=Group

class JoinGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))
        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except:
            messages.warning(self.request,'Warning! Already A Member!')
        else:
            messages.success(self.request,'You Are Now A Member!')

        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):

        try:
            membership=GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except:
            messages.warning(self.request,'Sorry You are not a part of this group!')
        else:
            membership.delete()
            messages.success(self.request,'You have left the group')
        return super().get(request,*args,**kwargs)

