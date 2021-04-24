## Not Slick - Forensics

opening the image with a hex editor wen can notice that the bytes are inverted. the magic bytes for a PNG file is ```89 50 4E 47``` and they are at the end. 

so let's invert them back with python

```python
f1 = open("notslick.png", "rb+")
f2 = open("out.png", "wb+")
f2.write(f1.read()[::-1])
f1.close()
f2.close()
```

and you get the flag inside the image

easy