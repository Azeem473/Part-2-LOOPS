num = int(input("Enter number: "))
sum_even = 0
sum_odd = 0
for i in range (1,num + 1):
    if i % 2 == 0:
        sum_even+=i
        print(f"Sum of even numbers up to {num}: {sum_even}")
    else:
        sum_odd+=i
        print(f"Sum of even numbers up to {num}: {sum_odd}")
        
