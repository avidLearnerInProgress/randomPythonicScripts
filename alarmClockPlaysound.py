import os,time
inputTime=float(input("Enter time to set alarm: "))
fn=os.path.dirname(os.path.abspath(__file__))
relativePath=fn+'\\data\\tower-clock.mp3'  #for windows path
print(relativePath)
time.sleep(inputTime)
os.startfile(relativePath)