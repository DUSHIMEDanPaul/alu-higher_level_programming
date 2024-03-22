#!/bin/bash 
# take in a url and display the content 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
<<<<<<< HEAD
=======

>>>>>>> 6c324df0abfbddc3dee58c56b929cae0a4854984
