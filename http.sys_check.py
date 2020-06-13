#By TeamsSix
#Blog teamssix.com
import sys,requests
requests.packages.urllib3.disable_warnings()

try:
    path=sys.argv[1]
except:
    print('python3 http.sys_check.py url.txt')
    sys.exit()

success_url = []
f = open(path)
f_read = f.readlines()
for i in f_read:
    i = i.replace('\n','')
    try:
        r = requests.get(i,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0','Range':'bytes=0-18446744073709551615'} ,verify=False,timeout=7)
    except KeyboardInterrupt:
        sys.exit()
    except:
        print('[-]  timeout ' +i)
        pass
    if r.status_code == 416:
        print('\033[1;34;40m[+]  check success {}\033[0m'.format(i))
        success_url.append(i)
    else:
        print('[-]  ' +i)

s_f = open('result.txt','w')
for j in success_url:
    s_f.write(j)
    s_f.write('\n')
s_f.close()
