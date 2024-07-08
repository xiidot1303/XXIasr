import datetime
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Sum, F
from base.forms import *
from base.models import SMS, Access, Client, Notes, Profile, Service, Task, Upload, SMStext, telegramPost, subscriptions, Bot_user
from django.db.models.query import Q
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from bot.update import dp, updater
from django.http.response import HttpResponse, FileResponse, Http404
from django.urls import reverse_lazy