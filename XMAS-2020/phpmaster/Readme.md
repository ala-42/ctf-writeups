# phpmaster

## analysis

* first the script check if there is 'e' in the first and second parameter 

* second it checks if they have the same length

* check if they are different 

* check if first char of p1 is different from 0

* check similarity between p1 and p2 using loose comparison 

## exploitation:

php is known for type juggling attacks reading this https://www.php.net/manual/en/language.operators.comparison.php can help to solve the challenge 

```var_dump(100 == "1e2"); // 100 == 100 -> true``` according to loose comprison in php this will pass all the check but not the first one because we have a **e** in p1. we can just replace **e** with **E** and it will be fine. 

http://challs.xmas.htsp.ro:3000/?param1=1E2&param2=100