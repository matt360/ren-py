﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
image school = "bg girl school.jpg"
define e = Character("Eileen")
define l = Character("Lucy")

# The game starts here.
label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg school
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show eileen happy

    # These display lines of dialogue.
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    menu:
        "Hey you look nice!":
                jump nice
        "Hey you look bad!":
                jump bad
    label nice:
        show eileen vhappy at right
        e "I'm very happy right now!"
        jump scene_two
    label bad:
        show eileen concerned
        e "Noooo"
        "NICE"
        jump scene_two
        
    label scene_two:    
    e "Are we going to be okay?"
    
    show eileen happy
    
    e "Looking forward to it!"
    
    hide eileen
    show lucy mad
    
    l "Yeah, right..."

    hide lucy 
    show eileen vhappy
    
    e "Don't be a hater"
    
    show school
    
    # This ends the game.

    return