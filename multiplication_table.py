__author__ = 'Daeho'
for x in [2,5,8]:
     print("");
     for y in range(1,10,1):
          if(x==8):
               print(x,'*',y,'=',(x*y),' ',x+1,'*',y,'=',((x+1)*y));
          else:
               print(x,'*',y,'=',(x*y),' ',x+1,'*',y,'=',((x+1)*y),' ',x+2,'*',y,'=',((x+2)*y))
