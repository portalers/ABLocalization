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
    adjust_spacing False

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


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize 30
    base_bar Frame("gui/game_menu_buttons/gm_main_bar.png", Borders(13, 15, 14, 15), tile=gui.scrollbar_tile)
    thumb Frame("gui/game_menu_buttons/gm_thumb_bar.png", Borders(16, 31, 15, 31), tile=gui.scrollbar_tile)
    thumb_offset 5

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

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
transform textbox_anim:
    yoffset 0 alpha 1
    on say_hide:
        yoffset 0 alpha 1
        ease .5 yoffset 300 alpha 0
    on say_show:
        yoffset 300 alpha 0
        ease .5 yoffset 0 alpha 1
screen say(who, what):
    style_prefix "say"

    window at textbox_anim:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"


    use quick_menu()

    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

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

    background Image("gui/dialogue_box.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/dialogue box_name box.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
transform ctc_bob:
    yoffset 0
    xoffset -60
    xanchor 0.5
    ease 1.6 yoffset -10
    ease 1.6 yoffset 0
    ease 1.6 yoffset -10
    ease 1.6 yoffset 0
    ease 1.6 yoffset -10
    ease 1.6 yoffset 0
    ease 0.8 xzoom -1
    ease 0.8 xzoom 1
    repeat
screen ctc(arg=None):

    zorder 100
    add "gui/ctc_button.png" xalign 0.93 yalign 0.96 at ctc_bob
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"
    use quick_menu()

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

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
        hbox at textbox_anim:
            pos (1290, 720)
            spacing 10
            imagebutton auto "gui/quick_buttons/back_%s.png" action Rollback()
            imagebutton auto "gui/quick_buttons/history_%s.png" action ShowMenu('history')
            imagebutton auto "gui/quick_buttons/skip_%s.png" selected_hover "gui/quick_buttons/skip_selected_idle.png" action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton auto "gui/quick_buttons/auto_%s.png" selected_hover "gui/quick_buttons/auto_selected_idle.png" action Preference("auto-forward", "toggle")
            if not has_new_entries():
                imagebutton auto "gui/quick_buttons/journal_%s.png" action ShowMenu('journal')
            else:
                imagebutton auto "gui/quick_buttons/journal_notif_%s.png" action ShowMenu('journal')
        imagebutton auto "gui/quick_buttons/gear_%s.png" action ShowMenu('enter_game_menu') pos (30, 30)


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
# init python:
#     config.overlay_screens.append("quick_menu")

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
init python:
    def gm_button_focus(x,y):
        return x >= 40 and x <= 316 and y >= 69 and y <= 123
screen navigation():
    vbox:
        style_prefix "navigation"
        xpos 150
        if main_menu:
            yalign 0.65
        else:
            yalign 0.9

        spacing gui.navigation_spacing
        if main_menu:
            imagebutton auto "gui/main_menu_buttons/mm_start_%s.png" action Start() focus_mask gm_button_focus
        else:
            imagebutton auto "gui/game_menu_buttons/gm_history_%s.png" action ShowMenu("history") focus_mask gm_button_focus sensitive renpy.get_screen('history') == None insensitive "gui/game_menu_buttons/gm_history_selected_idle.png"
            imagebutton auto "gui/game_menu_buttons/gm_save_%s.png" action ShowMenu("save") focus_mask gm_button_focus sensitive renpy.get_screen('save') == None insensitive "gui/game_menu_buttons/gm_save_selected_idle.png"

        imagebutton auto "gui/game_menu_buttons/gm_load_%s.png" action ShowMenu("load") focus_mask gm_button_focus sensitive renpy.get_screen('load') == None insensitive "gui/game_menu_buttons/gm_load_selected_idle.png"

        imagebutton auto "gui/game_menu_buttons/gm_pref_%s.png" action ShowMenu("preferences") focus_mask gm_button_focus sensitive renpy.get_screen('preferences') == None insensitive "gui/game_menu_buttons/gm_pref_selected_idle.png"

        imagebutton auto "gui/game_menu_buttons/gm_about_%s.png" action ShowMenu("about") focus_mask gm_button_focus sensitive renpy.get_screen('about') == None insensitive "gui/game_menu_buttons/gm_about_selected_idle.png"
        if not main_menu:
            imagebutton auto "gui/game_menu_buttons/gm_mm_%s.png" action MainMenu() focus_mask gm_button_focus

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            imagebutton auto "gui/game_menu_buttons/gm_quit_%s.png" action Quit(confirm=not main_menu) focus_mask gm_button_focus


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

#####################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu
default persistent.prologue_cleared = False
init python:
    def mm_button_focus(x,y):
        return x >= 40 and x <= 316 and y >= 69 and y <= 123
screen main_menu():
    style_prefix "main_menu"
    default title = "mm"

    tag menu
    if not persistent.prologue_cleared:
        add "gui/kobulightfinal.png"
    else:
        add "gui/kobulightfinal_nokobu2.png"
    python:
        import time
        year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
        if hour >=6  and hour <=12:
            if renpy.music.get_playing("music") != "audio/music/menu.ogg":
                renpy.music.play("audio/music/menu.ogg","music", loop=True)
        elif hour > 12 and hour <=18:
            if renpy.music.get_playing("music") != "audio/music/WTDL_-_Chillax_in_the_Mortal_Realm_Kubo_4.ogg":
                renpy.music.play("audio/music/WTDL_-_Chillax_in_the_Mortal_Realm_Kubo_4.ogg","music", loop=True)
        else:
            if renpy.music.get_playing("music") != "audio/music/menunight.ogg":
                renpy.music.play("audio/music/menunight.ogg","music", loop=True)
    add "gui/Title.png" pos(60, 55)
    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    vbox:
        spacing -70
        imagebutton auto "gui/main_menu_buttons/mm_start_%s.png" action Start() focus_mask mm_button_focus
        imagebutton auto "gui/main_menu_buttons/mm_load_%s.png" action ShowMenu("load") focus_mask mm_button_focus
        imagebutton auto "gui/main_menu_buttons/mm_pref_%s.png" action ShowMenu("preferences") focus_mask mm_button_focus
        imagebutton auto "gui/main_menu_buttons/mm_about_%s.png" action ShowMenu("about") focus_mask mm_button_focus
        imagebutton auto "gui/main_menu_buttons/mm_quit_%s.png" action Quit() focus_mask mm_button_focus
    hbox:
        yalign 0.95
        xalign 1.0
        xoffset -100
        imagebutton auto "gui/main_menu_buttons/patreon_%s.png" action OpenURL("https://www.patreon.com/TeamBoke")
        imagebutton auto "gui/main_menu_buttons/itch_%s.png" action OpenURL("https://bokedaidu.itch.io/where-the-demon-lurks")
        imagebutton auto "gui/main_menu_buttons/twitter_%s.png" action OpenURL("https://twitter.com/BokeTeam")


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 0.0
    xoffset 200
    xmaximum 1200
    yalign 1.0
    yoffset -100

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

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
screen enter_game_menu():
    tag menu
    on "show" action [Function(renpy.show_layer_at, g_to_m_blur, layer="master", reset=False), Function(renpy.show_layer_at, g_to_m_blur, layer="master_2", reset=False)]
    on "hide" action [Function(renpy.show_layer_at, m_to_g_blur, layer="master"), Function(renpy.show_layer_at, m_to_g_blur, layer="master_2")]
    # add "SM_background transparent overlay.png"
    # add "SM_menu overlay.png"
    use navigation
    imagebutton auto "gui/game_menu_buttons/back_%s.png" action Return() xalign 0.95 yalign 1.0
transform g_to_m_blur:
    blur 20
transform m_to_g_blur:
    linear 0.5 blur 0
screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    if main_menu:
        if not persistent.prologue_cleared:
            add "gui/kobulightfinal.png" at g_to_m_blur
        else:
            add "gui/kobulightfinal_nokobu2.png" at g_to_m_blur
    else:
        on "show" action Function(renpy.show_layer_at, g_to_m_blur, layer="master", reset=False)
        on "hide" action Function(renpy.show_layer_at, m_to_g_blur, layer="master")
    add "gui/SM_background transparent overlay.png"
    add "gui/SM_menu overlay.png"
    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport id "gm_content":
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation
    imagebutton auto "gui/game_menu_buttons/back_%s.png" action Return() xalign 0.97 yalign 0.99
    add "gui/game_menu_buttons/" + title.lower() + "_title.png" pos(90, 100)

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side


style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 110

    #background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 550
    yfill True

style game_menu_content_frame:
    left_margin 90
    right_margin 30
    top_margin 15
    bottom_margin 80

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

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

            label "{font=font/DenseLetters-nRgDO.otf}[config.name!t]"
            text _("{font=font/DenseLetters-nRgDO.otf}Version{/font} [config.version!t]\n")

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
                for page in range(1, 10):
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
    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")
                null width 80
                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                vbox:
                    style_prefix "check"
                    label _("Language")
                    textbutton _("{font=font/DenseLetters-nRgDO.otf}English{/font}"):
                            yalign 0.5
                            action Language(None)
                    textbutton _("{font=font/HYYuanLongHei-90W.ttf}简体中文{/font}"):
                        yalign 0.5
                        action Language("Schinese")
                    textbutton _("{font=font/GenSenRounded-H.ttc}繁體中文{/font}"):
                        yalign 0.5
                        action Language("Tchinese")
                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (2 * gui.pref_spacing)
            hbox:
                # vbox:
                #     style_prefix "check"
                #     label _("Font")
                #     grid 2 1:
                #         textbutton _("{font=font/DenseLetters-nRgDO.otf}English"):
                #             yalign 0.5 xalign 0.5
                #             action Language(None)
                #         textbutton _("{font=font/OpenDyslexicReg.otf}OpenDyslexic"):
                #             text_layout "nobreak" xalign 0.5 yoffset -8
                #             action Language("opendyslexic")

                #         # textbutton _("{font=font/HYYuanLongHei-90W.ttf}简体中文{/font}") action [SelectedIf(Language("Schinese")), gui.SetPreference("journal_title_size", 80), If(main_menu, main_menu_update_discord, update_discord)] xalign 0.5
                #         # textbutton _("{font=font/HYYuanLongHei-90W.ttf}繁體中文{/font}") action [SelectedIf(Language("Tchinese")), gui.SetPreference("journal_title_size", 80), If(main_menu, main_menu_update_discord, update_discord)] xalign 0.5
                # null width 80
                vbox:
                    style_prefix "radio"
                    xsize 500
                    label _("Discord Integration")
                    grid 2 1:
                        textbutton _("Off") action [SetField(persistent, "discord_active", False), Function(disconnect_discord)]
                        textbutton _("On") action [SetField(persistent, "discord_active", True), Function(init_discord), If(main_menu,
                            Function(main_menu_update_discord),
                            Function(update_discord)),
                        Function(init_discord), If(main_menu,
                            Function(main_menu_update_discord),
                            Function(update_discord))]

            null height (2 * gui.pref_spacing)
            hbox:
                style_prefix "slider"

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto Forward Time")

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

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


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
    yalign 1.0
    font gui.interface_2_font

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    # foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font gui.interface_2_font

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    # foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")
    font gui.interface_2_font

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

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        vbox:
            spacing 40
            for h in _history_list:

                hbox:

                    if h.who:
                        window:
                            xsize gui.history_name_width
                            right_padding 20
                            yalign 0.5
                            text h.who:
                                min_width gui.history_name_width
                                text_align 1.0
                                size 30
                                xalign 1.0
                                if "color" in h.who_args:
                                    color h.who_args["color"]
                    else:
                        null width gui.history_name_width

                    $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                    text what:
                        yalign 0.5
                        substitute False
                        size 29

            if not _history_list:
                label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

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

                imagebutton auto "gui/confirm_screen/yes_%s.png" action yes_action
                imagebutton auto "gui/confirm_screen/no_%s.png" action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_screen/Box.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


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
        text "[message!tq]"

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


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


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
define config.nvl_list_length = gui.nvl_list_length

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

#style pref_vbox:
#    variant "medium"
#    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    # zorder 100

    # if quick_menu:

    #     hbox:
    #         style_prefix "quick"

    #         xalign 0.5
    #         yalign 1.0

    #         textbutton _("Back") action Rollback()
    #         textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
    #         textbutton _("Auto") action Preference("auto-forward", "toggle")
    #         textbutton _("Menu") action ShowMenu()
## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        hbox at textbox_anim:
            pos (1290, 720)
            spacing 10
            imagebutton auto "gui/quick_buttons/back_%s.png" action Rollback()
            imagebutton auto "gui/quick_buttons/history_%s.png" action ShowMenu('history')
            imagebutton auto "gui/quick_buttons/skip_%s.png" selected_hover "gui/quick_buttons/skip_selected_idle.png" action Skip() alternate Skip(fast=True, confirm=True)
            imagebutton auto "gui/quick_buttons/auto_%s.png" selected_hover "gui/quick_buttons/auto_selected_idle.png" action Preference("auto-forward", "toggle")
            if not has_new_entries():
                imagebutton auto "gui/quick_buttons/journal_%s.png" action ShowMenu('journal')
            else:
                imagebutton auto "gui/quick_buttons/journal_notif_%s.png" action ShowMenu('journal')
        imagebutton auto "gui/quick_buttons/gear_%s.png" action ShowMenu('enter_game_menu') pos (30, 30)


#style window:
#    variant "small"
#    background "gui/phone/textbox.png"

#style radio_button:
#    variant "small"
#    foreground "gui/phone/button/radio_[prefix_]foreground.png"

#style check_button:
#    variant "small"
#    foreground "gui/phone/button/check_[prefix_]foreground.png"

#style nvl_window:
#    variant "small"
#    background "gui/phone/nvl.png"

#style main_menu_frame:
#    variant "small"
#    background "gui/phone/overlay/main_menu.png"

#style game_menu_outer_frame:
#    variant "small"
#   background "gui/phone/overlay/game_menu.png"

#style game_menu_navigation_frame:
#    variant "small"
#    xsize 510

#style game_menu_content_frame:
#    variant "small"
#    top_margin 0

#style pref_vbox:
#    variant "small"
#    xsize 600

#style bar:
#    variant "small"
#    ysize gui.bar_size
#    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
#    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

#style vbar:
#    variant "small"
#    xsize gui.bar_size
#    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
#    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

#style scrollbar:
#    variant "small"
#    ysize gui.scrollbar_size
#    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

#style vscrollbar:
#    variant "small"
#    xsize gui.scrollbar_size
#    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
#    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

#style slider:
#    variant "small"
#    ysize gui.slider_size
#    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
#    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

#style vslider:
#    variant "small"
#    xsize gui.slider_size
#    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
#    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

#style slider_pref_vbox:
#    variant "small"
#    xsize None

#style slider_pref_slider:
#    variant "small"
#    xsize 900
