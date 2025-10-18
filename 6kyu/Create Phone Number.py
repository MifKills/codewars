# Solution with str.format()
# def create_phone_number(n):
# return "({}{}{}) {}{}{}-{}{}{}{}".format(*n) # '*' unwrap a list, tuple, etc.

# Solution with a generator expression
# def create_phone_number(n):
#   str1 =  ''.join(str(x) for x in n[0:3])
#   str2 =  ''.join(str(x) for x in n[3:6])
#   str3 =  ''.join(str(x) for x in n[6:10])
#   return '({}) {}-{}'.format(str1, str2, str3)
