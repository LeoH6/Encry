import random
from colorama import Fore

#LeoH6

def encry(data):
  string = ""
  keylist = ""
  for i in range(len(data)):
    add = str(random.randint(0, 99))
    new = ord(data[i]) + int(add)
    string += "%"
    string += str(new)
    key = int((add))
    keylist += "%"
    keylist += str(key)
  keylist += "%"
  string += "%"
  print("")
  print("~Key = ", keylist, "\n")
  print("~New Data = ", string)
  print("")
  return string

def readstring(data):
  codes = []
  sp = data.split("%")
  for i in sp:
    if i.isdigit():
      codes.append(int(i))
  return codes

def readkey(data):
  key = []
  sp = data.split("%")
  for i in sp:
    if i.isdigit():
      key.append(int(i))
  return key

def anti():
  solved = ""
  askcodes = input("~Enter Encrypted Message or Data - ")
  print("")
  codes = readstring(askcodes)
  askkey = input("~Enter Key - ")
  pas = readkey(askkey)
  for i in range(len(codes)):
    add = (int(codes[i]) - int(pas[i]))
    solved += chr(add)
  print("")
  print("~Message succesfully decoded: ")
  print("")
  print("~", solved)

print(Fore.GREEN)

print("""
    ______                     
   / ____/___  ____________  __
  / __/ / __ \/ ___/ ___/ / / /
 / /___/ / / / /__/ /  / /_/ / 
/_____/_/ /_/\___/_/   \__, /  
                      /____/   """)

print(Fore.RESET)
print("~LeoH6 \n")
print("~Welcome User \n")
stop = False
while stop == (False):
  prompt = input("-> Would you like to encrypt(1) or decrypt(2) - ")
  print("")
  if prompt == ("1"):
    data = input("~Enter Message or Data - ")
    newdata = encry(data)
  elif prompt == ("2"):
    anti()
    print("")
  else:
    print("~Command Not Recognised...\n")
