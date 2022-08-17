#虚假姓名生成器
import sys, random

first = ("Baby Oil", "Bad News")

last = ("App","Big")

firstname = random.choice(first)
lastname = random.choice(last)

print("{} {}".format(firstname, lastname), file=sys.stderr)
