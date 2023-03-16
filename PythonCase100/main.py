# -*- coding: utf-8 -*-
# @Time    : 2023/3/16 14:32
# @Author  : wei.yan
# @Email   : 13675196684@163.com
# @File    : main.py
# @Software
# : PyCharm

"""def Cnt_Num( n ):
    cnt = 0
    for i in range(0, n):
        for j in range(0, n ):
            for k in range(0 , n ):
                if i!=j and j!=k and k!=i:
                    print(i*100+j*10+k)
                    cnt += 1
    print(cnt)
"""


# if __name__ == '__main__':
#     Cnt_Num(4)

def Cnt_Num( n ):
    cnt = 0
    for i in range(0 , n):
        for j in range(0, n ):
            for k in range(0, n):
                if i!=j and j!=k and k!=i:
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    Cnt_Num( 3)

