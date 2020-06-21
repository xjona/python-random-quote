import random

def quelle():
    #print("Keep it logically awesome.")

  f = open("quotes.txt") #f is variable
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd]) #starts with 0

if __name__== "__main__":
  quelle()
