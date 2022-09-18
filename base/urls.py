
from django.urls import path

from base.client_views import singleClient
from base.upload_views import NotesPage, cancelService, confirmSerivce, editClient, editNote
from base.views import *
from .user_views import CreateProfile, DeleteProfile, EditProfile, Profiles
from data.config import BOT_TOKEN

urlpatterns = [
    path(BOT_TOKEN, bot_webhook),
    path("login/", loginPage, name='login'),
    path("logout/", logoutPage, name='logout'),
    path("", homePage, name="home"),
    path("monitoring/", monitoringPage, name="monitoring"),
    path("upload/", uploadPage, name="upload"),
    path("create-service/", createService, name="create-service"),
    path("edit-service/<str:pk>", editService, name="edit-service"),
    path("delete-service/<str:pk>", deleteService, name="delete-service"),
    path("task/", taskPage, name="task"),
    path("view-task/<str:pk>", viewTaskPage, name="view-task"),
    path("delete-task/<str:pk>", deleteTask, name="delete-task"),
    path("finish-task/<str:pk>", finishTask, name="finish-task"),
    path("history/", serviceHistoryPage, name="history"),
    path("create-client/", createClient, name="create-client"),
    path("yatt/", YaTTPage, name='yatt'),
    path("jismoniy/", JismoniyPage, name='jismoniy'),
    path("governor/", GovernorPage, name='governor'),
    path("yuridik/", YuridikPage, name='yuridik'),
    path("tanirovka/", tanirovkaPage, name='tanirovka'),
    path("avtoraqam/", auctionPage, name='auction'),
    path("auction/", auction2Page, name='auction2'),
    path("teacher/", teachersPage, name='teacher'),


    path("cancel-serivce/<str:pk>", cancelService, name='cancel-service'),
    path("confirm-serivce/<str:pk>", confirmSerivce, name='confirm-service'),

    path("client/<str:pk>", singleClient, name='client'),
    path("edit-client/<str:pk>", editClient, name='edit-client'),

    path("notes/", NotesPage, name='notes'),
    path("note/<str:pk>", editNote, name='note'),
    path("sms/", SMSPage, name='sms'),
    path("edit-sms/<str:pk>", editSMS, name='edit-sms'),

    path("users/", Profiles, name="users"),
    path("create-user/", CreateProfile, name='create-user'),
    path("delete-user/<str:pk>", DeleteProfile, name="delete-profile"),
    path("edit-user/<str:pk>", EditProfile, name="edit-profile"),
    path("delete-client/<str:pk>", deleteClient, name="delete-client"),
    path("telegram/", telegramPage, name="telegram"),

    path('calendar/', calendar, name='calendar'),

    path('static/<str:folder>/<str:file>/', get_file, name='get_file'),
    path('static/templates/<str:folder>/<str:file>/', get_template, name='get_template'),

    path('get-auction-info/<int:client_pk>/<str:type>/', get_auction_info_file, name='get_auction_info_file'),
    path('get-carnumber-info/<int:client_pk>/<str:type>/', get_carnumber_info_file, name='get_carnumber_info_file'),

    path('templates', templates, name='templates'),
    path('edit-template/<int:pk>/', TemplateEditView.as_view(), name='edit-template'),
    path('create-template', TemplateCreateView.as_view(), name='create-template'),
]

