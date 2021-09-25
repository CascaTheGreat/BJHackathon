import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('searchbox')

char_string=" "
search_list = []

def word_separate():
  for char in searchterm:
    if char == ",":
      continue
    elif char == " ":
      search_list.append(char_string)
      continue
    charstring = charstring + char

def word_check(list2):
  for word in charstring:
    if  in word:
      print(list2)

word_check(list3)
word_check(list4)