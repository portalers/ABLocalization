translate Tchinese python:
    ### 簡轉繁 SourceHanSerifCN-Medium -> SourceHanSerifTC-Medium.otf
    gui.text_font = gui.preference("font_1", "font/SourceHanSerifTC-Medium.otf")

    gui.name_text_font = gui.preference("font_2", "font/HanyiSentyMarshmallow.ttf")
    gui.interface_text_font = gui.preference("font_3", "font/HuaWenZhongSong-Bold.ttf")

    ### 繁體缺字 HYYuanLongHei-90W.ttf -> GenSenRounded-H.ttc
    gui.interface_2_font = gui.preference("font_4", "font/GenSenRounded-H.ttc")

    ### 繁體缺字 shuainantuan.ttf -> HanyiSentyCrayon-non-color.ttf
    gui.journal_font = gui.preference("font_5", "font/HanyiSentyCrayon-non-color.ttf")

    gui.button_text_font = gui.interface_text_font
    gui.choice_button_text_font = gui.text_font
    gui.text_size = 38
