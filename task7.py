s:str ="   Python is fun!   "

s = s.strip()
print("Trimmed:", s)

left_s = s.ljust(20, '*')
print("Left Justified:", left_s) 

right_s = s.rjust(20, '*')
print("Right Justified:", right_s)