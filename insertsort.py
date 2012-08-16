def insertsort(list):
    for inicio in range(1,len(list)):
        valor=list[inicio]
        i=inicio -1
        while i>=0:
          if valor < list[i]:
               list[i+1] = list[i]
               list[i]=valor
               i=i-1
          else:
              break
