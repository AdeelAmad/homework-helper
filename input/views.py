from input import models
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.

class AnswerCreateView(LoginRequiredMixin, CreateView):
    model = models.answer
    permission_required = ('answer.can_create')
    fields = ['class_for', 'assignment_name', 'content']

class AnswerDetailView(DetailView):
    model = models.answer

class AnswerAPHGListView(ListView):



    queryset = models.answer.objects.filter(approval=True).filter(class_for='APHG')
    template_name = 'input/aphg.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

class AnswerGEOListView(ListView):

    queryset = models.answer.objects.filter(approval=True).filter(class_for='GEO')
    template_name = 'input/geometry.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

class AnswerENG1ListView(ListView):

    queryset = models.answer.objects.filter(approval=True).filter(class_for='English 1')
    template_name = 'input/english1.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

class AnswerSPAN1ListView(ListView):

    queryset = models.answer.objects.filter(approval=True).filter(class_for='Spanish 1')
    template_name = 'input/spanish1.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

class AnswerFRE1ListView(ListView):

    queryset = models.answer.objects.filter(approval=True).filter(class_for='French 1')
    template_name = 'input/french1.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

class AnswerALG1ListView(ListView):

    queryset = models.answer.objects.filter(approval=True).filter(class_for='Algebra 1')
    template_name = 'input/algebra1.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'



class AnswerListApproveView(ListView):

    queryset = models.answer.objects.exclude(approval=True)
    template_name = 'input/approve.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'

@permission_required('answer.can_create')
def staffHome(request):
    return render(request, 'input/shome.html')

def approveAns(request):
    return render(request, 'input/approve.html')

class AnswerApproveView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.answer
    fields = ['class_for', 'assignment_name', 'content', 'approval']

    permission_required = ('answer.can_approve')

class UpdateList(ListView):
    model = models.update
    template_name = 'users/updates.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'updates'
    ordering = ['-date']