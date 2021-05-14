import sys;args = sys.argv[1:]

def ask(first,second):
   print(first+' or '+second+'?')
   a = input()
   while a not in ['0','1']:
      print('0 or 1 please')
      a = input()
   return int(a)
   
def mergeSort(arr):
   if len(arr)>1:
      middle = len(arr)//2
      left = arr[:middle]
      right = arr[middle:]
      mergeSort(left)
      mergeSort(right)

      i = j = 0
      while i<len(left) and j<len(right):
         if ask(left[i],right[j]):
            arr[i+j]=right[j]
            j+=1
         else:
            arr[i+j]=left[i]
            i+=1

      while i<len(left):
         arr[i+j]=left[i]
         i+=1
      
      while j<len(right):
         arr[i+j] = right[j]
         j+=1

entries = open(args[0], 'r').read().splitlines()
print('These are your entries: '+', '.join(entries))
print('Type 0 if you prefer the first item and 1 if you prefer the second.')
mergeSort(entries)
print('Results:')
for i,e in enumerate(entries):
   print(str(i+1)+': '+e)