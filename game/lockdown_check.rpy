# Lockdown_check.rpy

# Этот файл не является частью DDLC. Этот файл, в основном, предназначен
# для предупреждения новичков о проблемах шаблона с конкретными версиями
# Ren'Py или предупредить их о Контроле качества в случае с версиями
# Ren'Py, которые вышли позднее, чем та, на которой тестировался шаблон.
## НЕ МОДИФИЦИРУЙТЕ ЭТОТ ФАЙЛ! ##

label lockdown_check:

    if renpy.version_tuple >= (7, 4, 6, 1693):
        scene black
        "{b}Внимание:{/b} В релизе \"Ren'Py 7.4.6\" был обнаружен баг, который сильно ломает трансформации DDLC."
        "Этот баг в какой-то мере ещё присутствует в Ren'Py версий 7.4.7 и выше, и нет гарантии, что этот баг будет исправлен в будущих релизах."
        "Пока что нет способа решить данную проблему. И поэтому Мод-шаблон будет неработоспособен на какой-либо версии Ren'Py выше 7.4.5."
        "На данный момент времени, если вы хотите писать модификации для DDLC на Ren'Py 7, вы должны использовать {a=https://renpy.org/release/7.4.5}{i}Ren'Py 7.4.5{/i}{/a} и ждать, пока проблема не будет устранена в новом релизе и данный факт не будет проверен лично GanstaKingofSA."
        "Простите за доставленные неудобства. Но мы желаем вам приятного моддинга!"
        $ renpy.quit()
    else:
        $ persistent.lockdown_warning = True
        return
