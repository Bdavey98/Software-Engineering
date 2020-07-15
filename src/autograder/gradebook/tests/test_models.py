from django.test import TestCase
from gradebook.models import Project, Assignment


class ProjectModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Project.objects.create(line_description = 'This project focuses on binary data.',
							   full_description = 'This project is meant to test student on their knowledge of binary data.',)
		
		
	def test_line_description_label(self):
		project = Project.objects.get(id=1)
		field_label = project._meta.get_field('line_description').verbose_name
		self.assertEquals(field_label, 'line description')
		
	def test_full_description_label(self):
		project = Project.objects.get(id=1)
		field_label = project._meta.get_field('full_description').verbose_name
		self.assertEquals(field_label, 'full description')
		
	def test_assignment_label(self):
		project = Project.objects.get(id=1)
		assignment_test = project.assignment_list.create(name = 'test',
														 due_date = '2020-05-23')
		self.assertEquals(project.assignment_list.get(pk=assignment_test.pk), assignment_test)
		
		
class AssignmentModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		Assignment.objects.create(name = 'P003-BitWorks',
								  due_date = '2020-05-23',)
		
	def test_name_label(self):
		test = Assignment.objects.get(id=1)
		field_label = test._meta.get_field('name').verbose_name
		self.assertEquals(field_label, 'name')
		
	def test_due_date_label(self):
		test = Assignment.objects.get(id=1)
		field_label = test._meta.get_field('due_date').verbose_name
		self.assertEquals(field_label, 'due date')
		
	
		
		
		
