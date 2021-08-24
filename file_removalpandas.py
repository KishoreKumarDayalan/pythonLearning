import os
import re
import pathlib
import time
import shutil
dir="E:\\Input - Copy\\"
out1="E:\\Output\\"
for root,dirs,files in os.walk(dir, topdown=False):
    for name in files:
        print("processing "+ name)
        out_filename=out1 + name
        if(os.path.exists(out_filename)):
            print("Error!!! File already exists!!! please check output directory")
            print()
            time.sleep(2)
        else:
            ip=dir+name
            f=open(ip,'r')
            a=list(f.readlines())
            b=[]
            for i in a:
                if not(i.strip()=='' or i.strip()[0:2]=='//'):
                    b.append(i.strip())
            if not(len(b)==3 and b[1]=='{' and b[2]=='}'):
                shutil.copyfile(ip,out_filename)
            else:
                print()
                print('deleting file ' + name + ' as it has empty content "')
                f.seek(0)
                print(f.read() + '"')
            print()
            f.close()
            time.sleep(2)