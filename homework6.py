my_dict={'Sasha':1985,'Vova':1998,'Lena':2000}
print('Dict:',my_dict)
print('Existing value:',my_dict['Lena'])
print('Not existing value:',my_dict.get('Bob'))
my_dict.update({'Karl':1995,'Misha':1990})
a=my_dict.pop('Vova')
print('Deleted value:',a)
print('Modifiet dictionary:',my_dict)
s=''
print(s)# пустая строка
my_set={True,12.3,'Ura, chet poluchaetsya!',True,True,True,111,111}
print('Set:',my_set)
my_set.update({13,False})
my_set.discard(1)
print('Modified set:',my_set)


