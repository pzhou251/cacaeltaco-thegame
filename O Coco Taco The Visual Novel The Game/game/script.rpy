﻿# The script of the game goes in this file.

#flags
default persistent.pizza_flag = 0
define menuFlag = 0
default persistent.game_started = 0

#character positions
transform quarter_left:
    xalign .25 yalign 1.0
transform quarter_right:
    xalign .75 yalign 1.0

# The game starts here.


label start:
    #if persistent.pizza_flag > 0 and game_started > 0:
    if (persistent.pizza_flag > 0) and (persistent.game_started > 0):
        wist "should jump now"
        jump pizza_start

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg classroom with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ persistent.game_started = 1

    scene bg obby with pixellate

    play sound boing
    play sound oof

    wist "Dang it, I quit >:c"

    wist "{i}Failed this obby again.{/i}"

    wist "{i}Maybe I should play a new game.{/i}"

    wist "hmm?"
    play sound click

    scene bg games with pixellate

    play sound click
    wist "huh? caca o taco"
    
    play sound click

    scene bg outside with pixellate
    show turan neutral with dissolve

    wist "What da heck I just wanted to buy a crunchwrap supreme , I didn't want to play a dating sim :c"


    play sound shake
    show turan shocked with hpunch
    turandot "WAITTT KITTY !!"
    show turan sad
    turandot "Don't go, lets eat tacos together 😭"

    wist "???"
    wist "how did you know I was a cat? :c hmm..."
    wist "Are you a player or an npc"

    show turan neutral
    turandot "Yeah."

    wist "???"
    wist "That doesnt answer my question"

    show turan neutral
    turandot "Oh, I'm just stuck here. My name's Turandot."

    wist "oh nice to meet you im wist : 3"
    wist "..."
    
    show turan happy
    turandot "..."

    wist "Wait :/ what do u mean ur stuck here"

    show turan thinking
    turandot "Hmm have u ever watched Saber Art Online."
    play sound bruh

    wist ">:/ i want to log out…."

    show turan shocked
    turandot "Nooooo wait lets get some food , Wist ! We can get a crunchy wrapy supremi™."
    
    wist "(╯✧ ∇ ✧)╯ crunchywrapy supremy…"

    scene bg outsidecoco with pixellate
    play sound tacochime
    
    narrator "Yeah we know fast food chains dont usually have door chimes when you enter its just to establish the setting ,,, gosh"
    
    show turan confused
    turandot "Why so sassy they probably weren't even thinking about that."

    wist "who are you talking to?? Whos they??0 ___0' "

    show turan neutral
    turandot "Don’t worry this game is , like , 5 min long so we dont have time delve into that."
    show turan happy
    turandot  "Let's go order."

    scene bg insidecoco with pixellate
    play sound tacobeep

    show turan happy at center with dissolve
    turandot "hiiiii :3"
    show turan sad at quarter_left with move

    show dj neutral at quarter_right

    dj " *sigh* "

    wist "hello!"

    dj "No animals allowed."

    wist "?????? >:O"

    show turan mad at quarter_left
    turandot "They're not an animal they're a player !"

    wist "*sweating* yeah…"

    hide turan mad with moveoutleft
    show dj mad at center with move

label food_menu:
menu:
    dj "Whatever, what do u want"

    "Crunchywrapy supremy":
        $ menuFlag = 0
        turandot "yum i love crunchwrapy supremy (placeholder text)"
        jump after_menu

    "Cheesy beans taquito":
        $ menuFlag = 1
        turandot "can you not spit on it this time"
        dj "hmmm ill think about it"
        wist "wait you spit on it??"
        wist "i wanna speak to your manager *karen hair sprite*"
        jump after_menu

    "Brazilian pizza":
        $ menuFlag = 2
        jump pizza_choice

label pizza_choice:
menu:
    dj "are you sure about this? ( this action will have consequences) "
    "Yes":
        #background and Turandot get darker / looks like night
        dj "you have chosen pizza [persistent.pizza_flag] time(s)"
        $ persistent.pizza_flag += 1
        #split second turandot sprite change
        #Game closes 
        $ renpy.quit()

    "No":
        jump food_menu
        #Goes back to menu
        #music restarts

label pizza_start:
    # The game reload , bgm play
    show turan thinking at center with dissolve
    turandot "phewww thank goshness you dindt have to see that" 
    wist "??? why did my screen just black out just now?" 
    turandot "ooo yeah i didnt want you to see what that Brazilian pizza would do to me" 
    # background changes to eaten pizza with police tape spongebob style
    wist "wait you did this? you logged me out of the game???"  
    turandot "oh it wasn't me it was my code writers"
    wist "excuse me o_O what kind of vn is this" 
    #Dissolve restroom door
    turandot "yeah they probably wanted to protect you from what that pizza was going to do to me"
    wist "… o_e"
    #Background dissolve back


label after_menu:



     


    # This ends the game.
    $ persistent.game_started = 0 # game ended
    return
