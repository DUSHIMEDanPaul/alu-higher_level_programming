#!/bin/bash
# get all the allowed methods 
<<<<<<< HEAD
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
=======
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
>>>>>>> 9bc55d9b852094cb1b4b6ffc53e5914ce0475a9f
