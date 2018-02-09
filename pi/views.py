from __future__ import absolute_import, division, print_function, unicode_literals

import uuid

from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from rest_framework import routers, serializers, viewsets
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import permissions

from chartit import DataPool, Chart

# from channels.forms import ChannelForm
# from channels.models import Channel
# from datas.models import Data
from pi.models import PiData, PiConfig
from datas.permissions import IsOwnerOrReadOnly
from datas.serializers import DataSerializer
from iotdashboard.debug import debug
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class DataQueryList(TemplateView):
    """
    All data list for template.
    """
    template_name = "back/pi_data.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        pi = True

        datas = PiData.objects.all().order_by('-created_date')[:100]
        config = PiConfig.objects.filter(user=request.user)

        return render(request, self.template_name, locals())
