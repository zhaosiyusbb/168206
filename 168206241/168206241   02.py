#coding=utf-8

 def selectedSort(myList):

     #��ȡlist�ĳ���

     length = len(myList)

     #һ�����ж����ֱȽ�

     for i in range(0,length-1):

         #Ĭ��������Сֵ��indexΪ��ǰֵ

         smallest = i

         #�õ�����Сindex��ֵ�ֱ�������ֵ���бȽ�,�Ա��ȡ��Сindex

         for j in range(i+1,length):

             #����ҵ��ȵ�ǰֵС��index,�������ֵ����

             if myList[j]<myList[smallest]:

                 tmp = myList[j]

                 myList[j] = myList[smallest]

                 myList[smallest]=tmp

         #��ӡÿһ�ֱȽϺõ��б�

         print("Round ",i,": ",myList)


 myList = [1,4,5,0,6]

 print("Selected Sort: ")

 selectedSort(myList)