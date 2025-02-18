## Авторское право 2019-2024 Азариэль Дель Кармен (bronya_rand). Все права защищены.

## lockdown_check.rpy
# Этот файл, в основном, предназначен для предупреждения мододелов-новичков о багах
# в конкретных версиях Ren'Py или чтобы предупредить их о проблемах Контроля качества в
# случае с версиями Ren'Py, которые вышли позднее той, на которой тестировался мод-шаблон.
# Нововведение в 4.0.0: Добавлено программное ограничение для Ren'Py версий 6/7 в Py3-шаблонах.

## НЕ МОДИФИЦИРУЙТЕ ЭТОТ ФАЙЛ! ##

# Проверяем, запущен ли проект на движке Ren'Py 8-й ревизии
python early:

    if renpy.version_tuple[0] != 8:
        raise NotRenPyEight

label lockdown_check:

    $ version = renpy.version()

    if renpy.version_tuple > (8, 3, 3, 24111502):

        scene black
        "{b}Внимание:{/b} Версия Ren'Py, на которой вы пытаетесь написать модификацию для DDLC, не была проверена на предмет совместимости с модификациями."
        "Самая недавняя версия Ren'Py 8-й ревизии, которая работает с модификациями для DDLC – «{i}Ren'Py 8.3.3{/i}»."
        "Запуск DDLC или вашей модификации на версии выше проверенной может привести к появлению багов и прочих сломанных функций игры."

        menu:
            "Продолжая запуск своей модификации на [version!q], вы соглашаетесь с тем, что вы прочитали текст этого предупреждения и осознаёте факт возникновения проблем на непроверенной версии Ren'Py."
            "Я согласен.":
                $ persistent.lockdown_warning = True
                return

    else:
        $ persistent.lockdown_warning = True
        return
