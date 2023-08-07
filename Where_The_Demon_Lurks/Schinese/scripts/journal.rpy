screen journal():
    default curr_tab = "Names"
    default curr_entry = None
    default curr_page = 1
    # Decoupling tab name from journal entry type to help with translations
    default tab_text = ""
    if curr_tab in JOURNAL_TAB_TRANSLATIONS:
        $ tab_text = JOURNAL_TAB_TRANSLATIONS[curr_tab]
    $ entry_list = get_entries_of_type(curr_tab)
    style_prefix "journal_"
    fixed:
        xysize (1357, 946)
        xalign 0.5 yalign 0.5
        add "gui/journal/journal_base.png"

        label tab_text pos (210,60):
            text_size gui.journal_title_size
            text_kerning 5
            text_color "000"
            text_font gui.journal_font
        label _("INFO{#journal}") pos (730,60):
            text_size gui.journal_title_size
            text_kerning 5
            text_color "000"
            text_font gui.journal_font
        ### ENTRY INFO ###
        # Handled first so new status can be cleared before notification added
        side "c r":
            xysize(470, 650)
            pos (730, 180)
            viewport id "message_list":
                vbox:
                    for message in get_journal_notes(curr_entry):
                        text message:
                            font gui.journal_font
                            size 33
                            color "000"
            bar:
                style "journal_vscrollbar"
                value YScrollValue("message_list")
        ### ENTRY LIST ###
        fixed:
            xysize(470, 650)
            pos (210, 140)
            vbox:
                for i in range(4):
                    $ curr_index = 4 * (curr_page - 1) + i
                    if curr_index < len(entry_list):
                        $ entry = entry_list[curr_index]
                        button:
                            xysize (441,154)
                            action SetScreenVariable("curr_entry", entry)
                            add "gui/journal/journal_tag.png"
                            text entry xalign 0.5 yalign 0.95:
                                font gui.journal_font
                                size 40
                                color "000"
                            if is_entry_new(entry):
                                add "gui/journal/journal_notif.png"
                    else:
                        null
            if len(entry_list) > 4:
                hbox:
                    xcenter 0.46 ypos 630
                    imagebutton auto "gui/journal/j_left_%s.png" action SetScreenVariable("curr_page", curr_page - 1) sensitive curr_page > 1
                    text str(curr_page) yalign 0.5:
                        min_width 100
                        text_align 0.5
                        font gui.journal_font
                        size 40
                        color "000"
                    imagebutton auto "gui/journal/j_right_%s.png" action SetScreenVariable("curr_page", curr_page + 1) sensitive curr_page < (len(entry_list) / 4) + 1
        ### TABS ###
        imagebutton auto "gui/journal/j_contact_%s.png" selected_hover "gui/journal/j_contact_selected_idle.png":
            action [SetScreenVariable("curr_tab", "Names"), SetScreenVariable("curr_entry", None), SetScreenVariable("curr_page", 1)]
            focus_mask "gui/journal/j_contact_idle.png"
            selected curr_tab == "Names"
        imagebutton auto "gui/journal/j_location_%s.png" selected_hover "gui/journal/j_location_selected_idle.png":
            action [SetScreenVariable("curr_tab", "Locations"), SetScreenVariable("curr_entry", None), SetScreenVariable("curr_page", 1)]
            focus_mask "gui/journal/j_location_idle.png"
            selected curr_tab == "Locations"
        ### CLOSE BUTTON ###
        imagebutton auto "gui/journal/j_close_%s.png" action Return() focus_mask "gui/journal/j_close_idle.png"

translate Schinese strings:

    # game/journal.rpy:42
    old "NAMES{#journal}"
    new "名称{#journal}"

    # game/journal.rpy:42
    old "LOCATIONS{#journal}"
    new "地点{#journal}"

    # game/journal.rpy:66
    old "INFO{#journal}"
    new "介绍{#journal}"

