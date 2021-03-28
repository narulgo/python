
def add_list(numbers1, numbers2):
    loop = abs(len(numbers1)-len(numbers2))
    
    if len(numbers1) < len(numbers2):
        for i in range(loop):
            #i = i * 0
            numbers1.append(0)
        
        
    if len(numbers1) > len(numbers2):
        for i in range(loop):
            #i = i * 0
            numbers2.append(0)
        
        
    if len(numbers1) == len(numbers2):
        new = []
        for x in range(len(numbers1)):
            sum1 = numbers1[x] + numbers2[x]
            new.append(sum1)
        return new
        
                
        
           
print(add_list([1, 2, 3, 5,  8, 9], [3, 4, 5]))
print(add_list([1, 2, 3], [4, 5, 6, 7, 8]))
print(add_list([1,2,3], [3,7,5]))


