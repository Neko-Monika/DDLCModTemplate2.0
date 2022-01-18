## console.rpy

# Этот файл содержит определения содержимого консоли Моники,
# появляющейся в игре, когда Моника удаляет персонажей.

# Это изображение создаёт серую «коробку» для внутриигровой консоли.
image console_bg:
    "#333"
    topleft
    alpha 0.75 xysize (480,180)

# Этот стиль объявляет оформление отображаемого текста во внутриигровой консоли.
style console_text:
    font "gui/font/consola.ttf"
    color "#fff"
    size 18
    outlines []

# Этот стиль управляет скоростью вывода отображаемого текста во внутриигровой консоли.
style console_text_console is console_text:
    slow_cps 30

# Эта переменная хранит весь ввод и вывод (т.е. «выхлоп») внутриигровой консоли.
default consolehistory = []

# Это изображение отображает текст во внутриигровой консоли.
image console_text = ParameterizedText(style="console_text_console", anchor=(0,0), xpos=30, ypos=10)

# Это изображение показывает историю команд во внутриигровой консоли.
image console_history = ParameterizedText(style="console_text", anchor=(0,0), xpos=30, ypos=50)

# Это изображение показывает стрелку в консоли справа от вводимой команды
# во внутриигровой консоли.
image console_caret = Text(">", style="console_text", anchor=(0,0), xpos=5, ypos=10)

# Этот лейбл вызывает консоль для дальнейшей манипуляции с командами.
label updateconsole(text="", history=""):
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    show console_text "[text]" as ctext zorder 100
    $ pause(len(text) / 30.0 + 0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    $ pause(0.5)
    return

# Примечание переводчика: этот лейбл используется для пропуска консоли в титрах, когда игрок 
# прошёл DDLC на Истинную концовку; аффтар просто внушил себе бог знает что.
# Для стирания всей истории консоли используйте `$ consolehistory = []`
label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    $ pause(0.5)
    return

# Этот лейбл является устаревшей реализацией внутриигровой консоли, почему-то оставленной в исходном скрипте.
label updateconsole_old(text="", history=""):
    $ starttime = datetime.datetime.now()
    $ textlength = len(text)
    $ textcount = 0
    show console_bg zorder 100
    show console_caret zorder 100
    show console_text "_" as ctext zorder 100
    label updateconsole_loop:
        $ currenttext = text[:textcount]
        call drawconsole (drawtext=currenttext)
        $ pause_duration = 0.08 - (datetime.datetime.now() - starttime).microseconds / 1000.0 / 1000.0
        $ starttime = datetime.datetime.now()
        if pause_duration > 0:
            $ pause(pause_duration / 2)
        $ textcount += 1
        if textcount <= textlength:
            jump updateconsole_loop

    $ pause(0.5)
    hide ctext
    show console_text "_" as ctext zorder 100
    call updateconsolehistory (history)
    $ pause(0.5)
    return

    label drawconsole(drawtext=""):

        show console_text "[drawtext]_" as ctext zorder 100

        return

# Этот лейбл добавляет конкретный текст в историю консоли.
label updateconsolehistory(text=""):
    if text:
        python:
            consolehistory.insert(0, text)
            if len(consolehistory) > 5:
                del consolehistory[5:]
            consolehistorydisplay = '\n'.join(map(str, consolehistory))
        show console_history "[consolehistorydisplay]" as chistory zorder 100
    return

# Этот лейбл скрывает внутриигровую консоль.
label hideconsole:
    hide console_bg
    hide console_caret

    hide ctext
    hide chistory
