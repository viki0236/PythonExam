text = [int(el) for el in input().split(", ")]
inex = int(input())
nums ={}
s = 0
for ind in enumerate(text):
  nums[ind[0]] = ind[1]
sort_nums = sorted(nums.items(), key=lambda x: x[1])


for key, vel in sort_nums:
    if key != inex:
        s += vel
    else:
        s += vel
        break
print(s)