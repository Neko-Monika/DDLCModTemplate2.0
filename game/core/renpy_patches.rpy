## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

## renpy_patches.rpy
# Этот файл, в основном, предназначен для патчинга конкретных версий Ren'Py, которые ломают
# DDLC или модификации к ней, путём внесения правок в движок Ren'Py перед стартом.

python early:
    import os
    ## Забор значений из Инструментария управления Windows путём использования класса Powershell Get-WmiObject (для Windows 11)
    os.environ['wmic process get Description'] = "powershell (Get-Process).ProcessName"
    os.environ['wmic os get version'] = "powershell (Get-WmiObject -class Win32_OperatingSystem).Version"

    ## Отображаемые элементы, использующие ATL, запускают свою анимацию при первом появлении,
    ## а не в том случае, когда появился сам экран.
    ## Нижеследующие две строки отключают подобное поведение ради блага трансформаций DDLC.
    if renpy.version_tuple >= (7, 4, 7, 1862):
        config.atl_start_on_show = False 
