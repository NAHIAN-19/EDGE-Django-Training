# Set operations to find same values and different values
def setOperations(set_of_names_1, set_of_names_2):
    # Intersection finds the same values in both
    names_in_both_sets = set_of_names_1.intersection(set_of_names_2)
    
    names_not_in_both_sets = set_of_names_1.symmetric_difference(set_of_names_2)
    
    return names_in_both_sets, names_not_in_both_sets

def home():
    set_of_names_1 = {'Nahian', 'Rafi', 'Rayhan', 'Mamun', 'Faisal'}
    set_of_names_2 = {'Amirul', 'Rifat', 'Faisal', 'Kashfi'}
    
    names_in_both_sets, names_not_in_both_sets = setOperations(set_of_names_1, set_of_names_2)
    
    print("Names in both sets : ",names_in_both_sets)
    print("Names in only one set : ",names_not_in_both_sets)
    
home() 
                