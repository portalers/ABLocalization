define config.default_language = "Schinese"

init python:
    config.font_replacement_map["font/HYYuanLongHei-90W.ttf", True, False] = ("font/HYYuanLongHei-90W.ttf", False, False)

screen preferences():

    tag menu
    if main_menu:
        add persistent.mm_image at g_to_m_blur
    add 'gui/overlay/Preferences.png'
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

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (2 * gui.pref_spacing)
            hbox:
                vbox:
                    style_prefix "radio"
                    xsize 430
                    label _("Discord Integration")
                    textbutton _("{#DiscordPreference}On") action [SetField(persistent, "discord_active", True), Function(init_discord), If(main_menu,
                        Function(main_menu_update_discord),
                        Function(update_discord)),
                    Function(init_discord), If(main_menu,
                        Function(main_menu_update_discord),
                        Function(update_discord))]
                    textbutton _("{#DiscordPreference}Off") action [SetField(persistent, "discord_active", False), Function(disconnect_discord)]
                    
                vbox:
                    style_prefix "check"
                    label _("Nipples")
                    textbutton _("{#NipplesPreference}On") action SelectedIf(SetField(preferences, "nip_enabled", True))
                    textbutton _("{#NipplesPreference}Off") action SelectedIf(SetField(preferences, "nip_enabled", False))
                vbox:
                    style_prefix "check"
                    label _("Language")
                    textbutton _("{font=font/DenseLetters-nRgDO.otf}English") action Language(None)
                    textbutton _("{font=font/HYYuanLongHei-90W.ttf}简体中文{/font}") action [SelectedIf(Language("Schinese")), gui.SetPreference("journal_title_size", 80), If(main_menu, main_menu_update_discord, update_discord)]
                    textbutton _("{font=font/HYYuanLongHei-90W.ttf}繁體中文{/font}") action [SelectedIf(Language("Tchinese")), gui.SetPreference("journal_title_size", 80), If(main_menu, main_menu_update_discord, update_discord)]

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