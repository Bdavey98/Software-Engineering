from django.core.exceptions import ValidationError

# A validation definition that checks if a file upload is either
# a 'java' file or a 'zip' file. Return an error if that is not the case.
#
# param value: The name of the file to be uploaded.
def validate_file(value):
    value= str(value)
    if value.endswith(".java") != True and value.endswith(".zip") != True: 
        raise ValidationError("Only 'Java' and 'Zip' files can be uploaded")
    else:
        return value
