# # Python function to print permutations of a given list
# def permutation(lst):
 
#     # If lst is empty then there are no permutations
#     if len(lst) == 0:
#         return []
 
#     # If there is only one element in lst then, only
#     # one permutation is possible
#     if len(lst) == 1:
#         return [lst]
 
#     # Find the permutations for lst if there are
#     # more than 1 characters
 
#     l = [] # empty list that will store current permutation
 
#     # Iterate the input(lst) and calculate the permutation
#     for i in range(len(lst)):
#        m = lst[i]
 
#        # Extract lst[i] or m from the list.  remLst is
#        # remaining list
#        remLst = lst[:i] + lst[i+1:]
 
#        # Generating all permutations where m is first
#        # element
#        for p in permutation(remLst):
#            l.append([m] + p)
#     return l
 
 
# # Driver program to test above function
# data = list('abc')
# ans = permutation(data)
# print(ans)


# def permute(num):
#     if len(num) == 2:
#         # get the permutations of the last 2 numbers by swapping them
#         yield num
#         num[0], num[1] = num[1], num[0]
#         yield num
#     else:
#         for i in range(0, len(num)):
#             # fix the first number and get the permutations of the rest of numbers
#             for perm in permute(num[0:i] + num[i+1:len(num)]):
#                 yield [num[i]] + perm

# for p in permute(["a", "b", "c"]):
#     print(p)



def per(lst):
    if len(lst) == 2:
        yield lst
        lst[0], lst[1] = lst[1], lst[0]
        yield lst
    for i in range(len(lst)):
        c = lst[i]    
        newlst = lst[:i] + lst[i + 1:]
        for p in per(newlst):
            yield [c] + p

for _ in per(["a", "b", "c"]):
    print(_)