from http import server
import os
from unittest.mock import DEFAULT
import uuid
import logging

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _ 


#################################
# mt5scheduler -> models Logger #
#################################

# ------- Configuring Logging File -------- #

# Logger For Log File
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Log File Logging Format
formatter = logging.Formatter("%(asctime)s:%(levelname)s::%(message)s")

# Create Log Folder and File
log_folder_name = "mt5scheduler/logs"
log_file_name = "models.log"
os.makedirs(log_folder_name, exist_ok=True)
log_file_path = f"{log_folder_name}/{log_file_name}"

# Log File Handler
Log_File_Handler = logging.FileHandler(log_file_path)
Log_File_Handler.setLevel(logging.DEBUG)
Log_File_Handler.setFormatter(formatter)

# Stream Handlers
Stream_Handler = logging.StreamHandler()

# Adding The Handlers
logger.addHandler(Log_File_Handler)
logger.addHandler(Stream_Handler)

# Log On START 
logger.debug("")
logger.debug("="*100)
logger.info("Mt5scheduler App -> Models.py :: Logging Active")
logger.debug("")


# CustomUserManager
class CustomUserManager(BaseUserManager):
    
    def add_user(self, server_name, login_id, platform, password, is_superuser=False):
        if is_superuser:
            is_staff = True
            is_active = True
        else:
            is_staff = False
            is_active = False
        
        user = self.model(
            server_name = server_name,
            login_id = login_id,
            platform = platform,
            is_staff = is_staff,
            is_active = is_active,
            is_superuser = is_superuser
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, server_name, login_id, platform, password):
        user = self.add_user(
            server_name,
            login_id,
            platform,
            password
        )
        return user
        

    def create_superuser(self, server_name, login_id, platform, password):
        user = self.add_user(
            server_name,
            login_id,
            platform,
            password,
            is_superuser=True
        )
        return user


# Custom UserModel
class AccountsModel(AbstractBaseUser, PermissionsMixin):

    account_id =  models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    server_name = models.CharField(default="Not set", null=False, blank=False, max_length=200)
    login_id = models.CharField(default=str(uuid.uuid4), max_length=100, blank=False, null=False, unique=True)
    platform = models.CharField(default="Not set", blank=False, null=False, max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    # Define Custom User Manager
    custom_objects = CustomUserManager()

    # Define Required Fields
    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = ['server_name','platform']

    # Model metadata
    class Meta:
        db_table = 'mt5scheduler_accountsmodel'

    # Model objects display format
    def __str__(self):
        return str(self.account_id)

    def get_servername(self):
        return self.server_name

    def get_login_id(self):
        return self.login_id

    def get_platform(self):
        return self.platform

    def get_is_active(self):
        return self.is_active

