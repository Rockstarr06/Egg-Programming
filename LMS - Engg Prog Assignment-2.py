#!/usr/bin/env python
# coding: utf-8

# # Library Management System

# You are required to design a simple Library Management System (LMS) to manage books for a small community library. 

# # 1. Add a book to the Library

# In[7]:


aa1= ('A Long Time Dead', 'J M Dalgliesh', '20')
ab1= ('The Skylark Secret', 'Fiona Valpy', '26')
ac1= ('The Lost Bookshop','Evie Woods', '14')

library={
    'AA1': aa1, 
    'AB1': ab1, 
    'AC1': ac1}
print('Library', library)

ISBN=str.upper(input('Add ISBN:' ))
book_Name=str.title(input('Add Book Name:' ))
author=str.title(input('Add Author:' ))
qty=int(input('Add Quantity:' ))
library[ISBN]=(book_Name, author, qty)
print('Added Successfully', library)


# # 2. Remove a book from the library using its ISBN!

# In[8]:


aa1= ('A Long Time Dead', 'J M Dalgliesh', '20')
ab1= ('The Skylark Secret', 'Fiona Valpy', '26')
ac1= ('The Lost Bookshop','Evie Woods', '14')

library={
    'AA1': aa1, 
    'AB1': ab1, 
    'AC1': ac1}
print('Library', library)

remove=str.upper(input('Remove a book by typing ISBN:' ))
library.pop(remove)
print('Removed Successfully', library)


# # 3. Find a book by its title

# In[9]:


aa1= ('A Long Time Dead', 'J M Dalgliesh', '20')
ab1= ('The Skylark Secret', 'Fiona Valpy', '26')
ac1= ('The Lost Bookshop','Evie Woods', '14')

library={
    'AA1': aa1, 
    'AB1': ab1, 
    'AC1': ac1}

library_find={
    'AA1': aa1[0],
    'AB1': ab1[0],
    'AC1': ac1[0]}

find=str.title(input('Find by Typing the Book Name:' ))

for key,value in library_find.items():
    if value==find:
        print(key)


# # 4. List all books

# In[10]:


aa1= ('A Long Time Dead', 'J M Dalgliesh', '20')
ab1= ('The Skylark Secret', 'Fiona Valpy', '26')
ac1= ('The Lost Bookshop','Evie Woods', '14')

library={
    'AA1': aa1, 
    'AB1': ab1, 
    'AC1': ac1}

library_find={
    'AA1': aa1[0],
    'AB1': ab1[0],
    'AC1': ac1[0]}

print(sorted(library_find.values()))


# # 5. Borrow a book

# In[2]:


aa1= ('A Long Time Dead', 'J M Dalgliesh', '20')
ab1= ('The Skylark Secret', 'Fiona Valpy', '26')
ac1= ('The Lost Bookshop','Evie Woods', '14')

library={
    'AA1': aa1, 
    'AB1': ab1, 
    'AC1': ac1}

library_find={
    'AA1': aa1[0],
    'AB1': ab1[0],
    'AC1': ac1[0]}

find=str.title(input('Find by Typing the Book Name:' ))

library_borrow={
    'AA1': aa1[2],
    'AB1': ab1[2],
    'AC1': ac1[2]}

for key, value in library_find.items():
     if value==find:
            print(int(library_borrow[key]))
            borrow=str(input('if borrowing then type \'Yes\':' ))
            print('Remaining Qty in Library:', int(library_borrow[key])-1)


# # Return  a book

# In[3]:


aa1= ('A Long Time Dead', 'J M Dalgliesh', '20')
ab1= ('The Skylark Secret', 'Fiona Valpy', '26')
ac1= ('The Lost Bookshop','Evie Woods', '14')

library={
    'AA1': aa1, 
    'AB1': ab1, 
    'AC1': ac1}

library_find={
    'AA1': aa1[0],
    'AB1': ab1[0],
    'AC1': ac1[0]}

find=str.title(input('Find by Typing the Book Name:' ))

library_borrow={
    'AA1': aa1[2],
    'AB1': ab1[2],
    'AC1': ac1[2]}

for key, value in library_find.items():
     if value==find:
            print(int(library_borrow[key]))
            borrow=str(input('if returning then type \'Yes\':' ))
            print('Remaining Qty in Library:', int(library_borrow[key])+1)

