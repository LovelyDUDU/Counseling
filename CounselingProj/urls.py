"""CounselingProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import mainapp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.main, name='main'), # 메인화면
    path('write/', mainapp.views.write, name='write'), #게시글 쓰기
    path('read/<int:post_id>',mainapp.views.read,name='read'), # 게시글 읽기
    path('update/<int:post_id>',mainapp.views.update, name='update'),
    path('delete/<int:post_id>',mainapp.views.delete,name='delete'), #게시글 삭제
    path('signup/', accounts.views.signup, name='signup'), #회원가입
    path('login/', accounts.views.login,name='login'), #로그인
    path('logout/', accounts.views.logout, name='logout'), #로그아웃
    path('profile/<str:user>',mainapp.views.profile, name='profile'), #메인에서 프로필화면 가기
    path('p_profile/<int:post_id>/<str:user>',mainapp.views.p_profile, name='p_profile'),
    path('c_create/<int:post_id>',mainapp.views.c_create, name="c_create"), #댓글 쓰기
    path('c_delete/<int:comment_id>',mainapp.views.c_delete, name='c_delete'), #댓글 삭제

    path('setPLike/<int:post_id>',mainapp.views.setPLike, name='setPLike'), # 게시글 공감
    path('setPdisLike/<int:post_id>',mainapp.views.setPdisLike, name='setPdisLike'), # 게시글 비공감

    path('setCLike/<int:post_id>/<int:comment_id>',mainapp.views.setCLike, name='setCLike'), # 댓글 공감
    path('setCdisLike/<int:post_id>/<int:comment_id>',mainapp.views.setCdisLike, name='setCdisLike'), # 댓글 비공감

    path('report/<int:post_id>', mainapp.views.report,name='report'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
