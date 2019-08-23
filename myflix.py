#!/usr/bin/env python3
message = 'You have scored an,'       

print()
print('What was your Test score?')
print()

testscore = float(input())

if testscore >= 90:
    message = message + 'A.'
if testscore >= 80:
    message = message + 'B.'
if testscore >= 70:
    message = message + 'C.'
if testscore >= 60:
    message = message + 'D.'
else:
    message = message + 'F.'
print()
print(message)
print()
