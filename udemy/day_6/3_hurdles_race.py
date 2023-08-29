"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
Similar to the previous one but in this case we don't know how many steps to win. We check with at_goal()
"""
from functions import jump_once
from functions import at_goal

win = False
while not win:
    jump_once()
    if at_goal():  # if at_goal() true we win the Race
        win = True

