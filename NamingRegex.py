import os
import re
import pathlib
import time
dir="E:\\Input - Copy\\"
out1="E:\\Output\\"
for root,dirs,files in os.walk(dir, topdown=False):
    for name in files:
        print("processing "+ name)
        out_filename=out1 + name
        print(out_filename)
        if(os.path.exists(out_filename)):
            print("Error!!! File already exists!!! please check output directory")
        else:
            a1url=dir+name
            a=open(a1url,"r")
            a2url=out1+"final211.txt"
            pathlib.Path(a2url).unlink(missing_ok=True)
            fi=open(a2url,"w")
            print('created final1 file')
            a3url=out1+"log1.txt"
            pathlib.Path(a3url).unlink(missing_ok=True)
            log=open(a3url,"w")
            print('created log file')
            count=0
            for s in a:
                a1=[]
                a1=re.findall(r'Record "\d+"', s)
                if(a1):
                    b=re.findall(r'\d+',list(a1)[0])
                    if(b):
                        log.write(s)
                        s=re.sub(list(a1)[0],"Record "+list(b)[0],s)
                        log.write(s)
                        count=count+1
                        fi.write(s)
                    else:
                        fi.write(s)
                else:
                    fi.write(s)
            fi.close()
            a.close()
            fi3=open(a2url,"r")
            fi2=open(out_filename,'w')  
            for s in fi3:
                a2=[]
                a2=re.findall(r'Codeunit "\d+"', s)
                if(a2):
                    b=re.findall(r'\d+',list(a2)[0])
                    if(b):
                        log.write(s)
                        s=re.sub(list(a2)[0],"Codeunit "+list(b)[0],s)
                        log.write(s)
                        count=count+1
                        fi2.write(s)
                    else:
                        fi2.write(s)
                else:
                    fi2.write(s)
            fi2.close()
            fi3.close()
            log.close()     
            print('file successfully processed, please check output')
            print(count)
            
        