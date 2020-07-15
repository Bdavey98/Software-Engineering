from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User
from .validators import validate_file

# An assignment given to students with a set due date.
# param name: The name of the assignment.
# param description: The description of the assignment.
# param due_date: The date the assignment is due.
class Assignment(models.Model):
	name = models.CharField(max_length = 60,
						   help_text = 'Give a name to the assignment.',
						   unique = True)

	description = models.TextField(max_length = 1000,
								   help_text = 'Describe the assignment.',
								   )
	
	due_date = models.DateField(null = True, blank = True)


	class Meta:
		permissions = [
			("can_grade_assignment", "Is allowed to grade an assignment"),
			("can_submit_assignment", "Is allowed to turn in an assignment"),
			("can_run_tests", "Is allowed to run an assignment in a unit test"),
		]

	def get_absolute_url(self):
		return reverse('assignment-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.name


# An abstract assignment with no due date.
# param line_description: A short description of the project.
# param full_description: A more detailed description of the project.
# param assignment_list: A list of assignments that are under a project.
# param assigned_students: A list of students able to view the project.
class Project(models.Model):
	line_description = models.CharField(max_length = 60, help_text = 'Write a brief description of the project.',
									unique = True)

	full_description = models.TextField(max_length = 1000, help_text = 'Describe the project in full.')

	assignment_list = models.ManyToManyField(Assignment, help_text = 'What assignments are under this project?')

	assigned_students = models.ManyToManyField(User, help_text = 'What students are assigned to this project?')


	def display_assignment_list(self):
		return ', '.join(Assignment.name for Assignment in self.Assignment.all()[:3])

	def get_absolute_url(self):
		return reverse('project-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.line_description

	display_assignment_list.short_description = 'Assignment List'


# An acceptance test that can be created by instructors.
# param name: The name of the test.
# param description: Describes what the test is focused on.
# param attached_aasignment: The assignment that the test will run on.
# param test_file: The test file that actually does the test.
# param Status: A tuple that sets the view permissions for the test.
# param view: Allows an instructor to set the status of the test.
class Test(models.Model):
	name = models.CharField(max_length = 100, help_text = 'What is the name of the test?')
	description = models.TextField(max_length = 1000, help_text = 'Describe the parameters of the test.')
	attached_assignment = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null = True)
	test_file = models.FileField(upload_to="tests/", validators=[validate_file])

	Status = (
		('Viewable to all', 'Public'),
		('Viewable to instructor', 'Private'),
	)

	view = models.CharField(
		max_length = 50,
		choices = Status,
		blank = True,
		default = 'Private',
		help_text = 'Test View Permissions',
	)

	def get_absolute_url(self):
		return reverse('test-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return self.name
	
# A submission that can be submitted by students.
# param submission_name: The name of the submission.
# param assignment: The assignment that the submission will be under.
# param sumission_file: The file that the student is submitting.
# param student: The student that has submitted the file.
class Submit(models.Model):
	submission_name = models.CharField(max_length = 160, help_text = "Enter your name and the name of the assignment you are submitting.")
	assignment = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null = True)
	submission_file = models.FileField(upload_to="submissions/", validators=[validate_file])
	student = models.ForeignKey(User,on_delete=models.SET_NULL, null = True)

	def get_absolute_url(self):
		return reverse('submit-detail', args=[str(self.id)])
		
	def __str__(self):
		"""String for representing the Model object."""
		return self.submission_name
	
