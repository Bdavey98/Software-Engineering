import sys
import os

def main():
    
    # Starts the server
    if 'up'.strip() in sys.argv:
        os.system("sudo docker-compose up")

    # Allows us to run a docker-compose down.
    if 'down'.strip() in sys.argv:
        os.system("sudo docker-compose down")

    # Builds the containers
    if 'build'.strip() in sys.argv:
        os.system("sudo docker-compose build")

    # Does the migrations
    if 'migrate'.strip() in sys.argv:
        os.system("sudo docker-compose run django python3 manage.py makemigrations")
        os.system("sudo docker-compose run django python3 manage.py migrate")
        
    # Creates a superuser
    if 'admin'.strip() in sys.argv:
        os.system("sudo docker-compose run django python3 manage.py createsuperuser")

    # Allows us to run ALL tests.
    if 'test'.strip() in sys.argv:
        os.system("sudo docker-compose run django python3 manage.py test")

     # Dumps the data in the current database into the fixtures directory.
    if 'dump-data'.strip() in sys.argv:
        os.system("sudo docker-compose run django python3 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission > src/autograder/fixtures/data.json")
        
    # Loads the data in the fixtures directory.
    if 'load-data'.strip() in sys.argv:
        os.system("sudo docker-compose run django python3 manage.py loaddata fixtures/data.json")
    

# end program    
if __name__=="__main__":
    main()
