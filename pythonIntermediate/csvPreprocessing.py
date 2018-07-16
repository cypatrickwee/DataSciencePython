import os

t = [];
def remove_empty_lines(filename):
   if not os.path.isfile(filename):
      print("{} does not exist.".format(filename));
      return
   
   with open(filename) as filehandler:
      lines = filehandler.readlines();
      for line in lines:
         if line.strip():
            t.append(line);
      print(t);
   
   with open("new_nfl.csv", "w") as filehandler:
      filehandler.writelines(t);

remove_empty_lines("nfl.csv");

'''
   improve version

   def remove_empty_lines(filename):
       if not os.path.isfile(filename):
        print("{} does not exist ".format(filename))
        return
    with open(filename) as filehandle:
        lines = filehandle.readlines()

    with open(filename, 'w') as filehandle:
        lines = filter(lambda x: x.strip(), lines)
        filehandle.writelines(lines) 
'''