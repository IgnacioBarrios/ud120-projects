#!/usr/bin/python

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    points_removed = 9
    cleaned_data = []

    ### your code goes here
    # Error sin ordenar
    Error = (net_worths - predictions) ** 2
    
    # Ordenamos los errores para ver cual es error máximo permitido
    error = sorted(Error)
    
    # Valor de error máximo no admisible 
    lower_error = error[-points_removed]
     
    j = 0
    for error in Error:
        if error < lower_error:
            cleaned_data.append([ages[j], net_worths[j], error])
            
        j = j +1
    
    #cleaned_data = [ages_clean,net_worths_clean,error_clean]   
        
    return cleaned_data

