from django.shortcuts import render
#Mixin para super_user "admin":
class Logged_Super_User_Mixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return super().dispatch(request, *args, **kwargs)
        return render(request, 'insufficient_permissions.html')