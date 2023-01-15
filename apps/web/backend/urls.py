"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import (
    path,
    include,
    re_path,
)
from django.contrib.auth import views as auth_views

from blog.views import (
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    BlogHomeView,
)

from accounts.views import (
    signin_view,
    signup_view,
    signout_view,

    ResetPasswordView,  
    PasswordResetDoneView,
    CustomChangePassword
)

from comments.views import CommentReply

from accounts.forms import PasswordResetConfirmForm

from pages.views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
)

from search.views import SearchView

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('search/', SearchView.as_view(), name='search'),

    re_path(r'^$', HomePageView.as_view(), name='home'),
    re_path(r'^about/$', AboutPageView.as_view(), name='about'),
    re_path(r'^contact/$', ContactPageView.as_view(), name='contact'),

    re_path(r'^blog/$', BlogHomeView.as_view(), name='blog-home'),
    re_path(r'^blog/create/$', BlogCreateView.as_view(), name='blog-create'),
    re_path(r'^blog/detail/(?P<id>[0-9A-Fa-f-]+)/$', BlogDetailView.as_view(), name='blog-detail'),
    re_path(r'^blog/update/(?P<id>[0-9A-Fa-f-]+)/$', BlogUpdateView.as_view(), name='blog-update'),
    re_path(r'^blog/delete/(?P<id>[0-9A-Fa-f-]+)/$', BlogDeleteView.as_view(), name='blog-delete'),

    re_path(r'^comment/reply/$', CommentReply.as_view(), name="comment-reply"), 

    re_path(r'^sign-in/$', signin_view, name='sign-in'),
    re_path(r'^sign-up/$', signup_view, name='sign-up'),
    re_path(r'^sign-out/$', signout_view, name='sign-out'),
    
    re_path(r'^password-reset/$', ResetPasswordView.as_view(), name='password_reset'),

    re_path(r'^password-reset-done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        form_class=PasswordResetConfirmForm,
        template_name='accounts/password-reset/password-reset-confirm.html'
    ),
    name='password_reset_confirm'),

    re_path(r'^password-reset-complete/$',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='accounts/password-reset/password-reset-complete.html'
        ),
         name='password_reset_complete'),

    re_path(r'^change-password/$', CustomChangePassword.as_view(), name='change-password'),
]