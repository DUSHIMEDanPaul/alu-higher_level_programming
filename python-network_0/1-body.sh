#!/bin/bash 
<<<<<<< HEAD
# take in a url and display the content 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
=======
# display the body of a file 
curl -sLfG "$1"
