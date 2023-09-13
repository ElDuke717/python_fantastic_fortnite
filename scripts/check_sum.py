# check_sum takes in a list and returns True if the sum of two of the numbers in the list equals zero

# We'll use a hashmap to determine the answer

# define check_sum, takes a list as argument
def check_sum(num_list):
    # declare map, assigned to a set
    seen = set()
    # loop over the list
    for num in num_list:
        if -num in seen:
            return True
        seen.add(num)
    return False


numsList = input("input a list of numbers: ")
print(type(numsList))
print(check_sum(numsList))
