import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))

    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')



## import re
##for i in range(int(input())):
##    N = input().strip()
##    if N.isalnum() and len(N) == 10:
##        if bool(re.search(r'(.*[A-Z]){2,}',N)) and bool(re.search(r'(.*[0-9]){3,}',N)):
##            if re.search(r'.*(.).*\1+.*',N):
##                print('Invalid')
##            else:
##                print('Valid' )   
##        else:
##            print('Invalid')
##    else:
##        print('Invalid')
##
##Second solution
