#!/bin/bash 
<<<<<<< HEAD
# take in a url and display the content 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
=======
# display the body of a file 
curl -sLfG "$1"
>>>>>>> 9bc55d9b852094cb1b4b6ffc53e5914ce0475a9f
