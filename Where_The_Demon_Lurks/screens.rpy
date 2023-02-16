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
                # Additional vboxes of type "radio_pref" or "check_pref" can be
                # added here, to add additional creator-defined preferences.

            null height (2 * gui.pref_spacing)
            hbox:
                
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



screen quick_menu():
    variant "touch"

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

