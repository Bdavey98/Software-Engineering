# Run script commands
The script is run by entering "python3 run.py 'command' " with 'command' being:  
up: do docker-compose up  
down: do docker-compose down  
build: does docker build  
migrate: runs makemigrations and migrate  
admin: create a new superuser  
test: run all of the tests made
load-data: Loads the fixture stored in the 'fixtures' directory.  
dump-data: Stores your current database setup into the 'fixtures' directory.  

# Database Info
The admin username is: Team4K  
The password for every user is: TBEJ@potsdam

# Database Troubleshooting
So I ran into some trouble with getting the database up and running. I was able to fix it by doing the following:

If you get an error saying that you can't connect to the mariadb server, find the id of the container running
the mariadb service and enter the following:

````
sudo docker exec -it <container ID> bash
root@<container ID>:/ mysql -u root -p
````

It will ask you for a password, it is either:" This_is_a_bad_password" or you just press enter. Once you're in
do this:

````  
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'django'@'%' IDENTIFIED BY 'django' WITH GRANT OPTION;FLUSH PRIVILEGES;
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'django'@'localhost' IDENTIFIED BY 'django' WITH GRANT OPTION;FLUSH PRIVILEGES;
MariaDB [(none)]> CREATE DATABASE autograder;
````

By this point it should work....Hopefully.

