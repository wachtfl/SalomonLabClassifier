import matlab.engine
eng = matlab.engine.start_matlab()
eng.configuration_script(5, 'spatial', [2, 4, 6])
#configurateAndDecode(sbjNumber, space_time_mode, electrodesToRemove)
person = input('Enter your name: ')
tf = eng.isprime(37)
print(tf)