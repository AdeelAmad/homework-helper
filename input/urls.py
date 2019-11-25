from django.urls import include, path
from .views import AnswerCreateView, AnswerAPHGListView, staffHome, approveAns, AnswerApproveView, AnswerListApproveView, AnswerGEOListView, AnswerENG1ListView, AnswerFRE1ListView, AnswerSPAN1ListView, AnswerALG1ListView
from .classes import DetailViewModified


urlpatterns = [
    path('answer/new/', AnswerCreateView.as_view(), name='answer-create'),
    path('answer/<int:pk>/', DetailViewModified.as_view(), name='answer-detail'),
    path('aphg/', AnswerAPHGListView.as_view(), name='aphg'),
    path('span1/', AnswerSPAN1ListView.as_view(), name='span1'),
    path('eng1/', AnswerENG1ListView.as_view(), name='eng1'),
    path('fre1/', AnswerFRE1ListView.as_view(), name='fre1'),
    path('geo/', AnswerGEOListView.as_view(), name='geo'),
    path('alg1/', AnswerALG1ListView.as_view(), name='alg1'),
    path('', staffHome, name='staffhome'),
    path('staff/approve', AnswerListApproveView.as_view(), name='approve'),
    path('answer/<int:pk>/update', AnswerApproveView.as_view(), name='answer-update')
]