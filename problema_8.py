
sdc=str(input('IntroduceTi Sirul de caractere format din litere majuscule ale alfabetului latin:'))
s1=""
s2=""
s3=""
for r in sdc:
    x=chr(ord(r)+1)
    s1+=x
    o=s1.replace('!',' ') 
    a=o.replace('[','A') 
print("Sirul 1:", a)
s2=o
for r in sdc:
    d=s2.replace(("Z"), ("A"))
    o=d.replace('!',' ')
    l=o.replace('[','A')
print("Sirul 2:", l) 
s3=l
for r in sdc:
    g=s3.replace(' ','-')
    o=g.replace('[','A')
print("Sirul 3:", o)