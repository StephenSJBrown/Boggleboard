import string
import random
import re
import math

letters = ""

dice = 'AAEEGNELRTTYAOOTTWABBJOOEHRTVWCIMOTUDISTTYEIOSSTDELRVYACHOPSHIMNQUEEINSUEEGHNWAFFKPSHLNNRZDEILRX'

dice = re.findall("\D{6}", dice)

def roll_dice():
    count = 16
    roll_result = ''
    while count > 0:
        roll_result+=random.choice(dice)[random.randint(0,5)]
        count-= 1
    return roll_result

def generate_letters():
    count = 16
    letters = ''
    while count > 0:
        letters+=random.choice(string.ascii_uppercase)
        count-= 1
    return letters

def show_board(letters):
    if letters == '':
        letters = "----------------"
    lines = re.findall("\D{4}", letters)
    for line in lines:
        line = re.sub('Q', ' Qu', line)
        line = re.sub('([^Qu|^\s])', r' \1 ', line)
        print('#', line)

def check(letters, word):
    lines = re.findall("\D{4}", letters)
    found = False
    for line in lines:
        if re.search(word, line):
            found = True
            break
    if found == True:
        print('Yeah good find!')
        show_board(letters)
    else:
        print('Not in there')

# i = new x
# j = new y

def adv_search(word, index, position="None"):
    # if we find the last letter next to the penultimate letter
    if index == 1:
        print('We got one!!!')
    # If we still have more letters to search through...
    else:
        # print('going deeper underground...')
        # if we find the letter has the next letter next to it (first the last
        # letter, then moving backwards)
        # print('checking if ', word[index-1],' has',word[index-2],' next to it')
        # capture new indicies if true or False if no indicies found
        new_indicies = adj_check(word, index-1, position)
        if new_indicies:
            # print('it does!')
            # print('Okay so the result of adj_check is: ', new_indicies)
            position = new_indicies
            # print('starting position(s): ', position)
            # then start again with the next letter
            # adv search now needs to take the new indicies
            adv_search(word, index-1, position)
        # if we don't find it
        else:
            print('The word was not found')

# CHECKS IF NEXT LETTER IS ADJACENT TO STARTING LETTER
def adj_check(word, index, position):
    # if we haven't tried any tried any letters before, then find where they are now
    # set the indicies to search through
    if position == "None":
        indices = [t for t, x in enumerate(letters) if x == word[index] ]
        print('indicies ',indices)
        # search board for letter[index]
        # return index_location of letter[index]
        # run the code the number of letters there are
    # otherwise, pass in the indicies that we captured from checking the letters before
    else:
        indices = position
    found = False
    next_position = []
    try:
        for target_index in indices:
            print('checking against the ', letters[target_index], 'at ', target_index)
            index_location = target_index
            x = index_location%4
            y = int(math.floor(index_location/4))
            # find adjacent
            #check row above (y-1)
            if y - 1 >= 0:
                for i in range(-1, 2):
                    #as long as still on grid horizontally
                    if i+x >= 0 and i+x < 4:
                        # check that cell
                        # convert coordinates to index location
                        target_index_location = ((y-1) * 4) + (x+i)
                        # print('target index location',target_index_location)
                        # check if next letter exists in there
                        if word[index-1] ==  letters[target_index_location]:
                            print('Found it!', word[index-1], 'at ', target_index_location)
                            next_position.append(target_index_location)
                            found = True
                    else:
                        continue

            # check same row
            for i in range(-1, 2, 2):
                #as long as still on grid horizontally
                # print((i+x))
                if i+x >= 0 and i+x < 4:
                    # check that cell
                    # convert coordinates to index location
                    target_index_location = (y * 4) + (x+i)
                    # print('target index location',target_index_location)
                    # check if next letter exists in there
                    if word[index-1] ==  letters[target_index_location]:
                        print('Found it!', word[index-1], 'at ', target_index_location)
                        next_position.append(target_index_location)
                        found = True
                else:
                    continue
            # check row below
            if y + 1 < 4:
                for i in range(-1, 2):
                    #as long as still on grid horizontally
                    # print((i+x))
                    if i+x >= 0 and i+x < 4:
                        # check that cell
                        # convert coordinates to index location
                        target_index_location = ((y+1) * 4) + (x+i)
                        # print('target index location',target_index_location)
                        # check if next letter exists in there
                        if word[index-1] ==  letters[target_index_location]:
                            print('Found it!', word[index-1], 'at ', target_index_location)
                            next_position.append(target_index_location)
                            found = True
                    else:
                        continue
        if found == False:
            return found
        else:
            return next_position
    # if the letter can't be found
    except:
        return found
    # return coordinates

print('Welcome to boggle board!')
print()
show_board(letters)

answer = ' '

while answer != 'end':
    print()
    print('Take an action. R = Roll. C = Clear Board. K = Check. E = End Game')
    answer = input()
    answer = re.sub('Qu', ' Q', answer)
    answer = answer.upper()
    if answer == 'R':
        letters = roll_dice() 
        show_board(letters)
    elif answer == 'C':
        letters = ''
        show_board(letters)
    elif answer == 'G':
        letters = generate_letters()
        show_board(letters)
    elif answer == 'K':
        if letters == "":
            print('You need a populated board before you can check')
        else:    
            word = input('What word will you check for? ').upper()
            index = len(word)
            # check(letters, word)
            adv_search(word,index)
    elif answer == 'E':
        print('End of game you schmuck')



