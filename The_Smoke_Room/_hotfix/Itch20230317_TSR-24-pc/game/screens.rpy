################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language


style input:
    properties gui.text_properties("input", accent=True)

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

# horzontal bar, not used in the UI
style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
# vertical bar, not used in the UI

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
# horizontal scrollbar, not used in the UI

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
# vertical scrollbar, used on the history screen

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
# horizontal slider, used on the preferences screen

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"
# vertical slider, not used in the UI

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

## Transform to tint the speaker img and character name, used as a part of the say function
transform tint(col):
    matrixcolor TintMatrix(col)
################################################################################
## Custom Say Screen
################################################################################

screen sayMore(who,what,col):
    style_prefix "sayMore"

    window:
        id "windowMore"
        if who is not None:
            add "gui/textbox_speaker.png":
                at tint(col)
            window:
                style "nameboxMore"
                text who id "who":
                    at tint("#000")
                at tint(col)
        ##if who is None:
        ##    add "gui/textbox_aside.png"
        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style windowMore is default
style sayMore_label is default
style sayMore_dialogue is default
style sayMore_thought is sayMore_dialogue

style nameboxMore is default
style nameboxMore_label is sayMore_label


style windowMore:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style nameboxMore:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)

    padding gui.namebox_borders.padding

style sayMore_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style sayMore_dialogue:
    properties gui.text_properties("dialogue")
    line_leading gui.dialogue_leading
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

################################################################################
## Basic Say Screen, used as a fallback for non-defined characters and aside lines
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        if who is not None:
            add "gui/textbox_speaker.png":
                at tint("#D9BC8B")
            window:
                style "namebox"
                text who id "who":
                    at tint("#000")
        if who is None:
            add "gui/textbox_aside.png"
        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox_base.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    line_leading gui.dialogue_leading
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos




## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xpos gui.dialogue_xpos
            xanchor gui.dialogue_xalign
            ypos gui.dialogue_ypos
            xsize gui.dialogue_width

            text prompt style "input_prompt"
            input id "input"


style input_prompt is say_dialogue

style input_prompt:
    properties gui.text_properties("input_prompt")
    xmaximum gui.dialogue_width

style input:
    xmaximum gui.dialogue_width

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    hbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        xalign 0.0
        yalign 0.96
        xoffset -25
        if main_menu:
            spacing 0
        else:
            spacing -20

        if main_menu:

            ##textbutton _("Start") action Start()
            imagebutton auto "gui/buttonGraphics/mm_start_%s.png" action Start() insensitive "gui/buttonGraphics/gm_start_selected_idle.png"

        else:

            ##textbutton _("History") action ShowMenu("history")
            imagebutton auto "gui/buttonGraphics/mm_history_%s.png" action ShowMenu("history") insensitive "gui/buttonGraphics/gm_history_selected_idle.png"

            ##textbutton _("Save") action ShowMenu("save")
            imagebutton auto "gui/buttonGraphics/mm_save_%s.png" action ShowMenu("save") insensitive "gui/buttonGraphics/gm_save_selected_idle.png"


        ##textbutton _("Load") action ShowMenu("load")
        imagebutton auto "gui/buttonGraphics/mm_load_%s.png" action ShowMenu("load") insensitive "gui/buttonGraphics/gm_load_selected_idle.png"
        ##textbutton _("Preferences") action ShowMenu("preferences")
        imagebutton auto "gui/buttonGraphics/mm_pref_%s.png" action ShowMenu("preferences") insensitive "gui/buttonGraphics/gm_pref_selected_idle.png"

        imagebutton auto "gui/buttonGraphics/mm_extras_%s.png" action ShowMenu("chapter_select") insensitive "gui/buttonGraphics/gm_extras_selected_idle.png"

        if _in_replay:

            ##textbutton _("End Replay") action EndReplay(confirm=True)
            imagebutton auto "gui/buttonGraphics/mm_replay_%s.png" action EndReplay(confirm=True) insensitive "gui/buttonGraphics/gm_replay_selected_idle.png"


        elif not main_menu:

            ##textbutton _("Main Menu") action MainMenu()
            imagebutton auto "gui/buttonGraphics/mm_mm_%s.png" action MainMenu() insensitive "gui/buttonGraphics/gm_mm_selected_idle.png"


        ##textbutton _("About") action ShowMenu("about")
        imagebutton auto "gui/buttonGraphics/mm_about_%s.png" action ShowMenu("about") insensitive "gui/buttonGraphics/gm_about_selected_idle.png"

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            ## textbutton _("Help") action ShowMenu("help")
            imagebutton auto "gui/buttonGraphics/mm_help_%s.png" action ShowMenu("help") insensitive "gui/buttonGraphics/gm_help_selected_idle.png"

            ## The quit button is banned on iOS and unnecessary on Android.
            ##textbutton _("Quit") action Quit(confirm=not main_menu)
            imagebutton auto "gui/buttonGraphics/mm_quit_%s.png" action Quit(confirm=not main_menu) insensitive "gui/buttonGraphics/gm_quit_selected_idle.png"

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            ## text "[config.name!t]":
            ##     style "main_menu_title"

            text "Build [config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 500
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    font gui.name_text_font
    color gui.idle_small_color
    size 30

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")



## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True
                        side_xfill True
                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial 1.0

                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        side_yfill True
                        side_xfill True

                        transclude

                else:

                    transclude

    use navigation

    ##textbutton _("Return"):
    ##    style "return_button"
    ##    action Return()

    imagebutton auto "gui/buttonGraphics/return_%s.png":
        style "return_button"
        action Return()


    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 200
    top_padding 100

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 0
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 415
    top_margin 15

style game_menu_viewport:
    xsize 1500

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    font gui.name_text_font
    color gui.text_color_black
    yalign 0.5
    yoffset -52
    xoffset -14

style return_button:
    xpos gui.navigation_xpos
    yalign 0.85
    yoffset -45
    xoffset -65


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size
    font gui.name_text_font


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 11):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color
    font gui.name_text_font

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                if renpy.variant("small"):

                    vbox:
                        style_prefix "radio"
                        label _("Language")
                        textbutton "English" action Language(None)
                        textbutton "{font=font/SourceHanSansSC-Normal.otf}简体中文{font}" action Language("Schinese")
                        textbutton "{font=font/SourceHanSansTC-Normal.otf}繁體中文{font}" action Language("Tchinese")

                if renpy.variant("medium"):

                    vbox:
                        style_prefix "radio"
                        label _("Language")
                        textbutton "English" action Language(None)
                        textbutton "{font=font/SourceHanSansSC-Normal.otf}简体中文{font}" action Language("Schinese")
                        textbutton "{font=font/SourceHanSansTC-Normal.otf}繁體中文{font}" action Language("Tchinese")

                if renpy.variant("pc"):
                    vbox:
                        style_prefix "radio"
                        label _("Language")
                        textbutton "English" action Language(None)
                        textbutton "{font=font/SourceHanSansSC-Normal.otf}简体中文{font}" action Language("Schinese")
                        textbutton "{font=font/SourceHanSansTC-Normal.otf}繁體中文{font}" action Language("Tchinese")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

                # vbox:
                #     style_prefix "check"
                #     label _("Font")
                #     textbutton _("Default") action [gui.SetPreference("font_a", "font/LibreBaskervilleRegular.ttf"), gui.SetPreference("font_b", "font/PlayfairDisplaySCBold.ttf"), gui.SetPreference("font_c", "font/LibreBaskervilleBold.ttf"), gui.SetPreference("font_leading", 1)]
                #     textbutton _("OpenDyslexic") action [ gui.SetPreference("font_a", "font/OpenDyslexic3-Regular.ttf"), gui.SetPreference("font_b", "font/OpenDyslexic3-Bold.ttf"), gui.SetPreference("font_c", "font/OpenDyslexic3-Regular.ttf"), gui.SetPreference("font_leading", -10)]

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

init python:
    def call_chapter_select(character, chapter):
        global chapter_value
        chapter_value = chapter

        print(chapter_value)

        if (character == "Nikolai"):
            renpy.jump_out_of_context("nik_chapter_select")
        elif (character == "William"):
            renpy.jump_out_of_context("will_chapter_select")
        elif (character == "Clifford"):
            renpy.jump_out_of_context("cliff_chapter_select")
        elif (character == "Murdoch"):
            renpy.jump_out_of_context("murdoch_chapter_select")

screen chapter_select():
    tag menu

    default active_selection = "Nikolai"

    use game_menu(_("Chapter Select"), scroll="viewpport"):
        style_prefix "chapter_select" #the fuck

        # Container for menu.
        hbox:
            # Container for each character option in character select.
            spacing 20
            vbox:
                if renpy.variant("small"):
                    spacing 20
                textbutton "Nikolai" action SetScreenVariable("active_selection", "Nikolai")
                textbutton "William" action SetScreenVariable("active_selection", "William")
                textbutton "Murdoch" action SetScreenVariable("active_selection", "Murdoch")
                textbutton "Clifford" action SetScreenVariable("active_selection", "Clifford")

            vbox:
                spacing 10
                # add vertical bar?

            # Container for character selection grids.
            vbox:
                if (active_selection == "Nikolai"):
                    use nik_select
                elif (active_selection == "William"):
                    use will_select
                elif (active_selection == "Murdoch"):
                    use murdoch_select
                elif (active_selection == "Clifford"):
                    use cliff_select

screen nik_select():
    vbox:
        grid 3 2:
            style_prefix "gslot"
            spacing gui.slot_spacing
            imagebutton idle "images/thumbnails/samthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Nikolai", 1), Hide("confirm"))
            imagebutton idle "images/thumbnails/nikthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Nikolai", 2), Hide("confirm"))
            imagebutton idle "images/thumbnails/nikthumb2.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Nikolai", 3), Hide("confirm"))
            imagebutton idle "images/thumbnails/nikthumb3.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Nikolai", 4), Hide("confirm"))
            null
            null
        add "sprites/nik/nik.webp" xpos 820 xysize(800, 800) ypos -400 alpha 0.75

screen will_select():
    vbox:
        grid 3 2:
            style_prefix "gslot"
            spacing gui.slot_spacing
            ## scene 1
            imagebutton idle "images/thumbnails/samthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 1), Hide("confirm"))
            imagebutton idle "images/thumbnails/wilthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 2), Hide("confirm"))
            imagebutton idle "images/thumbnails/wilthumb2.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 3), Hide("confirm"))
            imagebutton idle "images/thumbnails/luthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 4), Hide("confirm"))
            null
            null
        add "sprites/william/wil.webp" xpos 800 xysize(800, 800) ypos -400 alpha 0.75

screen murdoch_select():
    vbox:
        grid 3 2:
            style_prefix "gslot"
            spacing gui.slot_spacing
            imagebutton idle "images/thumbnails/samthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 1), Hide("confirm"))
            imagebutton idle "images/thumbnails/murthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 2), Hide("confirm"))
            imagebutton idle "images/thumbnails/murthumb2.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 3), Hide("confirm"))
            imagebutton idle "images/thumbnails/luthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 4), Hide("confirm"))
            null
            null
        add "sprites/murdoch/mur.webp" xpos 800 xysize(800, 800) ypos -400 alpha 0.75

screen cliff_select():
    vbox:
        grid 3 2:
            style_prefix "gslot"
            spacing gui.slot_spacing
            imagebutton idle "images/thumbnails/samthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 1), Hide("confirm"))
            imagebutton idle "images/thumbnails/cliffthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 2), Hide("confirm"))
            imagebutton idle "images/thumbnails/cliffthumb2.jpg" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 3), Hide("confirm"))
            imagebutton idle "images/thumbnails/luthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 4), Hide("confirm"))
            null
            null
        add "sprites/cliff/cli.webp" xpos 900 xysize(600, 700) ypos -300 alpha 0.75



style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    font gui.name_text_font
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport")):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what

        if not _history_list:
            label _("The dialogue history is empty.")


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    font gui.name_text_font

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5
    font gui.name_text_font


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")
    font gui.name_text_font
    size 40

style help_label:
    xsize 435
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5
    xfill True

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

style gui_medium_button_text:
    hover_color gui.text_color_gold


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size
    color gui.text_color_black

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
    color gui.text_color_black


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0
            spacing 75
            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

##style game_menu_navigation_frame:
##    variant "small"
##    xsize 510

## style game_menu_content_frame:
##    variant "small"
##    top_margin 0

## style pref_vbox:
##    variant "small"
##    xsize 600

## style slider_pref_vbox:
##    variant "small"
##    xsize None

## style slider_pref_slider:
##    variant "small"
##    xsize 900


###########
## Will Notebook
###########

screen quick_menu_will():

    zorder 100

    if quick_menu_will:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("Notebook") action (renpy.restart_interaction, ShowMenu('willnotes_screen'))

init python:
    config.overlay_screens.append("quick_menu_will")
    journal_entries = [
        {
            "text": _("{color=#000000}{font=willfont.ttf}Huxley Greene is dead. His body was found frozen. Decapitated with ripping force.{/font}{/color}"),
            "image": "wn1",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}Where was the body found? ASK TODD LATER. {/font}{/color}"),
            "image": "wn2",
        },
        {
            "text": _("{color=#000000} {font=willfont.ttf}Cliff claims Reed tries to break into his apartment.{/font} {/color}"),
            "image": "wn3",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}Cliff works with James for CGCS.{/font}{/color}"),
            "image": "wn4",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}Cliff's real name is Cornelis. He claims he does not have his worker's permit.{/font} {/color}"),
            "image": "wn5",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[stagnighttext!ti]{/font}{/color}"),
            "image": "wn6",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[chnighttext!ti]{/font}{/color}"),
            "image": "wn6",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley1!ti]{/font}{/color}"),
            "image": "wn7",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley2!ti]{/font}{/color}"),
            "image": "wn14",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley3!ti]{/font}{/color}"),
            "image": "todddumb",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[jamestext!ti]{/font}{/color}"),
            "image": "[jamesimage]",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[changtext!ti]{/font}{/color}"),
            "image": "wn11",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf} Sam needs to sleep more. [cynthiatext!ti]{/font}{/color}"),
            "image": "wn12",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[harlantext!ti]{/font}{/color}"),
            "image": "wn13",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[etheltext!ti]{/font}{/color}"),
            "image": "todddumb",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley4!ti]{/font}{/color}"),
            "image": "wn2",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[gumtext!ti]{/font}{/color}"),
            "image": "wn16",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[kanetext!ti]{/font}{/color}"),
            "image": "wn17",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[filmtext!ti]{/font}{/color}"),
            "image": "wn18",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[jartext!ti]{/font}{/color}"),
            "image": "wn19",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[shroudtext!ti]{/font}{/color}"),
            "image": "wn15",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[dolltext!ti] [marcydolltext!ti]{/font}{/color}"),
            "image": "wn20",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[samtoddtext!ti]{/font}{/color}"),
            "image": "musky",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[murdochtext!ti]{/font}{/color}"),
            "image": "bettercallmurdoch",
        }
    ]
default unlocked_journal_pages = 0
default current_journal_page = 0


init python:


    renpy.music.register_channel('music_menu', mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

    def musicJournalPlay():
        renpy.music.set_volume(0.0, delay=2.5, channel='music')

    def musicJournalStop():
        renpy.music.set_volume(1.0, delay=2.5, channel='music')

    def incrementJournal():
        global current_journal_page
        current_journal_page += 1

    def decrementJournal():
        global current_journal_page
        current_journal_page -= 1


screen willnotes_screen():

    tag menu

    on 'show' action Play("music_menu", "music/nonsense.mp3", fadein=5.0), Function(musicJournalPlay)
    on 'hide' action Stop("music_menu", fadeout=2.5), Function(musicJournalStop, *args, **kwargs)

    vbox:
        xminimum 0.33
        xmaximum 0.33
        frame:
            background "gui/customscreens/willnotebookbg.png"
            foreground [journal_entries[current_journal_page]["image"]]
            yminimum 0.75
            ymaximum 0.75
            has vbox
            ## This is where we display the currently-selected page of
            ## the journal, prefaced by the label "Notes:".
            label _("Notes:")
            $ journal_entry = journal_entries[current_journal_page]
            text journal_entry["text"]

    vbox:
        xpos 620
        xmaximum 200
        frame:
            style_group "pref"
            has vbox
            label _("Page:")

            if current_journal_page < (unlocked_journal_pages - 1):
                textbutton _("Next") action Function(incrementJournal, *args, **kwargs)
            else:
                textbutton _("{color=#2c2c2c}Next{/color}") action NullAction()

            if current_journal_page >= 1:
                textbutton _("Previous") action Function(decrementJournal, *args, **kwargs)
            else:
                textbutton _("{color=#2c2c2c}Previous{/color}") action NullAction()
            textbutton _("Close") action Return()

init -2 python:
    style.pref_frame.xfill = True
    style.pref_frame.xmargin = 5
    style.pref_frame.top_margin = 5

    style.pref_vbox.xfill = True

    style.pref_button.size_group = "pref"
    style.pref_button.xalign = 0.1

    style.pref_slider.xmaximum = 192
    style.pref_slider.xalign = 1.0

    style.soundtest_button.xalign = 1.0


# utils
init python:
    def redefine_journal_entries():
        # ! This will need to update if there are more journal entires added!
        new_journals = journal_entries = [
        {
            "text": _("{color=#000000}{font=willfont.ttf}Huxley Greene is dead. His body was found frozen. Decapitated with ripping force.{/font}{/color}"),
            "image": "wn1",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}Where was the body found? ASK TODD LATER. {/font}{/color}"),
            "image": "wn2",
        },
        {
            "text": _("{color=#000000} {font=willfont.ttf}Cliff claims Reed tries to break into his apartment.{/font} {/color}"),
            "image": "wn3",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}Cliff works with James for CGCS.{/font}{/color}"),
            "image": "wn4",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}Cliff's real name is Cornelis. He claims he does not have his worker's permit.{/font} {/color}"),
            "image": "wn5",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[stagnighttext!ti]{/font}{/color}"),
            "image": "wn6",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[chnighttext!ti]{/font}{/color}"),
            "image": "wn6",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley1!ti]{/font}{/color}"),
            "image": "wn7",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley2!ti]{/font}{/color}"),
            "image": "wn14",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley3!ti]{/font}{/color}"),
            "image": "todddumb",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[jamestext!ti]{/font}{/color}"),
            "image": "[jamesimage]",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[changtext!ti]{/font}{/color}"),
            "image": "wn11",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf} Sam needs to sleep more. [cynthiatext!ti]{/font}{/color}"),
            "image": "wn12",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[harlantext!ti]{/font}{/color}"),
            "image": "wn13",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[etheltext!ti]{/font}{/color}"),
            "image": "todddumb",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[huxley4!ti]{/font}{/color}"),
            "image": "wn2",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[gumtext!ti]{/font}{/color}"),
            "image": "wn16",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[kanetext!ti]{/font}{/color}"),
            "image": "wn17",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[filmtext!ti]{/font}{/color}"),
            "image": "wn18",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[jartext!ti]{/font}{/color}"),
            "image": "wn19",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[shroudtext!ti]{/font}{/color}"),
            "image": "wn15",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[dolltext!ti] [marcydolltext!ti]{/font}{/color}"),
            "image": "wn20",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[samtoddtext!ti]{/font}{/color}"),
            "image": "musky",
        },
        {
            "text": _("{color=#000000}{font=willfont.ttf}[murdochtext!ti]{/font}{/color}"),
            "image": "bettercallmurdoch",
        }
        ]

        return new_journals

    def update_unlocked_pages(new_unlocked_pages, new_current_page):
        global unlocked_journal_pages
        global current_journal_page
        global journal_entries
        global willnote
        willnote = True
        journal_entries = redefine_journal_entries()
        unlocked_journal_pages += new_unlocked_pages
        current_journal_page = new_current_page
