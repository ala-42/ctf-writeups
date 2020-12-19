# xmas-chan

## solution:

after a lot of fails with xss and file upload on the site i tried to check if there is other ways around 

visiting the url http://challs.xmas.htsp.ro:3010/getbanner.php we can notice that we are loading a jwt cookie

![](cookie.png)

the first thing todo here is decode the cookie with https://jwt.io/ let's see what we got 

![](decode.png)

hmmm i've never seen the kid parameter before let's read more about that:

```
The kid (key ID) Header Parameter is a hint indicating which key was used to secure the JWS. This parameter allows originators to explicitly signal a change of key to recipients. The structure of the kid value is unspecified. Its value MUST be a case-sensitive string.
```

also with more researching we can found resources about exploiting KID we can find command injection,lfi,rfi,sqli...

i tried all of them but failed at this point i wanted to give up the challenge and wait for writeup then i got one last weird idea which is to replace the kid value with **/var/www/html/** and adding **flag.php** to the payload

```
python3 jwt_tool.py eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImtpZCI6IlwvdG1wXC9qd3Qua2V5In0.eyJiYW5uZXIiOiJiYW5uZXJcLzUucG5nIn0.Fq35A3IqblXCqL9HLEQStEWc5t5VJUOYz27pLgF9WAY -I -hc kid -hv "/var/www/html/" -S hs256 -pc banner -pv "flag.php"
```
![](burp.png)

it works!!!

because first the flag is in source code of flag.php so flag.php need to be in the payload part
