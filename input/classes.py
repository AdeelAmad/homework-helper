from django.views.generic import DetailView
from input import models
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import View
from django.shortcuts import redirect


def DetailViewFunction(request, pk):

    if request.user.profile.tokens_have < 1:
        redirect('home')
    else:
        DetailViewModified()

class DetailViewModified(DetailView, SingleObjectMixin, View):

    def get(self, request, *args, **kwargs):
        self.object = request.user.profile

        if self.object.tokens_have < 1:
            return redirect('home')
        else:
            tokens = self.object.tokens_have
            tokens = tokens - 1
            self.object.tokens_have = tokens
            self.object.save()
            return super(DetailView, self).get(request, *args, **kwargs)

    model = models.answer