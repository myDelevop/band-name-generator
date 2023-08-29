"""
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
Be careful, the functions move and turn_left need to be deleted because already implemented  in the game
"""

from functions import jump_once

for i in range(0, 6):
    jump_once()

'''
# The same with while
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump_once()
    number_of_hurdles -= 1
    print(number_of_hurdles)
'''
