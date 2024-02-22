label label_library:
    scene bg library
    show fg library-table # onlayer master zorder 2
    show joyce holdbook smile outfit3 at trs_sitting
    show fg2 library-table-shadow1 onlayer master zorder 2
    show screen screen_glass("library") onlayer master zorder 2
    "this is a planned date: at the library, right now it's still in development"
    j "What book do you wanna read?"
    j -smile eyesdown "Do you want to read a mythology book?"
    menu:
        "Read a Mythology book.":
            "awesome"
        "Read a Physics book.":
            "awesome"
    call label_after_successful_Date_common
    $ g.phoneProgress[0] -= 2
    $ g.phoneProgress[1] = 10
    call label_newDay("label_home")

label label_library_endTurn:
    call label_date_isLost_common