import pip
pip.main (['install', "conda"])
# m=[]
# with open('d://DP//dataset_3380_5.txt')as inf:
#      for line in inf:
#          m.append(line.strip().split())
# res=[]
# for i in range (11):
#     res.append([])
#     res[i].append(i+1)
#     res[i].append(0)
#     res[i].append(0)
#     res[i].append(0)
# for zap in m:
#     zap[0]=int(zap[0])
#     zap[2]=int(zap[2])
# for zap in m:
#     a=zap[0]
#     res[(a-1)][1] +=1
# #    res[(zap[0])-1] += 1
#     res[(a-1)][2] +=(zap[2])
# for cl in res:
#     if cl[1]==0:
#         cl[3]='-'
#     else:
#         cl[3]=cl[2]/cl[1]
# for cl in res:
#     print(cl[0],cl[3])
# with open('d://DP//result.txt', 'w')as ouf:
#     for cl in res:
#         i=str(cl[0])+" " + str(cl[3])+'\n'
#         ouf.write(i)
    # for i in range (1,4):
    #     ouf.write(str(popred[i])+" ")
# d=int(input())
# coor = [0,0]
# comm = []
# for i in range(d):
#     comm.append(input().split())
#
# for i in comm:
#     i[1]=int(i[1])
#     if i[0] == "восток":
#         coor[0]+=i[1]
#     if i[0] == 'запад':
#         coor[0]-=i[1]
#     if i[0] == 'север':
#         coor[1] += i[1]
#     if i[0] == 'юг':
#         coor[1]-=i[1]
# print(coor[0],coor[1])



# d = int(input())
# dic=[]
# for i in range(d):
#     dic.append(input().lower())
# l = int(input())
# txt=[]
# for i in range(l):
#     txt.append(input().split())
#
# err=[]
# for l in txt:
#     for w in l:
#         if w not in dic:
#             if w not in err:
#                 err.append(w)
# for i in err:
#     print(i)

# shifr_base = input()
# shifr_code = input()
# text_noncode = input()
# text_code = input()
#
# text_noncode_code=""
# text_code_noncode=""
#
# for i in text_noncode:
#     text_noncode_code+=shifr_code[shifr_base.index(i)]
# for i in text_code:
#     text_code_noncode+=shifr_base[shifr_code.index(i)]
#
# print(text_noncode_code)
# print(text_code_noncode)


# # апишите программу, которая принимает на стандартный вход список игр
# # футбольных команд с результатом матча и выводит на стандартный вывод
# # сводную таблицу результатов всех матчей.
# #
# # За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
# #
# # Формат ввода следующий:
# # В первой строке указано целое число nn — количество завершенных игр.
# n=int(input())
# m=[]
# # После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# for i in range(n):
#     m.append(input().split(';'))
# # Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
# #
# # Вывод программы необходимо оформить следующим образом:
# # Команда:Всего_игр Побед Ничьих Поражений Всего_очков
# #
# d={}
# for l in m:
#     if l[0] not in d.keys():
#         d[l[0]]=[0,0,0,0,0]
#         d[l[0]][0]+=1
#         if l[1]>l[3]:
#
#             d[l[0]][1]+=1
#             d[l[0]][4]+=3
#         elif l[1]==l[3]:
#
#             d[l[0]][2]+=1
#             d[l[0]][4]+=1
#         else:
#
#             d[l[0]][3]+=1
#     else:
#         d[l[0]][0]+=1
#         if l[1]>l[3]:
#             d[l[0]][0]+=1
#             d[l[0]][1]+=1
#             d[l[0]][4]+=3
#         elif l[1]==l[3]:
#             d[l[0]][0]+=1
#             d[l[0]][2]+=1
#             d[l[0]][4]+=1
#         else:
#             d[l[0]][0]+=1
#             d[l[0]][3]+=1
#     if l[2] not in d.keys():
#         d[l[2]]=[0,0,0,0,0]
#         d[l[2]][0]+=1
#         if l[3]>l[1]:
#             d[l[2]][0]+=1
#             d[l[2]][1]+=1
#             d[l[2]][4]+=3
#         elif l[1]==l[3]:
#             d[l[2]][0]+=1
#             d[l[2]][2]+=1
#             d[l[2]][4]+=1
#         else:
#             d[l[2]][0]+=1
#             d[l[2]][3]+=1
#     else:
#         d[l[2]][0]+=1
#         if l[1]<l[3]:
#             d[l[2]][0]+=1
#             d[l[2]][1]+=1
#             d[l[2]][4]+=3
#         elif l[1]==l[3]:
#             d[l[2]][0]+=1
#             d[l[2]][2]+=1
#             d[l[2]][4]+=1
#         else:
#             d[l[2]][0]+=1
#             d[l[2]][3]+=1
#
# # Конкретный пример ввода-вывода приведён ниже.
# #
# # Порядок вывода команд произвольный.
# #
# # Sample Input:
# # 3
# # Зенит;3;Спартак;1
# # Спартак;1;ЦСКА;1
# # ЦСКА;0;Зенит;2
# # Sample Output:
# # Зенит:2 2 0 0 6
# # ЦСКА:2 0 1 1 1
# # Спартак:2 0 1 1 1
# for l in d.keys():
#     print(l, end=';')
#     for i in range(5):
#         print(d[l][i],end=' ')

# import requests
# r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
# t=r.text
# count=1
# while t.split()[0]!="We":
#     r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/'+t)
#     print(t)
#     t=r.text
#     with open('d://DP//result'+str(count)+'.txt', 'w')as ouf:
#         ouf.write(t)
#     count=+1
# # import sys
#
# for i in range (len(sys.argv)):
#     print(sys.argv[i], end=' ')
# m=[]
# with open('d://DP//dataset_3363_4.txt')as inf:
#     for line in inf:
#         m.append(line.strip().split(';'))t
#
# print (m)
# pofam=[]
# popred=[0,0,0,0]
# for l in m:
#     pofam.append((int(l[1])+int(l[2])+int(l[3]))/3)
#     count =1
#     while count <4:
#         popred[count]+=int(l[count])
#         count+=1
# count=1
# while count<4:
#     popred[count]=popred[count]/len(m)
#     count+=1
# # for i in pofam:
# #     print(i)
# # for i in range (1,4):
# #     print (popred[i], end=' ')
# # stroka='abc a bCd bC AbC BC BCD bcd ABC'
#
# # stls=stroka.lower().split()
# # d={}
# # for i in stls:
# #     if i in d.keys():
# #         d[i]+=1
# #     else:
# #         d[i]=1
# # print(d)
# # mw=0
# # wws=[]
# # for i in d:
# #     if d[i]<mw:
# #         pass
# #     elif d.get(i)==mw:
# #         wws.append(i)
# #     else:
# #         wws=[]
# #         wws.append(i)
# #         mw=d[i]
# # print(wws)
# # wws.sort()
# # res=wws[0]+' '+str(mw)
# # print (res)
# with open('d://DP//result.txt', 'w')as ouf:
#     for i in pofam:
#         i=str(i)+'\n'
#         ouf.write(i)
#     for i in range (1,4):
#         ouf.write(str(popred[i])+" ")
# # for i in pofam:
# #     print(i)
# # for i in range (1,4):
# #     print (popred[i], end=' ')