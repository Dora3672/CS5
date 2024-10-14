#
# Filename: hw2pr4.py
#

### Warmup-1 > sleep_in
def sleep_in(weekday, vacation):
  return True if not weekday or vacation else False

### Warmup-1 > monkey_trouble
def monkey_trouble(a_smile, b_smile):
  return (a_smile == b_smile)

### Warmup-1 > sum_double
def sum_double(a, b):
  return int(a+b) if a != b else int(2*(a+b))

### Warmup-1 > diff21
def diff21(n):
  return 21-n if 21>int(n) else 2*(n-21)

### Warmup-1 > parrot_trouble
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

### Warmup-1 > makes10
def makes10(a, b):
  return True if a+b==10 or a==10 or b==10 else False

### Warmup-1 > near_hundred
def near_hundred(n):
  return True if abs(n-100)<=10 or abs(n-200)<=10 else False

### Warmup-1 > pos_neg
def pos_neg(a, b, negative):
  if negative:
    return True if a<0 and b<0 else False
  return True if (a<0 and b>0) or (a>0 and b<0) else False

### Warmup-1 > not_string
def not_string(str):
  if str[:3] != 'not' or len(str)<3:
    return 'not ' + str
  return str

### Warmup-1 > missing_char
def missing_char(str, n):
  return str[:n] + str[n+1:]

### Warmup-1 > front_back
def front_back(str):
  if len(str) <= 1:
    return str
  return str[len(str)-1] + str[1:len(str)-1] + str[0]

### Warmup-1 > front3
def front3(str):
  return 3*str if len(str)<=3 else 3*str[:3]

### String-1 > hello_name
def hello_name(name):
  return "Hello "+name+"!"

### String-1 > make_abba
def make_abba(a, b):
  return a+b+b+a

### String-1 > make_tags
def make_tags(tag, word):
  return '<'+tag+'>'+word+'</'+tag+'>'

### String-1 > make_out_word
def make_out_word(out, word):
  return out[:len(out)/2]+word+out[len(out)/2:]

### String-1 > extra_end
def extra_end(str):
  return str[-2:]*3

### String-1 > first_two
def first_two(str):
  return str if len(str)<2 else str[:2]

### String-1 > first_half
def first_half(str):
  return str[:len(str)/2]

### String-1 > without_end
def without_end(str):
  return str[1:-1]

### String-1 > combo_string
def combo_string(a, b):
  return a+b+a if len(a)<len(b) else b+a+b

### String-1 > non_start
def non_start(a, b):
  return a[1:]+b[1:]

### String-1 > left2
def left2(str):
  return str[2:]+str[:2]

### List-1 > first_last6
def first_last6(nums):
  return True if 6 in [nums[0], nums[-1]] else False

### List-1 > same_first_last
def same_first_last(nums):
  return len(nums)>0 and nums[0]==nums[-1] 

### List-1 > make_pi
def make_pi():
  return [3, 1, 4]

### List-1 > common_end
def common_end(a, b):
  return (a[0]==b[0] or a[-1]==b[-1])

### List-1 > sum3
def sum3(nums):
  return sum(nums)  

### List-1 > rotate_left3
def rotate_left3(nums):
  return nums[1:]+[nums[0]]

### List-1 > reverse3
def reverse3(nums):
  return nums[::-1]

### List-1 > max_end3
def max_end3(nums):
  return [max(nums[0],nums[-1])]*3

### List-1 > sum2
def sum2(nums):
  return sum(nums[:2]) if len(nums)>2 else sum(nums)

### List-1 > middle_way
def middle_way(a, b):
  return [a[1], b[1]]

### List-1 > make_ends
def make_ends(nums):
  return [nums[0], nums[-1]]

### List-1 > has23
def has23(nums):
  return (2 in nums or 3 in nums)

### Logic-1 > cigar_party
def cigar_party(cigars, is_weekend):
  return (39<cigars<61 or (is_weekend and 39<cigars))

### Logic-1 > date_fashion
def date_fashion(you, date):
  if you <=2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
     return 2
  return 1
  
### Logic-1 > squirrel_play
def squirrel_play(temp, is_summer):
  return 59<temp<91 if not is_summer else 59<temp<101

### Logic-1 > caught_speeding
def caught_speeding(speed, is_birthday):
  if 60>=speed or (65>=speed and is_birthday):
    return 0
  elif 60<speed<81 or (60<speed<86 and is_birthday):
    return 1
  return 2

### Logic-1 > sorta_sum
def sorta_sum(a, b):
  return 20 if 9<a+b<20 else a+b

### Logic-1 > alarm_clock
def alarm_clock(day, vacation):
  if 0<day<6 and not vacation:
    return "7:00"
  elif (0<day<6 and vacation) or ((day==0 or day==6) and not vacation):
    return "10:00"
  return "off"

### Logic-1 > love6
def love6(a, b):
  return (a==6 or b==6 or a+b==6 or abs(b-a)==6)

### Logic-1 > in1to10
def in1to10(n, outside_mode):
  if outside_mode:
    return n<=1 or n>=10
  return n in list(range(1,11))

### Logic-1 > near_ten
def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8

### Logic-2 > make_bricks
def make_bricks(small, big, goal):
    goal -= min(big, goal // 5) * 5
    return goal <= small

### Logic-2 > lone_sum
def lone_sum(a, b, c):
    if a == b == c:
        return 0
    elif a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a + b + c
    
### Logic-2 > lucky_sum
def lucky_sum(a, b, c):
    if 13 in [a, b, c]:
        index_of_13 = [a, b, c].index(13)
        if index_of_13 == 0:
            return 0
        elif index_of_13 == 1:
            return a
        else:
            return a + b
    else:
        return a + b + c

### Logic-2 > no_teen_sum
def no_teen_sum(a, b, c):
  def fix_teen(n):
    if n not in [13,14,17,18,19]:
      return n
    return 0
  return fix_teen(a) + fix_teen(b) + fix_teen(c)

### Logic-2 > round_sum
def round_sum(a, b, c):
  def round10(num):
    if num%10 <5:
      return num//10 * 10
    return (num//10 + 1) * 10
  return round10(a) + round10(b) + round10(c)

### Logic-2 > close_far
def close_far(a, b, c):
    is_b_close = abs(a - b) <= 1
    is_c_close = abs(a - c) <= 1
    is_b_far = abs(b - a) >= 2 and abs(b - c) >= 2
    is_c_far = abs(c - a) >= 2 and abs(c - b) >= 2
    return (is_b_close and is_c_far) or (is_c_close and is_b_far)

### Logic-2 > make_chocolate
def make_chocolate(small, big, goal):
   b = min(big, goal//5)
   return goal - b*5 if goal-b*5<=small else -1