import matlab.engine
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
eng = matlab.engine.start_matlab()


#com.mathworks.mde.desk.MLDesktop.getInstance.getMainFrame.setVisible(0)

eng.configuration_script(5, 'spatial', [2, 4, 6])
#configurateAndDecode(sbjNumber, space_time_mode, electrodesToRemove)
person = input('Enter your name: ')
tf = eng.isprime(37)
print(tf)