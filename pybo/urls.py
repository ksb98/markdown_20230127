from django.urls import path
from . import views  # 현재 디렉터리에 views 모듈

urlpatterns = [

    path('', views.index),  # view index로 메핑
    path('<int:question_id>/',views.detail, name='detail'),
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'),
    path('boot/list/', views.boot_list, name='boot_list'),
    path('boot/reg/', views.boot_reg, name='boot_reg'),

]
app_name = 'pybo';
