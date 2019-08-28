import random
import itertools

# 사용자가 변경할 수 있는 부분
# 시뮬레이션 반복 시행 횟수
numRepeatSimulation = 100
numGamesPerWeek = 1000

# 1년동안 로또를 사는 횟수(52주)
numWeeks = 52


#로또 1000원으로 바뀐 후 각 등수당 평균 당첨금액
first_prize = 2439639208
second_prize = 57199661
third_prize = 1451702
fourth_prize = 50000
fifth_prize = 5000

lottoBeginNum = 1 
lottoEndNum = 45 
priceOneGame = 1000
simulatedFirstPrizeNumbersList  = 0
simulatedSecondPrizeNumbersList  = 0
simulatedThirdPrizeNumbers  = 0
simulatedFourthPrizeNumbersList  = 0
simulatedFifthPrizeNumbersList  = 0


totalGain = 0
totalLoss = 0
totalCountFirstPrize = 0
totalCountSecondPrize = 0
totalCountThirdPrize = 0
totalCountFourthPrize = 0
totalCountFifthPrize = 0

for q in range(0, numRepeatSimulation):  
  print("Phase #", q)
  for i in range(0, numWeeks):
    simulatedFifthPrizeNumbersList = random.sample(range(lottoBeginNum,lottoEndNum+1),7) 
    simulatedBonusNumber  = simulatedFifthPrizeNumbersList.pop(random.randint(0,6))
    simulatedFifthPrizeNumbersList.sort()
    
    thirdPrizeCombinations = list(itertools.combinations(simulatedFifthPrizeNumbersList, 5))
    fourthPrizeCombinations = list(itertools.combinations(simulatedFifthPrizeNumbersList, 4))
    fifthPrizeCombinations = list(itertools.combinations(simulatedFifthPrizeNumbersList, 3))
    
    simulatedSecondPrizeNumbersList=[0] * 6
    simulatedThirdPrizeNumbers=[0] * 6
    simulatedFourthPrizeNumbersList=[0] * 15
    simulatedFifthPrizeNumbersList=[0] * 20  
    
    for i, _ in enumerate(thirdPrizeCombinations):
      simulatedSecondPrizeNumbersList[i] = list(thirdPrizeCombinations[i])
      simulatedSecondPrizeNumbersList[i].append(int(simulatedBonusNumber))
      simulatedSecondPrizeNumbersList[i].sort()
    for i, _ in enumerate(thirdPrizeCombinations):
      simulatedThirdPrizeNumbers[i] = list(thirdPrizeCombinations[i])
      simulatedThirdPrizeNumbers[i].sort()
    for i, _ in enumerate(fourthPrizeCombinations):
      simulatedFourthPrizeNumbersList[i] = list(fourthPrizeCombinations[i])
      simulatedFourthPrizeNumbersList[i].sort()
    for i, _ in enumerate(fifthPrizeCombinations):
      simulatedFifthPrizeNumbersList[i] = list(fifthPrizeCombinations[i])
      simulatedFifthPrizeNumbersList[i].sort()
 

    countFirstPrize = 0
    countSecondPrize = 0
    countThirdPrize = 0
    countFourthPrize = 0
    countFifthPrize = 0
    countGames = 0
    while countGames < numGamesPerWeek: 
      retry = False  
      myNumbersList = random.sample(range(lottoBeginNum, lottoEndNum + 1), 6) 
      myNumbersList.sort()
      myNumbersForFifthPrizeCombinations = list(itertools.combinations(myNumbersList, 3))
      myNumbersForFourthPrizeCombinations = list(itertools.combinations(myNumbersList, 4))
      myNumbersForThirdPrizeCombinations = list(itertools.combinations(myNumbersList, 5))
      myNumbersForFifthPrizeList = [0] * 20
      myNumbersForFourthPrizeList = [0] * 15
      myNumbersForThirdPrizeList =[ 0] * 6
      myNumbersForSecondPrizeList = [0] * 6
      myNumbersForFirstPrizeList = myNumbersList
      
      for i, _ in enumerate(myNumbersForThirdPrizeCombinations):
        myNumbersForSecondPrizeList[i] = list(myNumbersForThirdPrizeCombinations[i])
        myNumbersForSecondPrizeList[i].sort()
      for i, _ in enumerate(myNumbersForThirdPrizeCombinations):
        myNumbersForThirdPrizeList[i] = list(myNumbersForThirdPrizeCombinations[i])
        myNumbersForThirdPrizeList[i].sort()        
      for i, _ in enumerate(myNumbersForFourthPrizeCombinations):
        myNumbersForFourthPrizeList[i] = list(myNumbersForFourthPrizeCombinations[i])
        myNumbersForFourthPrizeList[i].sort()
      for i, _ in enumerate(myNumbersForFifthPrizeCombinations):
        myNumbersForFifthPrizeList[i] = list(myNumbersForFifthPrizeCombinations[i])
        myNumbersForFifthPrizeList[i].sort()

     
      if simulatedFirstPrizeNumbersList == myNumbersForFirstPrizeList:
        countFirstPrize += 1
        retry = True
      
      if retry == False:        
        for k in range(len(simulatedSecondPrizeNumbersList)):
          if retry == False:
            for m in range(len(simulatedSecondPrizeNumbersList)):
              if simulatedSecondPrizeNumbersList[k] == myNumbersForSecondPrizeList[m]:
                countSecondPrize += 1
                retry = True
                break 
              
      if retry == False:        
        for k in range(len(simulatedThirdPrizeNumbers)):
          if retry == False:
            for m in range(len(simulatedThirdPrizeNumbers)):
              if simulatedThirdPrizeNumbers[k] == myNumbersForThirdPrizeList[m]:
                countThirdPrize += 1
                retry = True
                break 
              
      if retry == False:        
        for k in range(len(simulatedFourthPrizeNumbersList)):
          if retry == False:
            for m in range(len(simulatedFourthPrizeNumbersList)):
              if simulatedFourthPrizeNumbersList[k] == myNumbersForFourthPrizeList[m]:
                countFourthPrize += 1
                retry = True
                break 
      if retry == False:        
        for k in range(len(simulatedFifthPrizeNumbersList)):
          if retry == False:
            for m in range(len(simulatedFifthPrizeNumbersList)):
              if simulatedFifthPrizeNumbersList[k] == myNumbersForFifthPrizeList[m]:
                countFifthPrize += 1
                retry = True
                break        

      countGames += 1


    totalGain += countFirstPrize * first_prize 
    totalGain += countSecondPrize * second_prize
    totalGain += countThirdPrize * third_prize
    totalGain += countFourthPrize * fourth_prize
    totalGain += countFifthPrize * fifth_prize
    totalCountFirstPrize += countFirstPrize
    totalCountSecondPrize += countSecondPrize
    totalCountThirdPrize += countThirdPrize
    totalCountFourthPrize += countFourthPrize
    totalCountFifthPrize += countFifthPrize
  totalLoss += numWeeks * numGamesPerWeek * priceOneGame
  
totalCountFirstPrize /= numRepeatSimulation
totalCountSecondPrize /= numRepeatSimulation
totalCountThirdPrize /= numRepeatSimulation
totalCountFourthPrize /= numRepeatSimulation
totalCountFifthPrize /= numRepeatSimulation
totalGain /= numRepeatSimulation
totalLoss /= numRepeatSimulation
totalGain -= totalLoss


print("1년 (총 52주)")
print("주당 게임 총 회수: ", numGamesPerWeek, "(총 투자액:",  totalLoss,"원)")
print("1등 당첨회수: ", totalCountFirstPrize, "(1등 당첨시 :",  first_prize,"원)")
print("2등 당첨회수: ", totalCountSecondPrize, "(2등 당첨시 :",  second_prize,"원)")
print("3등 당첨회수: ", totalCountThirdPrize, "(3등 당첨시 :",  third_prize,"원)")
print("4등 당첨회수: ", totalCountFirstPrize, "(4등 당첨시 :",  fourth_prize,"원)")
print("5등 당첨회수: ", totalCountFifthPrize, "(5등 당첨시 :",  fifth_prize,"원)")
print("이득: ", totalGain, "원") 
