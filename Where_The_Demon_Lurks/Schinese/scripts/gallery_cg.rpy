screen gallery_cg():
    tag menu
    default page = 0
    add persistent.mm_image at g_to_m_blur
    add CGGUI_PATH + 'cg_gallery.png'
    label _("CG GALLERY") pos(50, 15) text_size 60
    text _("Use the pin to set the main menu CG") size 30 xsize 250 pos(1570, 40) text_align 1.
    label _("{#CGGalleryPage}第" + str(page+1) + "页") xalign .5 yalign .8 text_text_align .5 text_size 60 
    if page > 0:
        imagebutton auto GUI_LEFT_BUTTON_AUTO action SetScreenVariable('page', page - 1) pos(486, 815) at half_size
    if page*6+6 < len(CG_LIST):
        imagebutton auto GUI_RIGHT_BUTTON_AUTO action SetScreenVariable('page', page + 1) pos(1319, 815) at half_size
    grid 3 2:
        $ count = 0
        xalign .5 yalign .3
        for img in CG_LIST[page*6: min(page*6+6, len(CG_LIST))]:
            $ count += 1
            fixed:
                xysize (432, 294)
                button:
                    idle_child img.idle
                    hover_child img.hover
                    insensitive_child img.idle
                    action Show('show_cg', img=img.img)
                    sensitive img.unlocked
                    focus_mask True
                if img.unlocked:
                    imagebutton auto CGGUI_PATH + 'pin_button_%s.png': 
                        action SelectedIf(SetField(persistent, 'mm_image', img.img)) 
                        pos(384, 10) 
                        focus_mask None
                        selected_hover CGGUI_PATH + 'pin_button_selected_idle.png'
        if count < 6:
            for i in range(6-count):
                null

    imagebutton auto "gui/game_menu_buttons/back_%s.png" action ShowMenu('gallery_main') xpos .05 yalign 0.98 at half_size

translate Schinese strings:

    # game/scripts/gallery_cg.rpy:85
    old "CG GALLERY"
    new "美术室"

    # game/scripts/gallery_cg.rpy:86
    old "Use the pin to set the main menu CG"
    new "可用图钉设置背景"

