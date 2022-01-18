## console.rpy

# Этот файл содержит определения содержимого консоли Моники,
# появляющейся в игре, когда Моника удаляет персонажей.

# Данный файл был сильно изменён по сравнению с ревизией из оригинального DDLC, чтобы обеспечить
# лучший доступ к вызову консоли, нежели чем через лейблы. Для вызова пропишите $ run_input(input="Команда", output="Результат").
# А для того, чтобы просто отобразить консоль, пропишите `show screen console_screen`.
# Благодарим Lezalith за помощь в создании этой новой консоли!

init -1:

    # None или кортеж с (input, output).
    default new_input = None

    # Список с результатами команд.
    default console_history = []

    # Не предназначено для изменения во время игры.
    # Задержка после введённой команды и перед отображением её результата.
    define console_delay = 0.5

    define console_cps = 30

init python:

    # Заставить консоль отобразить указанные команду и результат.
    def run_input(input, output):
        global new_input

        new_input = (input, output)

        if renpy.get_screen("console_screen"):
            renpy.hide_screen("console_screen")
        renpy.call_screen("console_screen", finish=True)
        renpy.show_screen("console_screen")

    # Добавить результат команды в историю.
    def add_to_history(input):
        global console_history

        console_history.insert(0, input[1])
        if len(console_history) > 5:
            console_history.pop(5)

    # Add the output to history after code is done
    def input_finished():
        global new_input

        add_to_history(new_input)
        new_input = None
        
        renpy.restart_interaction()

    def clear_history():
        global console_history

        console_history = []

screen console_screen(finish=False):

    style_prefix "console_screen"

    default finish_actions = [Function(input_finished), SetScreenVariable("in_progress", False), Return()]

    # Строка введённой команды для отображения.
    # Она добавляется вне переменной new_input, дабы оная
    # не показывалась снова и снова.
    default new_input_code = "_"

    # Меняется на True, когда идёт обновление текста команды (code_text)
    default in_progress = False

    # Если текст сейчас не выводится посимвольно.
    if not in_progress:

        $ new_input_code = "_"

        # Если доступен new_input, он устанавливается в качестве отображаемого кода.
        if store.new_input:

            $ in_progress = True
            $ new_input_code = store.new_input[0]

    # Начинает показываться новый код.
    if in_progress:

        timer ( float(len(renpy.filter_text_tags(new_input_code, deny = []))) / float(console_cps) + console_delay ) action finish_actions

    frame:

        vbox:
            hbox:
                text ">" xpos 5 ypos 10

                text new_input_code xpos 15 ypos 10:
                    slow_cps 30
                    xmaximum 460

            vbox:
                xpos 26 ypos 30 
                spacing 5
                for x in store.console_history:
                    text x

style console_screen_frame:
    background Frame(Transform(Solid("#333"), alpha=0.75))
    xsize 480
    ysize 180

# Этот стиль объявляет оформление отображаемого текста во внутриигровой консоли.
style console_screen_text:
    font "gui/font/consola.ttf"
    color "#fff"
    size 18
    outlines []

# Этот лейбл очищает историю внутриигровой консоли и введённых команд.
# Было решено оставить его, т.к. он просто добавляет паузу в некоторых местах.
label updateconsole_clearall(text="", history=""):
    $ pause(len(text) / 30.0 + 0.5)
    $ pause(0.5)
    return
