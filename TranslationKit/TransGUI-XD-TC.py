import os, tkinter, customtkinter, TranslationKit

customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

not2TransFile = ['define.rpy', 'options.rpy', 'screens.rpy']
pathResource = ""
pathDestination = ""
pathResult = ""
nameTranlation = 'Tchinese'
dupHashOverride = True
editFullwidthPunctuation = True
stringsBlockOverride = False
useMT = False
newPrefix = '@@@'
MTLang='zh-TW'
doneText = ' done '


app = customtkinter.CTk()
app.geometry("1040x585")
app.minsize(1040, 585)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)


app.title("TransGUI-XD")


def button_callback1():
    global pathResource
    pathResource = tkinter.filedialog.askdirectory() + '/'
    text_1.configure(state="normal")
    text_1.delete('0.0', 'end')
    text_1.insert("0.0", pathResource)
    text_1.configure(state="disabled")
    print(pathResource)

def button_callback2():
    global pathDestination
    pathDestination =  tkinter.filedialog.askdirectory() + '/'
    text_2.configure(state="normal")
    text_2.delete('0.0', 'end')
    text_2.insert("0.0", pathDestination)
    text_2.configure(state="disabled")
    print(pathDestination)

def button_callback3():
    global pathResult
    pathResult =  tkinter.filedialog.askdirectory() + '/'
    text_3.configure(state="normal")
    text_3.delete('0.0', 'end')
    text_3.insert("0.0", pathResult)
    text_3.configure(state="disabled")
    print(pathResult)

def button_callback4():

    if pathResource and pathDestination and pathResult and entry.get() and prefix.get():
        if pathResource == pathDestination:
            resourceFiles = [f for f in os.listdir(pathResource) if f.endswith('.rpy') and os.path.isfile(os.path.join(pathResource, f)) and f not in not2TransFile]
            i = 0
            for f in resourceFiles:
                print(f)
                i += 1
                progressbar_1.set(i/len(resourceFiles))
                app.update()
                tmpTC = TranslationKit.TransFileHandler(sourcePath=pathResource, destinationPath=pathResource, resultPath=pathResource, fileName=f, tranlationName=entry.get())
                tmpTC.initNewTransFile(stringsBlockOverride=stringsBlockOverride, dupHashOverride=dupHashOverride, editFullwidthPunctuation=editFullwidthPunctuation, newPrefix=prefix.get(), useMT=useMT, MTLang=MTLang)
            del tmpTC
            print(f'{doneText:#^50}')
            window = customtkinter.CTkToplevel(app)
            window.title('完成提示')
            window.geometry("320x180")
            def destroy_windows():
                progressbar_1.set(0.0)
                window.destroy()
            button_window = customtkinter.CTkButton(master=window, text='完成！', font=customtkinter.CTkFont(size=36, family='STHeiti'), command=destroy_windows)
            button_window.pack(padx=60, pady=40, fill="both", expand=True)
        else:
            resourceFiles = [f for f in os.listdir(pathResource) if f.endswith('.rpy') and os.path.isfile(os.path.join(pathResource, f)) and f not in not2TransFile]
            destinationFiles = [f for f in os.listdir(pathDestination) if f.endswith('.rpy') and os.path.isfile(os.path.join(pathDestination, f)) and f not in not2TransFile]
            matchFiles = set(resourceFiles) & set(destinationFiles)
            i = 0
            for f in matchFiles:
                print(f)
                i += 1
                progressbar_1.set(i/len(resourceFiles))
                app.update()
                tmpTC = TranslationKit.TransFileHandler(sourcePath=pathResource, destinationPath=pathDestination, resultPath=pathResult, fileName=f, tranlationName=entry.get())
                tmpTC.findDiff(followOrginOrder=True)
                tmpTC.initNewTransFile(stringsBlockOverride=stringsBlockOverride, dupHashOverride=dupHashOverride, editFullwidthPunctuation=editFullwidthPunctuation, newPrefix=prefix.get(), useMT=useMT, MTLang=MTLang)
            del tmpTC
            print(f'{doneText:#^50}')
            window = customtkinter.CTkToplevel(app)
            window.title('完成提示')
            window.geometry("320x180")
            def destroy_windows():
                progressbar_1.set(0.0)
                window.destroy()
            button_window = customtkinter.CTkButton(master=window, text='完成！', font=customtkinter.CTkFont(size=36, family='STHeiti'), command=destroy_windows)
            button_window.pack(padx=60, pady=40, fill="both", expand=True)

def button_callback5():

    if pathResult and entry.get() and prefix.get():
        resourceFiles = [f for f in os.listdir(pathResult) if f.endswith('.rpy') and os.path.isfile(os.path.join(pathResult, f)) and f not in not2TransFile]
        i = 0
        for f in resourceFiles:
            print(f)
            i += 1
            progressbar_1.set(i/len(resourceFiles))
            app.update()
            tmpTC = TranslationKit.TransFileHandler(sourcePath=pathResult, destinationPath=pathResult, resultPath=pathResult, fileName=f, tranlationName=entry.get())
            if useMT:
                tmpTC.rawSourceFile = []
            tmpTC.initNewTransFile(stringsBlockOverride=stringsBlockOverride, dupHashOverride=dupHashOverride, editFullwidthPunctuation=editFullwidthPunctuation, newPrefix=prefix.get(), useMT=useMT, MTLang=MTLang)
        del tmpTC
        print(f'{doneText:#^50}')
        window = customtkinter.CTkToplevel(app)
        window.title('完成提示')
        window.geometry("320x180")
        def destroy_windows():
            progressbar_1.set(0.0)
            window.destroy()
        button_window = customtkinter.CTkButton(master=window, text='完成！', font=customtkinter.CTkFont(size=36, family='STHeiti'), command=destroy_windows)
        button_window.pack(padx=60, pady=40, fill="both", expand=True)

def checkbox_event1():
    print("checkbox1 toggled, current value:", check_var_1.get())
    global dupHashOverride
    if check_var_1.get() == 'on':
        dupHashOverride = True
    else:
        dupHashOverride = False
    print(dupHashOverride)
def checkbox_event2():
    print("checkbox2 toggled, current value:", check_var_2.get())
    global editFullwidthPunctuation
    if check_var_2.get() == 'on':
        editFullwidthPunctuation = True
    else:
        editFullwidthPunctuation = False
    print(editFullwidthPunctuation)
def checkbox_event3():
    print("checkbox3 toggled, current value:", check_var_3.get())
    global stringsBlockOverride
    if check_var_3.get() == 'on':
        stringsBlockOverride = True
    else:
        stringsBlockOverride = False
    print(stringsBlockOverride)

def checkbox_event4():
    global useMT
    if check_var_4.get() == 'on':
        useMT = True
    else:
        useMT = False
    print(useMT)

def change_appearance_mode_event(appearance_mode_optionemenu):
    customtkinter.set_appearance_mode(appearance_mode_optionemenu)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.grid(row=0, column=0, rowspan=10, columnspan=1, sticky="nsew", pady=40, padx=(10,30))
frame_2 = customtkinter.CTkFrame(master=app)
frame_2.grid(row=0, column=1, rowspan=10, columnspan=4, sticky="nsew", pady=40, padx=(0,10))

check_var_1 = tkinter.StringVar(master=frame_1, value="on")
checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="重複內容刪舊留新", command=checkbox_event1,
                                     variable=check_var_1, onvalue="on", offvalue="off", font=customtkinter.CTkFont(family='STHeiti'))
checkbox_1.grid(row=1, column=0, sticky="nsew", pady=(20,0), padx=20)

check_var_2 = tkinter.StringVar(master=frame_1, value="on")
checkbox_2 = customtkinter.CTkCheckBox(master=frame_1, text="修飾標點符號", command=checkbox_event2,
                                     variable=check_var_2, onvalue="on", offvalue="off", font=customtkinter.CTkFont(family='STHeiti'))
checkbox_2.grid(row=2, column=0, sticky="nsew", pady=(40,0), padx=20)

check_var_3 = tkinter.StringVar(master=frame_1, value="off")
checkbox_3 = customtkinter.CTkCheckBox(master=frame_1, text="Strings Block區域\n來源資料覆蓋目標", command=checkbox_event3,
                                     variable=check_var_3, onvalue="on", offvalue="off", font=customtkinter.CTkFont(family='STHeiti'))
checkbox_3.grid(row=3, column=0, sticky="nsew", pady=(40,0), padx=20)

check_var_4 = tkinter.StringVar(master=frame_1, value="off")
checkbox_4 = customtkinter.CTkCheckBox(master=frame_1, text="目標未填寫入機翻\n(會有前綴'@@@')\n大約500句/分鐘\n很慢慎用", command=checkbox_event4,
                                     variable=check_var_4, onvalue="on", offvalue="off", font=customtkinter.CTkFont(family='STHeiti'))
checkbox_4.grid(row=4, column=0, sticky="nsew", pady=(30,0), padx=20)

entry_label = customtkinter.CTkLabel(master=frame_1, text="翻譯檔名稱(可輸入)：", anchor="w", font=customtkinter.CTkFont(family='STHeiti'))
entry_label.grid(row=5, column=0, sticky="nsew", pady=(30,0), padx=20)
entry = customtkinter.CTkEntry(master=frame_1, placeholder_text=nameTranlation)
entry.insert(0, nameTranlation)
entry.grid(row=6, column=0, sticky="nsew", pady=(0,0), padx=20)

prefix_label = customtkinter.CTkLabel(master=frame_1, text="未填/機翻前綴(不可空)：", anchor="w", font=customtkinter.CTkFont(family='STHeiti'))
prefix_label.grid(row=7, column=0, sticky="nsew", pady=(0,0), padx=20)
prefix = customtkinter.CTkEntry(master=frame_1, placeholder_text=newPrefix)
prefix.insert(0, newPrefix)
prefix.grid(row=8, column=0, sticky="nsew", pady=(0,20), padx=20)

appearance_mode_label = customtkinter.CTkLabel(master=frame_1, text="主題顏色：", anchor="w", font=customtkinter.CTkFont(family='STHeiti'))
appearance_mode_label.grid(row=9, column=0, sticky="nsew", pady=(10,0), padx=15)
appearance_mode_optionemenu = customtkinter.CTkOptionMenu(master=frame_1, values=["Dark", "Light", "System"],
                                                                       command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=10, column=0, sticky="nesw", pady=0, padx=(10,10))


text_1 = customtkinter.CTkTextbox(master=frame_2, width=560, height=20)
text_1.insert("0.0", pathResource)
text_1.configure(state="disabled")
text_1.grid(row=1, column=2, rowspan=1, columnspan=2, sticky="nsew", pady=(60,0), padx=10)
button_1 = customtkinter.CTkButton(master=frame_2, text='\U0001F4C1 來源檔案路徑(舊翻資料)', command=button_callback1, font=customtkinter.CTkFont(family='STHeiti'))
button_1.grid(row=1, column=4, rowspan=1, columnspan=1, sticky="nsew", pady=(60,0), padx=0)


text_2 = customtkinter.CTkTextbox(master=frame_2, width=560, height=20)
text_2.insert("0.0", pathDestination)
text_2.configure(state="disabled")
text_2.grid(row=2, column=2, rowspan=1, columnspan=2, sticky="nsew", pady=(40,0), padx=10)
button_2 = customtkinter.CTkButton(master=frame_2, text='\U0001F4C1 目標檔案路徑(新版未填)', command=button_callback2, font=customtkinter.CTkFont(family='STHeiti'))
button_2.grid(row=2, column=4, rowspan=1, columnspan=1, sticky="nsew", pady=(40,0), padx=0)


text_3 = customtkinter.CTkTextbox(master=frame_2, fg_color="#50577A", width=500, height=20)
text_3.insert("0.0", pathResult)
text_3.configure(state="disabled")
text_3.grid(row=3, column=2, rowspan=1, columnspan=2, sticky="nsew", pady=(60,0), padx=10)
button_3 = customtkinter.CTkButton(master=frame_2, text='\U0001F4C1 輸出檔案/只做選項修飾路徑', fg_color='#41416A', hover_color='#2E2E5C', command=button_callback3, font=customtkinter.CTkFont(family='STHeiti'))
button_3.grid(row=3, column=4, rowspan=1, columnspan=1, sticky="nsew", pady=(60,0), padx=0)

button_4 = customtkinter.CTkButton(master=frame_2, text='\U000025B6  生成製作開始', font=customtkinter.CTkFont(family='STHeiti' ,size=40, weight='bold'), fg_color='#0091ea', width=400, height=120, command=button_callback4)
button_4.grid(row=7, column=3, rowspan=3, columnspan=2, sticky="nsw", pady=(120,0), padx=(0, 40))

button_5_label = customtkinter.CTkLabel(master=frame_2, text="只做選項修飾檔案啟動鈕\n(重複內容刪舊留新，修飾標點符號等等)\n！！！特別注意！！！\n如果開啟使用'機翻'選項\n再點這個鈕是整份當新的送去機翻", anchor="center", font=customtkinter.CTkFont(family='STHeiti'))
button_5_label.grid(row=7, column=2, sticky="sw", pady=(120,0), padx=(40, 10))
button_5 = customtkinter.CTkButton(master=frame_2, text='\U000025B6 只做選項修飾檔案啟動鈕',font=customtkinter.CTkFont(family='STHeiti', size=18), fg_color='#6B728E', hover_color='#46466F', width=100, height=28, command=button_callback5)
button_5.grid(row=8, column=2, rowspan=1, columnspan=1, sticky="sw", pady=(0,0), padx=(40, 10))

progressbar_1 = customtkinter.CTkProgressBar(master=app, progress_color='#4E9F3D')
progressbar_1.grid(row=8, column=0, rowspan=2, columnspan=5, sticky="nsew", pady=(10,20), padx=(10,10))
progressbar_1.set(0.0)


app.mainloop()
