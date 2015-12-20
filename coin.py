import random
import Tkinter
coin=["Heads", "Tails"]
random.shuffle(coin)
flippedcoin=[]
flip=raw_input("Press Y to flip and N to exit")
while flip=="Y" :
 flippedcoin+=[coin.pop()]
 print "The result is: ", flippedcoin
 coin=coin+flippedcoin
 random.shuffle(coin)
 flippedcoin=[]
 flip=raw_input("Press Y to flip and N to exit")

