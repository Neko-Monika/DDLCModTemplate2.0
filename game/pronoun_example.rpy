## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.
## Вы можете использовать этот файл/эту функцию только в модификациях для DDLC, а не для патчеров,
## неофициальных фиксов DDLC, и так далее.

## pronoun_example.rpy

# Этот файл служит примером функции местоимений.
# Используйте это в качестве примера, дабы научиться пользоваться этой функцией.

label pronoun_example:
    stop music fadeout 2.0
    scene bg club_day
    with dissolve_scene_full
    jump pronoun_menu
    
label pronoun_menu:
    menu:
        "Сделай выбор."
        "Выбрать местоимение":
            call set_pronoun

        "Текущее местоимение":
            if not he:
                "Вы пока не выбрали местоимение."
            else:
                "Ваше текущее местоимение: [he_capital]/[him_capital]."
            jump pronoun_menu

        "Проиграть пример.":
            if not he:
                "Вы пока не выбрали местоимение. Выберите его, прежде чем продолжить."
                jump pronoun_menu
            mc "Мои местоимения – [he]/[him]."
            m "[he_capital] здесь, чтобы узнать о том, что [he] тот ещё чёрт."
            s "Не говори про н[are] такое!"
            n "[he_capital] мне не очень нравится."
            y "С н-н[hes] всё будет хорошо?"
            jump pronoun_menu

        "Очистить местоимения":
            $ he = ""
            $ him = ""
            $ are = ""
            $ hes = ""
            $ he_capital = ""
            $ him_capital = ""
            $ are_capital = ""
            $ hes_capital = ""
            $ finishPronouns()

            "Все местоимения очищены."
            jump pronoun_menu
            
        "Выйти":
            return
    return

label set_pronoun:
    menu:
        "Какие твои местоимения?"
        "Он/Ему":
            $ he = "он"
            $ him = "ему"
            $ are = "его"
            $ hes = "им"
            $ finishPronouns()

            "Местоимения установлены на «Он/Ему»."

        "Она/Ей":
            $ he = "она"
            $ him = "ей"
            $ are = "её"
            $ hes = "ей"
            $ finishPronouns()

            "Местоимения установлены на «Она/Ей»."

    $ he_capital = he.capitalize()
    $ him_capital = him.capitalize()
    $ are_capital = are.capitalize()
    $ hes_capital = hes.capitalize()
    jump pronoun_menu