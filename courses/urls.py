from django.urls import path
from . import views
from .views import CourseChartView


urlpatterns = [
    path('mine/',
         views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    path('create/',
         views.CourseCreateView.as_view(),
         name='course_create'),
    path('<pk>/edit/',
         views.CourseUpdateView.as_view(),
         name='course_edit'),
    path('<pk>/delete/',
         views.CourseDeleteView.as_view(),
         name='course_delete'),
    path('<pk>/module/',
         views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('content/<int:id>/delete/',
         views.ContentDeleteView.as_view(),
         name='module_content_delete'),
    path('module/<int:module_id>/',
         views.ModuleContentListView.as_view(),
         name='module_content_list'),
    path('module/order/',
         views.ModuleOrderView.as_view(),
         name='module_order'),
    path('content/order/',
         views.ContentOrderView.as_view(),
         name='content_order'),  

    path('subject/<slug:subject>)/',
         views.CourseListView.as_view(),
         name='course_list_subject'),
    path('<slug:slug>/',
         views.CourseDetailView.as_view(),
         name='course_detail'),
    path('', views.index, name='index'),      
    path('course/<int:course_id>/', views.detail, name='detail'),
    path('course/<int:course_id>/results/', views.results, name='results'),
    path('course/<int:course_id>/vote/', views.vote, name='vote'),
    path('course/chart/', CourseChartView.as_view(), name='course_chart'),                                         
]
