from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.db.models import Q

Usuario = get_user_model()

class EmailAuth(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
            p = password
            e = email
            try:

                usuario = Usuario.objects.get(email__iexact=e)

            except Usuario.DoesNotExist:

                pw = make_password(p, salt=None, hasher='default')

            except Usuario.MultipleObjectsReturned:

                usuario.objects.filter(email=e).order_by('id').first()
            
            else:

                if usuario.check_password(p) and self.user_can_authenticate(usuario):

                    return usuario
            return None
    
    def get_user(self, user_id):
        try:
            user = Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None