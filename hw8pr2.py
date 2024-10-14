# hw8pr2.py
# Dora Ding

def string_times(str, n):
  return n * str

def front_times(str, n):
  return n * str if len(str) <= 3 else n * str[:3]

def string_bits(str):
  return str[0::2]

def string_splosion(str):
  answer = ''
  for i in range(len(str)):
    answer += str[:i + 1]
  return answer

def last2(str):
  if len(str) < 2:
      return 0
  end = str[-2:]
  count = 0
  for i in range(len(str) - 2):
      if str[i:i + 2] == end:
          count += 1
  return count

def array_count9(nums):
  return nums.count(9)

def array_front9(nums):
  if len(nums) < 4:
    return True if nums.count(9) > 0 else False
  return True if nums[:4].count(9) > 0 else False

def array123(nums):
  for i in range(len(nums) - 2):
    if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
      return True
  return False

def string_match(a, b):
  count = 0
  for i in range(min(len(a),len(b)) - 1):
    if a[i:i + 2] == b[i:i + 2]:
      count += 1
  return count

def count_evens(nums):
  return len([x for x in nums if x % 2 == 0])

def big_diff(nums):
  difference = 0
  for i in nums:
    for ii in nums:
      if abs(i - ii) > difference:
        difference = abs(i - ii)
  return difference

def centered_average(nums):
  nums.remove(min(nums))
  nums.remove(max(nums))
  return sum(nums) // len(nums)

def sum13(nums):
  n = [x for x in nums]
  for i in range(len(nums)):
    if nums[i] == 13 or (nums[i - 1] == 13 and i != 0):
      n.remove(nums[i])
  return sum(n)

def sum67(nums):
  total = 0
  ignoring = False
  for num in nums:
    if num == 6:
      ignoring = True
    if not ignoring:
      total += num
    if num == 7 and ignoring:
      ignoring = False
  return total

def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2 and nums[i + 1] == 2:
      return True
  return False

def double_char(str):
  result = ''
  for c in str:
    result += c * 2
  return result

def count_hi(str):
  return str.count("hi")

def cat_dog(str):
  return str.count('cat') == str.count('dog')

def count_code(str):
  return sum(1 for i in range(len(str) - 3) if str[i:i + 2] == 'co' and str[i + 3] == 'e')

def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a.endswith(b) or b.endswith(a)

def xyz_there(str):
  for i in range(len(str) - 2):
    if str[i:i + 3] == "xyz" and (i == 0 or str[i - 1] != "."):
      return True
  return False