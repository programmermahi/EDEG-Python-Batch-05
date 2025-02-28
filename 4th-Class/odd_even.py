odd_sum = 0
even_sum = 0

odd_number = 1
while odd_number <= 20:
    odd_sum += odd_number  
    odd_number += 2  


print("Odd Sum:",odd_sum)
even_number = 20
while even_number >= 1:
    even_sum += even_number  
    even_number -= 2  
print("even_sum:",even_sum)

total_result = odd_sum + even_sum
print(f"The total sum of odd numbers from 1 to 20 and even numbers from 20 to 1 is: {total_result}")
