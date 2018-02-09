from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify as djslugify
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import hashlib, random

# Create your models here.


class PiData(models.Model):
    """
    """
    user           		= models.ForeignKey('auth.User', related_name='ownerpidata')
    temperature         = models.CharField(_('Temperature'), max_length=10, null=True, blank=False)
    humidity         	= models.CharField(_('Humidity'), max_length=10, null=True, blank=False)
    day_night         	= models.CharField(_('Day night'), max_length=10, null=True, blank=False)
    moisture         	= models.CharField(_('Moisture'), max_length=10, null=True, blank=False)
    light_lux         	= models.CharField(_('Light lux'), max_length=10, null=True, blank=False)
    relay_state         = models.CharField(_('Relay state'), max_length=10, null=True, blank=False)
    remote_address  	= models.CharField(_('Ip address'), max_length=255)
    created_date        = models.DateTimeField(_('Created date'), auto_now=True)

    def __str__(self):
        return self.remote_address

class PiConfig(models.Model):
	"""
	"""
	user 				= models.ForeignKey('auth.User', related_name='ownerpiconfig')
	remote_address 		= models.CharField(_('Ip address'), max_length=255)
	last_login 			= models.DateTimeField(_('Last login'), auto_now=True)

	def __str__(self):
		return self.remote_address