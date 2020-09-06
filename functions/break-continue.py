
nums = [1, 15, 3, 17, 5, 6, 7, 8, 9, 10]
for num in nums:
    if num % 2 == 0:
        print(f'{num} is an EVEN number and exiting the loop..!!')
        # break
        continue
    else:
        print(f'{num} is an ODD number')

print(f'For loop broken at {num} !')
