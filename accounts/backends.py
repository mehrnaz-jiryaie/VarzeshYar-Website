from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from .models import Account, TrainerAccount

# class AccountBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = Account.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except Account.DoesNotExist:
#             pass
#         try:
#             user = TrainerAccount.objects.get(username=username)
#             if user.check_password(password):
#                 return user
#         except TrainerAccount.DoesNotExist:
#             pass
#         return None

#     def get_user(self, user_id):
#         try:
#             return Account.objects.get(pk=user_id)
#         except Account.DoesNotExist:
#             try:
#                 return TrainerAccount.objects.get(pk=user_id)
#             except TrainerAccount.DoesNotExist:
#                 return None




class AccountBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Account.objects.get(username=username)
            if user.check_password(password):
                return user
        except Account.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk=user_id)
        except Account.DoesNotExist:
            return None

class TrainerAccountBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = TrainerAccount.objects.get(username=username)
            if user.check_password(password):
                return user
        except TrainerAccount.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return TrainerAccount.objects.get(pk=user_id)
        except TrainerAccount.DoesNotExist:
            return None