import ttg

x = 0
cnf_bases = [['A', 'B'], ['A', 'B'], ['A', 'B'], ['A', 'B', 'C']]
cnf_formula = [['((~A) or (~B)) = ((~A) or (~B))'], ['(A => B) = ((~B) => (~A))'], 
              ['((A => B) and (B => A)) = (A = B)'], ['(A or B) and ((~B) or C) => A or C']]
formula = [['((~P) or P) and (R or (~R))'], ['((~C) or A or B) and ((~A) or C) and ((~B) or C)'], ['(B or C) and ((~C) or (~B)) and (~A) and (A)']]
bases = [['P', 'R'], ['A', 'B', 'C'], ['A', 'B', 'C']]
text = ['(a) ¬(A∧B) ⇔ ¬A∨¬B', '(b) A ⇒ B ⇔ ¬B ⇒ ¬A', '(c) ((A⇒B)∧(B ⇒A)) ⇔ (A ⇔ B)', '(d) (A∨B)∧(¬B ∨C)⇒(A∨C)']

#Function that gets an evaluation for each table whether it is TRUE, SATISFIABLE or UNSATISFIABLE
def get_evaluation(lst):
  
    data_frame = lst[0] 
    chk = True
    value = 1
      
    #Comparing each element with first item  
    for item in lst: 
        if data_frame != item: 
            chk = False
            break; 
              
    if (chk == True):
        for x in lst:
            value*=x
            #print(value)
        if value == 1:
            print("Evaluation: TRUE, Tautology, Valid")
        else:
            print("Evaluation: UNSATISTIABLE, Contradiction, Invalid")
        
    else: print("Evaluation: SATISFIABLE, Contingency, Invalid")             
  
#Proving the PL1 Problems
def problem1_solution():
    for i in range(4):
        truth_table = ttg.Truths(cnf_bases[i], cnf_formula[i])
        pandas_table = truth_table.as_pandas()
        models = 0
        for value in pandas_table[pandas_table.columns[-1]]:
            if value == 1:
                models +=1
        interpretations = ttg.Truths(cnf_bases[i], cnf_formula[i]).as_pandas()[cnf_formula[i]].values.tolist()
        expression = ttg.Truths(cnf_bases[i],cnf_formula[i]).as_pandas()[cnf_formula[i][0]].array
        print("\n", text[i])
        print(truth_table)
        print("Number of models: ", models)
        print("Number of interpretations: ", len(interpretations))
        get_evaluation(expression)
    
#Function to Evaluate a Propositional Logic that results to Tautology
def tautology_evaluator():
    tautology_table = ttg.Truths(bases[0],formula[0])
    tautology_pandas = tautology_table.as_pandas()
    tautology_models = 0
    tautology_interpretation = tautology_pandas.values.tolist()
    tautology_expression = ttg.Truths(bases[0], formula[0]).as_pandas()[formula[0][0]].array
    for value in tautology_pandas[tautology_pandas.columns[-1]]:
            if value == 1:
                tautology_models +=1
    print("\n ------------ Tautology Prover ------------")
    print(tautology_table)
    print("Number of models: ", tautology_models)
    print("Number of interpretations: ", len(tautology_interpretation))
    get_evaluation(tautology_expression)
    print("\n ------------------- End -------------------")
    print("\n \n")

#Function to Evaluate a Propositional Logic that results to Contingency
def contingency_evaluator():
    contingency_table = ttg.Truths(bases[1],formula[1])
    contingency_pandas = contingency_table.as_pandas()
    contingency_models = 0
    contingency_interpretation = contingency_pandas.values.tolist()
    contingency_expression = ttg.Truths(bases[1], formula[1]).as_pandas()[formula[1][0]].array
    for value in contingency_pandas[contingency_pandas.columns[-1]]:
            if value == 1:
                contingency_models +=1
    print("\n ------------------------- Contingency Prover -------------------------")
    print(contingency_table)
    print("Number of models: ", contingency_models)
    print("Number of interpretations: ", len(contingency_interpretation))
    get_evaluation(contingency_expression)
    print("\n --------------------------------- End ---------------------------------")
    print("\n \n")

#Function to Evaluate a Propositional Logic that results to Contradiction
def contradiction_evaluator():
    contradiction_table = ttg.Truths(bases[2],formula[2])
    contradiction_pandas = contradiction_table.as_pandas()
    contradiction_models = 0
    contradiction_interpretation = contradiction_pandas.values.tolist()
    contradiction_expression = ttg.Truths(bases[2], formula[2]).as_pandas()[formula[2][0]].array
    for value in contradiction_pandas[contradiction_pandas.columns[-1]]:
            if value == 1:
                contradiction_models +=1
    print("\n --------------------- Contradiction Prover ----------------------")
    print(contradiction_table)
    print("Number of models: ", contradiction_models)
    print("Number of interpretations: ", len(contradiction_interpretation))
    get_evaluation(contradiction_expression)
    print("\n ------------------------------ End ------------------------------")
    print("\n \n")


#Main Program is here which runs all the functions    
while x < 100:
    print("\n*************************************************")
    print("* Written by: Natalie Jane Pacificar BSCS 2B-AI *")
    print("* ---Theorem Prover for Propositional Logic---  *")
    print("*************************************************\n")
    print("1. Show evaluation in Problem 1")
    print("2. Choose from the given formula")
    print("3. Exit")

    choice = int(input("Enter your desired action: "))
    
    #1. Show evaluation in Problem 1
    if(choice == 1):
        problem1_solution()
        print("\nDo you want to exit? y/n")
        answer = str(input("> "))
        if answer.lower().startswith("y"):
            x = 101
        elif answer.lower().startswith("n"):
            pass
        
    #2. Choose from the given formula
    elif(choice == 2):
        print("\nChoose which logical statement to prove below:")
        print("1. Tautology: ((~P) or P) and (R or (~R))")
        print("2. Contingency: ((~C) or A or B) and ((~A) or C) and ((~B) or C)")
        print("3. Contradiction: (B or C) and ((~C) or (~B)) and (~A) and (A)")
        response = int(input("> "))
        if(response == 1):
            tautology_evaluator()
        elif(response == 2):
            contingency_evaluator()
        elif(response == 3):
            contradiction_evaluator()
        else:
            print("Oops. Try again with a valid response.")
    #3. Exit
    elif(choice == 3):
        x = 101
        
    else:
        print("Oops. Try again with a valid number.")
        
    x = x + 1
    



'''
Attributions. This program is not possible without their help.
1. Code snippet to get the number of models is grabbed from Carlo Antonio Taleon.
2. Reused a snippet from Geeks for Geeks. It served as a blueprint for me to come
   up with a solution to count the number of True Values and evaluate if these values
   is a tautolgy, contingency or a contradiction.
'''  

        

    















    
