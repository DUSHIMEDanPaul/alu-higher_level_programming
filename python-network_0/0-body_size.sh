<<<<<<< HEAD
#!/bin/bash 
# take in a url and display the content 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
<<<<<<< HEAD
=======

>>>>>>> 6c324df0abfbddc3dee58c56b929cae0a4854984
=======
#!/bin/bash
# Script that takes in a URL, sends a request and displays the size of the body of the response
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
>>>>>>> fdb7003ed2662074bbc679488a7255aee0834dfd
