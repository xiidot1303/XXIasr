
from django.urls import path

from base.client_views import singleClient, change_congragulation
from base.upload_views import NotesPage, cancelService, confirmSerivce, editClient, editNote, change_sub_gived, archiveService, editUpload
from base.views.main import *
from base.views import fine, decree
from .user_views import CreateProfile, DeleteProfile, EditProfile, Profiles, ActiveProfile
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
    path("taxi/", TaxiPage, name='taxi'),
    path("ishonchnoma/", IshonchnomaPage, name='ishonchnoma'),
    path("aviakassa/", aviakassaPage, name='aviakassa'),
    path("daromad12/", daromad12Page, name='daromad12'),
    path("taxer/", taxerPage, name='taxer'),
    path("student/", studentPage, name='student'),
    path("mahalla/", mahallaPage, name='mahalla'),


    path("cancel-serivce/<str:pk>", cancelService, name='cancel-service'),
    path("confirm-serivce/<str:pk>", confirmSerivce, name='confirm-service'),
    path("archive-serivce/<int:pk>", archiveService, name='archive-service'),
    path("edit-upload/<int:pk>", editUpload, name='edit-upload'),

    path("client/<str:pk>", singleClient, name='client'),
    path("edit-client/<str:pk>", editClient, name='edit-client'),

    path("notes/", NotesPage, name='notes'),
    path("note/<str:pk>", editNote, name='note'),
    path("sms/", SMSPage, name='sms'),
    path("edit-sms/<str:pk>", editSMS, name='edit-sms'),

    path("users/", Profiles, name="users"),
    path("create-user/", CreateProfile, name='create-user'),
    path("delete-user/<str:pk>", DeleteProfile, name="delete-profile"),
    path("active-user/<str:pk>", ActiveProfile, name="active-profile"),
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
    path('delete-template/<int:pk>/', template_delete, name='delete-template'),
    
    path('keys', keys, name='keys'),
    path('keys/<str:active_type>/', keys, name='keys_by_type'),
    path('keys/change-type/<int:key_pk>/<str:type>/<str:active_type>/', change_key_type, name='change_key_type'),
    path('keys/delete/<int:key_pk>/', delete_key, name='delete_key'),

    path('edit-botuser/<int:pk>/', BotuserEditView.as_view(), name='edit-botuser'),

    path('change-congragulation/<int:client_pk>/<str:status>/', change_congragulation, name='change_congragulation'),

    path('download-ishonchnoma-files/<client_id>/', download_ishonchnoma_files, name='download_ishonchnoma_files'),
    path('download-application-files/<client_id>/', download_application_files, name='download_application_files'),

    path('fetch_keys/<str:key_type>/', fetch_keys, name='fetch_keys'),
    path('change_sub_gived/<str:client_id>/', change_sub_gived, name='change_sub_gived'),

    path('operator', operator, name = 'operator'),
    path('edit-duedate/<int:pk>/', change_duedate, name = 'change_duedate'),

    # fine
    path('fine-list', fine.fine_list, name='fine_list'),
    path('fine-create', fine.FineCreateView.as_view(), name='fine_create'),
    path('fine-edit/<int:pk>/', fine.FineEditView.as_view(), name='fine_edit'),
    path('fine-acquitted/<int:pk>/', fine.fine_acquitted, name='fine_acquitted'),

    # decree
    path('decree-list', decree.decree_list, name='decree_list'),
    path('decree-create', decree.DecreeCreateView.as_view(), name='decree_create'),
    path('decree-edit/<int:pk>/', decree.DecreeEditView.as_view(), name='decree_edit'),
    path('decree-receive/<int:pk>/', decree.decree_receive, name='decree_receive'),
    path('decree-complete/<int:pk>/', decree.DecreeCompleteView.as_view(), name='decree_complete'),
    path('decree-check/<int:pk>/<str:status>/', decree.decree_check, name='decree_check'),
    path('decree-download-substance/<int:pk>/', decree.decree_download_substance, name='decree_download_substance'),
]

