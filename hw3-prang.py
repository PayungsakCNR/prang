import itertools
import math
import string

x0, y0 = (0, 0)
x1, y1 = (string.ascii_lowercase.index('p')+1,
           string.ascii_lowercase.index('k')+1)
x2, y2 = (54, 167)
x3, y3 = (38, 33)
c0 = [x0, y0]
c_list = [[x1, y1], [x2, y2], [x3, y3]]

def dist(ci, cj):
    return math.sqrt((cj[0]-ci[0]) ** 2 + (cj[1]-ci[1]) ** 2)

print(dist(c0,c_list[0]))
print(dist(c_list[0],c_list[1]))
print(dist(c_list[1],c_list[2]))
print(dist(c_list[2],c0))

print('Total')
print(dist(c0,c_list[0]) + dist(c_list[0],c_list[1]) + dist(c_list[1],c_list[2]) + dist(c_list[2],c0))

def dist_total(c0, c_list):
#     # Use given dist() function to calculate c0 --> c_list[0]
    tot = dist(c0, c_list[0])
#     # Use for loop to calculate distance of
#     # c_list[0] --> c_list[0+1=1]
#     # c_list[1] --> c_list[1+1=2]
    for i in range(len(c_list)-1):
        tot = tot + dist(c_list[i], c_list[i+1])
#     # Calculate c_list[2] --> c0
    tot = tot + dist(c_list[2], c0)
    return tot

print(dist_total(c0,c_list))

perm_of_city = list(itertools.permutations(c_list))
# # Print the requested output
print('The permutations of the cities are: ')
for a_perm in perm_of_city:
    print(perm_of_city)


# # (e) Use the 1st permutation (index0) to calculate the total distance
#print('The total distance to travelling using the 1st permutation:')
#print(f'Route= {perm_of_city[0]}, Distance= {dist_total(XX, XX)}')

'''
[0,0]
[16, 11]
[54, 167]
[38, 33]
[0,0]
'''
#print(perm_of_city[0][0])
#print(perm_of_city[0][1])
#print(perm_of_city[0][2])

# # (e) Use the 1st permutation (index0) to calculate the total distance
print('The total distance to travelling using the 1st permutation:')
print(f'Route= {perm_of_city[0]}, Distance= {dist_total(c0, perm_of_city[0])}')

print('The total distance for each permutation:')
#print(perm_of_city[0])
#print(perm_of_city[1])

dist_total_keep = []
for i in range(len(perm_of_city)):
    d = dist_total(c0, perm_of_city[i])
    print(f'Route= {perm_of_city[i]}, Distance= {d}')
    dist_total_keep.append(perm_of_city[i])
d_keep_min = min(dist_total_keep) # Find the minimum distance
d_keep_ind = dist_total_keep.index(d_keep_min) # Find the index
perm_min = perm_of_city[d_keep_ind] # Find the permutation of the index
print(f'The Travelling route is {perm_of_city[d_keep_ind]}')
print(f'The minimum distance is {dist_total(c0, perm_of_city[d_keep_ind])}.')




# # (f) Use for loop to calculate total distance for all permutations.
#dist_total_keep = [] # Keep the total distance for each permutation.
#print('The total distance for each permutation:')
#for perm_i in perm_of_city:
    #d = dist_total(perm_of_city[perm_i][0], perm_of_city[perm_i])
#     # Printout each permutation and total distance
    #print(f'Route= {perm_of_city[perm_i]}, Distance= {d}')
    #print(f'Route= perm_of_city[perm_i]')
    #print(perm_of_city[perm_i])
    #dist_total_keep.append(perm_of_city[perm_i])
#d_keep_min = min(dist_total_keep) # Find the minimum distance
#d_keep_ind = dist_total_keep.index(d_keep_min) # Find the index
#perm_min = perm_of_city[d_keep_ind] # Find the permutation of the index
#print(f'The Travelling route is {perm_of_city[d_keep_ind]}')
#print(f'The minimum distance is {d_keep_min}.')
