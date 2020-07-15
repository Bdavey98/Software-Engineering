from django.urls import path
from . import views
from gradebook import views as core_views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('assign/', core_views.Assign, name='Assign'),
	path('newTest/', core_views.newTest, name='newTest'),
	path('newSubmission/', core_views.newSubmission, name='newSubmission'),
	path('projects/', views.ProjectListView.as_view(), name = 'projects'),
	path('project<int:pk>/', views.ProjectDetailView.as_view(), name = 'project-detail'),
	path('assignments/', views.AssignmentListView.as_view(), name = 'assignment-list'),
	path('assignment<int:pk>/', views.AssignmentDetailView.as_view(), name ='assignment-detail'),
	path('test/', views.TestListView.as_view(), name = 'test'),
	path('test<int:pk>/', views.TestDetailView.as_view(), name ='test-detail'),
	path('submit/', views.SubmitListView.as_view(), name ='submit'),
	path('submit<int:pk>/', views.SubmitDetailView.as_view(), name ='submit-detail')
]
