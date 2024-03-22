#!/bin/bash
<<<<<<< HEAD
# get all the allowed methods 
<<<<<<< HEAD
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2--
=======
<<<<<<< HEAD
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
=======
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
>>>>>>> 9bc55d9b852094cb1b4b6ffc53e5914ce0475a9f
>>>>>>> 6c324df0abfbddc3dee58c56b929cae0a4854984
=======
#  a script that takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
>>>>>>> fdb7003ed2662074bbc679488a7255aee0834dfd
