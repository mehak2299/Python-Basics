def run(s):
  flag=False
  for i in s.upper():
      if i>='A'and i<='Z':
          flag=True
      elif i>='0' and i<='9':
          flag=True
      else:
          flag=False
  return  flag

if __name__ =='__main__':
   string = "GeeksForGeeks123_"

   # calling run function
   print(run(string))