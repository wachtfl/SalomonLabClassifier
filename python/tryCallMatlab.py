import matlab.engine
eng = matlab.engine.start_matlab()
eng.ddtbox_script(nargout=0)
eng.quit()