# pecular gifts

## solution:

this is a super guessy challenge 

unzip the file and we get 2 files: **GIFTS.jpg** and **XMAS.jpg**

typical stego challenge, first i run steghide on XMAS.jpeg after a lot of guess is used the password **XMAS** and i got a file **xmas.txt**

```
--- Message from Santa Claus ---
Did you know that base64 can be used for encoding scripts and websites?
Maybe we can use it for our gifts.
```
and then you need to guess that the password for **GIFTS.jpg** is the word gifts base64 encoded it will extract flag.txt