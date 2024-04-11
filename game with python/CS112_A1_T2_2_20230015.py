
#purpose : game to take number from 1 to 9 and try to get 15 by 3 numbers
#Author : Ahmed Hussein Ahmed Mohammed   
# Date March 29 , 2024


print ("****************************************")
print ("********* Number scrabble **************")
print ("****************************************")
print (" ")


print ("Some rules to play ")
print (" ")
print("   1- The game is played by 2 players") 
print("   2- Each player can take a number from 1 to 9")
print("   3- The number that is taken cannot be taken again  ")
print("   4- The player wins if has picked 3 numbers that add up to 15")
print("   5- If all the numbers are used and no player gets exactly 15 , the game is a draw ")
print (" ")
print ("Have a nice game.")
print (" ")
print ("=================================================================================")
print (" ")


# array to store the numbers that the player will take, in order to exchange the value of each number for the numbers taken by the player
total_num_1=[100,100,100,100,100]  
total_num_2=[100,100,100,100] 
# the list will appear for players to choose from
list =[1,2,3,4,5,6,7,8,9] 

n=0
m=0
a=0 # to get out from loop 

while len(list)>0:
  
  print ("player 1 takes a number from the list  ") 
  print (list)
  num_1=int(input ())
  if  num_1 in list :
    total_num_1[n]=num_1
    n=n+1
    list.remove(num_1)
    
  else :
     print ("The number doesn't exist ")
     continue
  
  if total_num_1[0]+total_num_1[1]+total_num_1[2]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[0]+total_num_1[2]+total_num_1[3]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[0]+total_num_1[3]+total_num_1[4]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[1]+total_num_1[2]+total_num_1[3]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[0]+total_num_1[2]+total_num_1[4]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[0]+total_num_1[1]+total_num_1[3]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[0]+total_num_1[1]+total_num_1[4]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[1]+total_num_1[2]+total_num_1[4]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[3]+total_num_1[1]+total_num_1[4]==15:
    print("player 1 win ")
    break
  
  elif  total_num_1[3]+total_num_1[2]+total_num_1[4]==15:
    print("player 1 win ")
    break
  
  elif len(list)==0:
    a=5
    break

  
  print ("player 2 takes a number from the list  ") 
  print (list)
  num_2=int(input ())  
  
  if  num_2 in list :
   total_num_2[m]=num_2
   m=m+1
   list.remove(num_2)
   
  else :
     while True:
      print ("The number doesn't exist ")
      print ("player 2 takes a number from the list  ") 
      print (list)
      num_2=int(input ())
      
      if  num_2 in list :
       total_num_2[m]=num_2
       m=m+1
       list.remove(num_2)
       break
      
  if total_num_2[0]+total_num_2[1]+total_num_2[2]==15:
     print("player 2 win ")
     break
  
  elif  total_num_2[0]+total_num_2[2]+total_num_2[3]==15:
    print("player 2 win ")
    break
  
  elif  total_num_2[1]+total_num_2[2]+total_num_2[3]==15:
    print("player 2 win ")
    break
  
  elif  total_num_2[0]+total_num_2[1]+total_num_2[3]==15:
    print("player 2 win ")
    break
  
if a==5:
    print("draw")


 
  