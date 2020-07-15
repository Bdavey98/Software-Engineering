from django import forms
from gradebook.models import Project, Test, Assignment, Submit
from django.contrib.auth.models import User


# Form used for assigning a project to a student
# param projects: A list that displays the members in 'Projects'
# param fields: Shows 'students' and 'projects' when the form is displayed.
class ProjectAssignmentForm(forms.ModelForm): 

    projects = forms.ModelChoiceField(queryset = Project.objects.all(), required = True)
    

    class Meta:
        model = Project
        fields = ('projects', 'assigned_students')
        
    def __init__(self, *args,**kwargs):
        super (ProjectAssignmentForm,self ).__init__(*args,**kwargs)
        self.fields['assigned_students'].queryset = User.objects.filter(groups__name='Student')
   
# Form used to create a new public acceptance test
# param name: The name of the test
# param description: A description of what the test does
# param view_status: Sets who will be able to see the newly created test.
class NewAcceptanceTest(forms.ModelForm):
    Status = (
        ('Viewable to all', 'Public'),
        ('Viewable to instructor', 'Private'),
    )

    name = forms.CharField(max_length = 100, help_text = 'What is the name of the test?')
    description = forms.CharField(max_length = 1000, widget=forms.Textarea, help_text = 'Describe the parameters of the test.')
    view_status = forms.ChoiceField(choices = Status)

    class Meta:
        model = Test
        fields = ('attached_assignment', 'test_file',)
        
# Form used to submit an assignment into the autograder website
# param assignment: The list of assignments a student is able to submit a file to
class NewSubmission(forms.ModelForm):
    assignment = forms.ModelChoiceField(queryset = Assignment.objects.all())
    
    
    class Meta:
        model = Submit
        fields = ('submission_name', 'submission_file')
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(NewSubmission, self).__init__(*args, **kwargs)
        self.fields['assignment'].queryset = Assignment.objects.filter(
        project__assigned_students__username=self.user.username)
        
        
   