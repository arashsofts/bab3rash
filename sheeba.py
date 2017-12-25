
class bcolors:
    HEADER = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Cuser = "abdullah"
Cuser1 = "abdulrahman"
Cuser2 = "ahmed"
Cuser3 = "fakri"
Cuser4 = "osamah"
yes = "yes"

#individual lookup


Abdulrahman = bcolors.UNDERLINE + bcolors.BOLD + bcolors.HEADER + "Abdulrahman [Busboy]" + bcolors.ENDC

Abdullah = bcolors.UNDERLINE + bcolors.FAIL + bcolors.BOLD + "Abdullah [Busboy]" + bcolors.ENDC

Ahmed = bcolors.UNDERLINE + bcolors.HEADER + bcolors.BOLD + "Ahmed [Busboy]" + bcolors.ENDC


Fakri = bcolors.UNDERLINE + bcolors.BOLD + bcolors.FAIL + "Fakri [Busboy]" + bcolors.ENDC

Osamah = bcolors.UNDERLINE + bcolors.BOLD + bcolors.HEADER + "Osamah [Busboy]" + bcolors.ENDC

user = "Name: "
user1 = "Name: "
user2 = "Name: "
user3 = "Name: "
user4 = "Name: "

import getpass

credentials = {}                                                            ## Sets up an array for the login credentials
with open('/Usernames.txt', 'r') as f:                                       ## Opens the file and reads it
    for line in f:  ## For each line
        username, password = line.strip().split(':')                        ## Separate each line into username and password, splitting after a colon
        credentials[username] = password                                    ## Links username to password

loop = 'true'

print bcolors.OKGREEN + "Login To Sheeba SKED 1.0" + bcolors.ENDC

while (loop == 'true'):

    username = raw_input("Please enter your username: ")                    ## Asks for username

    if (username in credentials):                                           ## If the username is in the credentials array
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("Please enter your password: ")      ## Asks for password
            if (password == credentials[username]):                         ## If the password is linked to the username
                print "Logged in successfully as " + username               ## Log in
                loop = 'false'
                loop1 = 'false'
            else:
                print "Password incorrect!"

    else:
        print "Username incorrect!"



# START HERE 

def my_add_fn():
   print "SUM:%s"%sum(map(int,raw_input("Enter 2 numbers seperated by a space: ").split()))


def my_waiters():
   print user + Abdulrahman
   print bcolors.WARNING + ("  Mon  | Tue  | Wed  | Thur | Fri  | Sat  | sun |  ") + bcolors.ENDC
   print("---------------------------------------------------")
   print bcolors.FAIL + ("       |      |      |      | 9-4  |4Close| 9-4 |  ") + bcolors.ENDC
   print("---------------------------------------------------")
   print user1 + Abdullah

   print bcolors.WARNING + ("  Mon  | Tue  | Wed  | Thur | Fri  | Sat  | sun |  ") + bcolors.ENDC
   print("---------------------------------------------------")
   print bcolors.FAIL + ("       |      |4Close|4Close|      |4Close|4Close|  ") + bcolors.ENDC
   print("---------------------------------------------------")

   print user2 + Ahmed


   print bcolors.WARNING + ("  Mon  | Tue  | Wed  | Thur | Fri  | Sat  | sun |  ") + bcolors.ENDC
   print("---------------------------------------------------")
   print bcolors.FAIL + ("4-Close|4Close|      |      |4Close|      |4Close|  ") + bcolors.ENDC
   print("---------------------------------------------------")

   print user3 + Fakri


   print bcolors.WARNING + ("  Mon  | Tue  | Wed  | Thur | Fri  | Sat  | sun |  ") + bcolors.ENDC
   print("---------------------------------------------------")
   print bcolors.FAIL + ("       |      |      |      |      | 9-4 |     |  ") + bcolors.ENDC
   print("---------------------------------------------------")



   print user4 + Osamah


   print bcolors.WARNING + ("  Mon  | Tue  | Wed  | Thur | Fri  | Sat  | sun |  ") + bcolors.ENDC
   print("---------------------------------------------------")
   print bcolors.FAIL + ("   9-4 |  9-4 |  9-4 |  9-4 |4Close|      |     |  ") + bcolors.ENDC
   print("---------------------------------------------------")



   print bcolors.OKGREEN + "Under Development" + bcolors.ENDC

def individual():
   print ("Hello")

def my_quit_fn():
   raise SystemExit

def invalid():
   print "INVALID CHOICE!"

menu = {"1":("Busboys",my_add_fn),
           "2":("Waiter/s)",my_waiters),
           "3":("Individual Lookup",individual),
           "4":("Quit",my_quit_fn),
          }
for key in sorted(menu.keys()):
     print key+":" + menu[key][0]

ans = raw_input("Make A Choice: ")
menu.get(ans,[None,invalid])[1]()
