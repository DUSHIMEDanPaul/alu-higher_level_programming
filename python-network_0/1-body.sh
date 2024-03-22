<<<<<<< HEAD
#!/bin/bash 
<<<<<<< HEAD
# take in a url and display the content 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
=======
# display the body of a file 
curl -sLfG "$1"
<<<<<<< HEAD
=======
>>>>>>> 9bc55d9b852094cb1b4b6ffc53e5914ce0475a9f
>>>>>>> 6c324df0abfbddc3dee58c56b929cae0a4854984
=======
#!/bin/bash
# This script takes in a URL, sends GET request and displays body of response
curl -sL "$1"
>>>>>>> fdb7003ed2662074bbc679488a7255aee0834dfd
