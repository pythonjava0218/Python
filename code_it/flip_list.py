numbers = [2, 4, 6, 8, 10, 12, 14]
 
for left_index in range(0, int(len(numbers) / 2)):
    right_index = len(numbers) - left_index - 1

    temp = numbers[left_index]
    numbers[left_index] = numbers[right_index]
    numbers[right_index] = temp
print(numbers)
    
    
    

 
               
