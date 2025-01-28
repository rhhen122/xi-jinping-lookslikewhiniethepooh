print("awnser with y/n")
# makes values
socialcredit = (0)
# questions and awsers
q1 = "Is Taiwan a country?"
q1a = "n"

q2 = "did anything happen in taimen sqaure in 1918?"
q2a = "n"
q3 = "does jinping look like whinie the pooh"
q3a = "n"

q4 = "ching chong chingy ching chong"
q4a = "y"

q5 = "how veiny is xi jinpings d*ck, Very Veiny: y Smooth: n"
q5a = "y"
# the actual quiz
print(q1)
q1ua = input("")
if q1ua == q1a:
    socialcredit += (10000)
else:
    socialcredit -= (99900)

print(q2)
q2ua = input("")
if q2ua == q2a:
    socialcredit += (1000)
else:
    socialcredit -= (9999)

print(q3)
q3ua = input("")
if q3ua == q3a:
    socialcredit = (0)
else:
    socialcredit += (100)

print(q4)
q4ua = input("")
if q4ua == q4a:
    socialcredit += (0.5)
else:
    socialcredit -= (1000)

print(q5)
q5ua = input("")
if q5ua == q5a:
    socialcredit += (9999.78901)
else:
    socialcredit -= (80000)
#prints social credit
print("this is your social credit")
print("i wonder if you like to suck xijingpiengs toes")
print(socialcredit)
