# destroyed

##solution:

running strings on the **destroyed.elf** i saw many references to files in windows filesystem let's use volatility then

```volatility -f volatility destroyed.elf -f imageinfo ```

the first thing i always do is to check the files 

```volatility -f destroyed.elf --profile=Win7SP1x64 filescan > filescan.txt```

we notice a test.txt

```volatility -f destroyed.elf --profile=Win7SP1x64 dumpfiles -Q 0x000000007e9e91b0 -D .```

decode the hex **582D4D41537B7468616E6B73666F7264756D70696E6762726F7D** string and get the flag
 

