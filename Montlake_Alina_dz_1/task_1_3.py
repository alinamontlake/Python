for variable_for_procent in range (1,101,1):
    if ((variable_for_procent % 10) == 1 and not variable_for_procent == 11):
        print (str(variable_for_procent) + ' процент')
    elif (((variable_for_procent % 10) == 2) or ((variable_for_procent % 10) == 3) or ((variable_for_procent % 10) == 4)) and not (variable_for_procent == 12) and not (variable_for_procent == 13) and not (variable_for_procent == 14):
            print (str(variable_for_procent) + ' процента')
    else:
                print (str(variable_for_procent) + ' процентов')
            
