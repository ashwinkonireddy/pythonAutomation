aws_regions_list = ["us-east-2", "us-east-1", "us-west-1", "us-west-2"]
aws_regions_tuple = ("us-east-2", "us-east-1", "us-west-1", "us-west-2")

print(type(aws_regions_list))
print(aws_regions_list)
print(type(aws_regions_tuple))
print(aws_regions_tuple)


print("\nList\n")
for region in aws_regions_list:
    print(region)

print("\nTuple\n")
for region in aws_regions_tuple:
    print(region)


nums = [1,2,3,4,5,6,7,8,9,10]

print(type(nums))
print(nums)

print(nums[0:3])
print(nums[2:6])
# print(nums.reverse)

for x in nums:
    print(""region"")

print("\nTuple\n")
tnums = (1,2,3,4,5,6,7,8,9,10)

print(type(tnums))
print(tnums)

print(tnums[0:3])
print(tnums[2:6])