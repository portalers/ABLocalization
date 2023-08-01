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
                        style_prefix "check"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
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


                vbox:
                    style_prefix "check"
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "{font=fonts/SourceHanSerifCN-Bold.otf}简体中文{/font}" action Language("Schinese")
                    textbutton "{font=fonts/SourceHanSerifTW-Bold.otf}繁體中文{/font}" action Language("Tchinese")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

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



## This increases the size of the quick buttons to make them easier to touch
## on tablets and phones.

screen quick_menu_will():
    variant "touch"

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
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("Hide") action HideInterface()
            textbutton _("Notebook") action (renpy.restart_interaction, ShowMenu('willnotes_screen'))


screen quick_menu():
    variant "touch"

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
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')
            textbutton _("Hide") action HideInterface()

###修复章节选择界面立绘异常问题
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
        add "sprites/nik/nik.webp" xpos 820 xysize(981,1080) ypos -474 alpha 0.75 zoom 0.8

screen will_select():
    vbox:
        grid 3 2:
            style_prefix "gslot"
            spacing gui.slot_spacing
            ## scene 1
            imagebutton idle "images/thumbnails/samthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 1), Hide("confirm"))
            imagebutton idle "images/thumbnails/wilthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 2), Hide("confirm"))
            imagebutton idle "images/thumbnails/wilthumb2.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 3), Hide("confirm"))
            imagebutton idle "images/thumbnails/puthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 4), Hide("confirm"))
            imagebutton idle "images/thumbnails/luthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "William", 5), Hide("confirm"))
            null
        add "sprites/william/wil.webp" xpos 800 xysize(961,1075) ypos -470 alpha 0.75 zoom 0.8

screen murdoch_select():
    vbox:
        grid 3 2:
            style_prefix "gslot"
            spacing gui.slot_spacing
            imagebutton idle "images/thumbnails/samthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 1), Hide("confirm"))
            imagebutton idle "images/thumbnails/murthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 2), Hide("confirm"))
            imagebutton idle "images/thumbnails/murthumb2.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 3), Hide("confirm"))
            imagebutton idle "images/thumbnails/puthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 4), Hide("confirm"))
            imagebutton idle "images/thumbnails/luthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Murdoch", 5), Hide("confirm"))
            null
        add "sprites/murdoch/mur.webp" xpos 800 xysize(961,1075) ypos -470 alpha 0.75 zoom 0.8

screen cliff_select():
    vbox:
        grid 3 2:
            style_prefix "gslot"
            spacing gui.slot_spacing
            imagebutton idle "images/thumbnails/samthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 1), Hide("confirm"))
            imagebutton idle "images/thumbnails/cliffthumb1.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 2), Hide("confirm"))
            imagebutton idle "images/thumbnails/cliffthumb2.jpg" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 3), Hide("confirm"))
            imagebutton idle "images/thumbnails/puthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 4), Hide("confirm"))
            imagebutton idle "images/thumbnails/luthumb.webp" action Confirm(spoiler_message, Function(call_chapter_select, "Clifford", 5), Hide("confirm"))
            null
        add "sprites/cliff/cli.webp" xpos 900 xysize(748,925) ypos -350 alpha 0.75 zoom 0.8