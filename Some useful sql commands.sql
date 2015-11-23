show databases;

CREATE DATABASE project;


# grant all privileges to user:yiting with ip_address:128.111.106.188 with password:roma
grant all on *.* to yiting@'128.111.106.188' identified by 'roma';

# show all grants/privileges
select * from information_schema.user_privileges;
