import base64
def base64encode(s):
    en = base64.b64encode(s.encode('utf-8'))
    return en.decode('utf-8')
def base64decode(a):
    de = base64.b64decode(a)
    return de.decode('utf-8')
strdesum = ''
for i in range(1,49):
    fname = 'douyinzhibo{:0>2d}_ids_str.txt'.format(i)
    print(fname)
    strin = ''
    with open(fname,mode='r',encoding='utf-8') as txtf:
        strin = txtf.read()
    strde = base64decode(strin)
    strdesum+=strde
    print(strde)


for i in range(1,23):
    fname = 'dymcmn{:0>2d}_ids_str.txt'.format(i)
    print(fname)
    strin = ''
    with open(fname,mode='r',encoding='utf-8') as txtf:
        strin = txtf.read()
    strde = base64decode(strin)
    strdesum+=strde
    print(strde)
stren = base64encode(strdesum)
with open('douyinsum_ids_str.txt',mode='w',encoding='utf-8') as wf:
    wf.write(stren)
