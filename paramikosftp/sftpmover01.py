#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

flag = True
while(flag):
    ## where to connect to
    P = input("Enter the IP adddr of machine: ")
    U = input("Enter the username : ")
    Pw = input("Enter the password : ")

    t = paramiko.Transport(P, 22) ## IP and port

    ## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username=U , password= Pw)

    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    ## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

    ## close the connection
    sftp.close() # close the connection
    cont = input("Enter 0 to exit and 1 to continue: ")
    if cont == "0":
       break 
    print(flag, cont)
