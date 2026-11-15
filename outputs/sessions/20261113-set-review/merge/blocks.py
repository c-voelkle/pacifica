import re,sys
R='/home/claude/pacifica/book-agent/revision/'
def section(f):
    L=open(R+f+'.md',encoding='utf8').read().split('\n')
    a=next(i for i,l in enumerate(L) if l.startswith('## Storyline text'))
    b=next(i for i in range(a+1,len(L)) if L[i].startswith('## '))
    return L[a+1:b]
def blocks(f):
    """returns list of ('i',text) instruction or ('q',text) quote paragraphs"""
    out=[];cur=None
    for l in section(f):
        if l.startswith('>'):
            body=l[1:].lstrip()
            if body=='' :
                cur=None; continue
            if cur is None: cur=['q',body]; out.append(cur)
            else: cur[1]+=' '+body
        else:
            cur=None
            if l.strip(): out.append(['i',l.strip()])
    return out
if __name__=='__main__':
    for f in sys.argv[1:]:
        print('=====',f)
        for n,(k,t) in enumerate(blocks(f)):
            if k=='i': print(f'[{n}] I: {t[:700]}')
            else: print(f'[{n}] Q({len(t)}): {t[:150]} … {t[-90:]}')
