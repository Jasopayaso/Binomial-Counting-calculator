import math



def main():
    functionWanted = input('What is the topic do you need: ')


    #if the user wants a binomial distribution calculator
    if 'binomial' in functionWanted:
         #runs the binomial attributes function that asks the user for the inputs
         binomialQuestions = binomial_attributes()
         #runs the binomial distribution function and returns the output
         binomialAnswers = binomial_distribution(binomialQuestions[0], binomialQuestions [1], binomialQuestions[2])
         print(
               f'The binomial mean is {binomialAnswers[0]} \n'
               f'The standard deviation is {binomialAnswers[1]}\n'
               f'The binomial probability of x={binomialQuestions[2]} is {binomialAnswers[2]}'
        )  
         
    #if the user wants to use the counting calculator
    if 'counting' in functionWanted:
         while True:
             factorialCheck = input('Are you selecting a specific amount from a larger sample? (y/n): ')
             if factorialCheck.lower() not in ('y' , 'n'):
                print('Please pick y or n')
             else:
                break
          
         if factorialCheck == 'n':
            factorialNumber = int(input("What's the number that you want to count from: "))
            print(math.factorial(factorialNumber))
         else:
            countingQuestions = counting_attributes()
            countingAnswers = counting_techniques(countingQuestions[0], countingQuestions[1], countingQuestions[2])
            print(f'There are {countingAnswers} possible outcomes')

def counting_attributes():
     """Asks the user for the attributes for the current problem"""

     totalObjects = int(input('What is the total amount of objects being counted: '))
     sampleChosen = int(input('What is the amount you want from the total: '))
     while True:
         permutationCheck = input('Does the order matter (y/n): ')
         if permutationCheck.lower() not in ('y' , 'n'):
             print('Please pick y or n')
         else:
            break

     return totalObjects , sampleChosen, permutationCheck


def binomial_attributes():
    #asking the users for the values
    successProbability = float(input('What is the success probability of the binomial distribution (input in decimal form):'))
    fixedTrials = int(input('What is the numbers of fixed trials: '))
    numberOfSuccess = int(input('What is the number of successes you want to compute: '))

    #returns the outputs in a tuple
    return successProbability, fixedTrials, numberOfSuccess

def binomial_distribution(successProbability, fixedTrials, numberOfSuccess):

    #initialize the permutationCheck to be 'n' to run the combination formula
    permutationCheck = 'n'
    #binomial distribution calculations
    binomialMean = float(fixedTrials * successProbability)
    binomialStandardDeviation = float(math.sqrt(binomialMean * (1 - successProbability)))
    binomialProbability = counting_techniques(fixedTrials, numberOfSuccess, permutationCheck) * (successProbability ** \
                                                                                                 (numberOfSuccess)) * ((1 - successProbability) ** (fixedTrials - numberOfSuccess))

    #output
    return "%.2f" % binomialMean, "%.2f" % binomialStandardDeviation, "%.4f" % binomialProbability

def counting_techniques(totalObjects, sampleChosen, permutationCheck):
    """Runs the permutations and combinations formula depending on the situation"""

    #the permutation formula 
    def permutation(totalObjects, sampleChosen):
         """the permuation formula used in statistics"""
         permutationsCalculator = math.factorial(totalObjects) / math.factorial(totalObjects - sampleChosen)
         return permutationsCalculator
    
    #the combination formula   
    def combination(totalObjects, sampleChosen):
         """the combination formula used in statistics"""
         combinationsCalculator = permutation(totalObjects, sampleChosen) / math.factorial(sampleChosen)
         return combinationsCalculator

    #asks the user if order matters in order to perform the correct calculation as well as user validation for y/n

    #runs the respective calculator after finding out if the order/arragement matters
    if permutationCheck == 'y':
        return permutation(totalObjects, sampleChosen)
    elif permutationCheck == 'n':
        return combination(totalObjects, sampleChosen)
    





if __name__ == '__main__':
        main()

