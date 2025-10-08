


list = ['dog','cat','rabbit','ferret']
print (list)

list.append('mouse')

print (list)

#insert item with "insert"

list.insert(0, 'pig')
print(list)

#"del" removes item forever popped removes it but allows for the same item to be recalled

del list [0]
print (list)

popped_list = list.pop(1)
print(list)
print(popped_list)

#popped will print what was popped duh

wouldnt_own = (popped_list)

print()
print (f"id never own a {wouldnt_own.upper()}")
print()

#the output is a simple sentece about pets id never own

#you can remove an item from any position using the "pop()"

popped_list = list.pop()
print(popped_list)

#if the place number is unknown just use the ".remove()" method
print()
print(list)

list.remove('ferret')
print(list)

#.remove can also be used to work with values in a list

uncommon = ('rabbit')
list.remove(uncommon)
print(f"\nmost people down own a {uncommon.upper()}")  