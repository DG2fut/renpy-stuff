define s = Character("Sayori",color="#FA8072")
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
label start:

    $ y = renpy.input("Reveal yourself")
    if y == "":
        "I was asking for your name dumbass"

    scene bedtime with flash

    show say1 at truecenter:
        zoom 0.8
    with dissolve

    play music "audio/ohayou.mp3.mp3"

    s "Hey..." with wiperight
    s "So [y]... \nAbout that thing you said..." with wiperight
    pause(1.0)
    s "So you want to do it right now?" with wiperight
    s "The atmosphere is perfect and everything..." with wiperight
    show say2 at truecenter:
        zoom 0.8
    with dissolve
    s "Heyyyyy!! Are u listening to me?!?!" with wiperight
    s "Did you hit your head or something?" with wiperight
    s "Anyway..." with wiperight
    hide say2
    show say1 at truecenter:
        zoom 0.8
    with dissolve
    s "It's time." with wiperight
    s "I'm ready." with wiperight

    "Its time to choose." with wiperight

    menu:
        "Huh?":
            jump op1
        "Let's do it.":
            jump op2
        "I hate you":
            jump op3

label op1:
    hide say1
    show say3 at truecenter:
        zoom 0.8
    with flash
    s "What do you mean 'Huh?'"
    s "Why are you acting like you don't know what's going on?" with wiperight
    s "You're the one that brought me here, [y]." with wiperight
    hide say3
    show say2 at truecenter:
        zoom 0.8
    with dissolve
    s "And now you're pussying out at the last second..." with wiperight
    s "After all those sweet things you said to me..." with wiperight
    s "Was it all just a lie?" with wiperight
    hide say2
    show say4 at truecenter:
        zoom 0.8
    with dissolve
    s "How could you..." with wiperight
    s "After all that's happened..." with wiperight
    hide say4
    show say6 at truecenter:
        zoom 0.8
    with dissolve
    s "Fuck you, [y]." with wiperight
    s "Just get out already." with wiperight
    hide say4
    scene street with dissolve
    "OHHHHHHHHHHH..." with wiperight
    "She wanted to DO IT." with wiperight
    "Great job dumbass." with wiperight
    "That was your only chance." with wiperight
    "And you ruined it." with wiperight
    jump end

label op2:
    show say5 at truecenter:
        zoom 0.8
    with dissolve
    s "Yep! Let's do it!" with wiperight
    s "I LOVE YOU!!!" with wiperight
    show say7 at truecenter:
        zoom 1.6
    with dissolve
    hide say5
    "Sayori pushes you on to the bed and gently gets on top of you" with wiperight
    s "Get your pika out and chu me already ;)" with wiperight
    "You take your pokeballs out." with wiperight
    hide say7
    show say8 at truecenter:
        zoom 1.6
    with dissolve
    s "OMG!!!"
    hide say8
    show say5 at truecenter:
        zoom 0.8
    with dissolve
    s "Lmao it's so fucking tiny." with wiperight
    s "Fuck off, you horny bastard." with wiperight
    s "Go get some real bitches instead." with wiperight
    show white at truecenter:
        zoom 7.0
    with flash
    "Haha you thought XD" with wiperight
    "Go touch some grass fr" with wiperight
    jump end

label op3:
    show say1 at truecenter:
        zoom 0.8
    with dissolve
    s "Of course i know that you dumb baka" with wiperight
    s "You know what happens after this right" with wiperight
    "[s] takes out a knife" with wiperight
    "RIP you're screwed"
    hide say1
    show say5 at truecenter:
        zoom 0.8
    with dissolve
    s "Die lmao" with wiperight
    show white at truecenter:
        zoom 8.0
    with flash
    "You died XOXO"
    jump end
    


label end:
    show black
    "Thanks for playing UwU"
    return
