# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render, redirect
# from django.urls import reverse, reverse_lazy
# from django.contrib.auth.models import User
# from users.models import User_profile
# from users.forms import Update_profile_form
# from django.views.generic import UpdateView
# # Create your views here.

# class Profile_view(LoginRequiredMixin, UpdateView):
#     model = User_profile
#     form_class = Update_profile_form
#     template_name = 'profile_view.html'
#     def get_success_url(self):
#         return reverse('profile_view', kwargs={'username':self.object.name})