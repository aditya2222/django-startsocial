from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import reverse
from django.views.generic import *
from groups.models import Group,GroupMember
# Create Groups Here

class CreateGroupView(CreateView):
    fields = ('name','description')
    model = Group

class SingleGroup(DetailView):
    model=Group

class ListGroups(ListView):
    model=Group

