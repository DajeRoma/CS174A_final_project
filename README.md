# CS174A_final_project

Due Date: Demo on December 7, 2015 (Monday)

This is the final project of the course and is a team project (maximum size of team: 2). The objective of this project is to implement and evaluate a secure database service prototype that stores data encrypted in the cloud and allows clients to run aggregate SQL queries over it. To ensure data confidentiality, it is required to use homomorphic encryption schemes, which allow performing addition or multiplication operations over encrypted ciphertexts without the need for decryption while ensuring strong security. In a nutshell, you will write an aggregation User-Defined-Function (UDF) for MySQL that implements the SUM operation over encrypted values. The MySQL server will run on an Amazon AWS instance and your client should connect remotely to issue queries: INSERT, simple SELECT, and SELECT SUM().


Some useful linux commands to refer to:

-- copy my_udf.so (in the current directory) to /usr/lib/mysql/plugin/ where .so file should go
sudo cp my_udf.so /usr/lib/mysql/plugin/

-- create a fold called 174A
mkdir 174A

-- compile the .c file to .so
gcc -I/usr/include/mysql -shared -o my_udf.so my_udf.c

-- compile the .c file to .so (if the previous one gives warning and mention "-fPIC")
gcc -I/usr/include/mysql -shared -o my_udf.so my_udf.c -fPIC

