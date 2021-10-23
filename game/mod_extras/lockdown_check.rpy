## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

## lockdown_check.rpy
# Этот файл, в основном, предназначен для предупреждения мододелов-новичков о багах
# в конкретных версиях Ren'Py или чтобы предупредить их о проблемах Контроля качества в
# случае с версиями Ren'Py, которые вышли позднее той, на которой тестировался мод-шаблон.

## НЕ МОДИФИЦИРУЙТЕ ЭТОТ ФАЙЛ! ##

label lockdown_check:

    $ version = renpy.version()

    if renpy.version_tuple > (7, 4, 11, 2266):
        scene black
        "{b}Внимание:{/b} Версия Ren'Py, на которой вы пытаетесь написать модификацию для DDLC, не была проверена на предмет совместимости с модификациями."
        "Самая недавняя версия Ren'Py, которая работает с модификациями для DDLC – «{i}Ren'Py 7.4.11{/i}»."
        "Запуск DDLC или вашей модификации для DDLC на версии выше проверенной может привести к появлению багов и прочих сломанных функций игры."

        menu:
            "Продолжая запуск своей модификации на версии [version!q], вы соглашаетесь с тем, что вы прочитали текст этого предупреждения и осознаёте факт возникновения проблем на непроверенной версии Ren'Py."
            "Я согласен.":
                $ persistent.lockdown_warning = True
                return

    else:
        $ persistent.lockdown_warning = True
        return
