#Jedlueng 
#19 September 2021

birth_years = [1995, 2004, 2019, 1988, 1977, 1902]

#your code goes here
def cal(birth_year):
    return(2050-birth_year) 


print(list(map(cal,birth_years)))