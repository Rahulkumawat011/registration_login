from apps.core.views import CreateUserView, UpdateUserView, UserDeleteView, ConfirmDelete, student_list

app_name = "core"
from apps.core import views
from django.urls import path


urlpatterns = [
    path("index", views.index),
    path('form', views.homepage),
    path('contact', views.Contact.as_view()),
    # path('create_user',views.create_user),
    path('create_student', views.create_student),
    # path('create_table',views.create_table)
    # path('student_list', views.student_list),
    # path('delete/<int:id>',views.delete),
    # path('update/<int:id>', views.update),
    # path('confirm_delete/<int:id>', views.Confirm_Delete),
    path('student_list',student_list.as_view()),
    path('create_user/', CreateUserView.as_view(), name='create_user'),
    path('delete/<int:id>/', UserDeleteView.as_view(), name='delete_user'),
    path('update/<int:pk>/',  UpdateUserView.as_view(), name='update_user'),
    path('confirm_delete/<int:id>', ConfirmDelete.as_view()),

]