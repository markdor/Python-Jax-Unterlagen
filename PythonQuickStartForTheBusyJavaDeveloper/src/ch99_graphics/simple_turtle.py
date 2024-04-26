# ImportError: No module named _tkinter
# brew install python-tk
# pip3 install tk

from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

