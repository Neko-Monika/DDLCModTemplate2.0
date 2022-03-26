## Авторское право 2019-2022 Азариэль Дель Кармен (GanstaKingofSA). Все права защищены.

# bsod.rpy
# В этом файле содержится код экрана для отображения ложного Синего экрана смерти.

## Экран Синего экрана смерти ############################################################
##
## Этот экран используется для мимикрии СЭС/паники ядра на компьютере игроков на всех
## возможных платформах (на мобильных устройствах будет использоваться экран паники ОС Linux).
##
## Синтаксис:
## bsodCode - Код ошибки, который вы хотите показать игроку. Если не дано, будет 
##            подставлено «DDLC_ESCAPE_PLAN_FAILED».
## bsodFile (только Windows 7) - Мимикрия имени файла, из-за которого 
##            возникла проблема. Если не дано, будет подставлено «libGLESv2.dll».
## rsod (только Windows 11) - Меняет Чёрный ЭС Windows 11 на Красный.
##
## Примеры:
## show screen bsod("DOKI_DOKI", "renpy32.dll", False) 
## show screen bsod("EILEEN_EXCEPTION_NOT_HANDLED", rsod=True)

init python:
    import subprocess
    import platform

    cursor = 0

    def fakePercent(st, at, winver):

        if int(0 + (st * 5)) < 100:
            percent = int(0 + (st * 5))
        else:
            percent = 100

        if winver == 8:
            d = Text("автоматически выполнена перезагрузка. (выполнено: " + str(percent) + "%)\n", style="bsod_win8_text", size=26)
        else:
            d = Text(str(percent) + "% завершено", style="bsod_win10_text", line_leading=25)

        if percent < 100:
            return d, renpy.random.randint(1, 3)
        else:
            return d, None

    def constantCursor(st, at):
        global cursor
        if cursor == 0:
            cursor = 1
            return Text("  _", style="bsod_linux_text"), 0.3
        else:
            cursor = 0
            return Text("   ", style="bsod_linux_text"), 0.3

    if renpy.windows:
        try: osVer = tuple(map(int, subprocess.check_output("powershell (Get-WmiObject -class Win32_OperatingSystem).Version", shell=True).split("."))) # Vista+
        except: osVer = tuple(map(int, platform.version().split("."))) or (5, 1, 2600) # XP возвращает JIC (хотя кто пользуется XP в наши дни?)

screen bsod(bsodCode="DDLC_ESCAPE_PLAN_FAILED", bsodFile="libGLESv2.dll", rsod=False):

    layer "master"

    if renpy.windows:

        if osVer < (6, 2, 9200): # Windows 7

            add Solid("#000082")

            vbox:

                style_prefix "bsod_win7"

                text "Вследствие возникшей проблемы система Windows принудительно завершила работу для предотвращения урона компьютеру."
                text "Проблема была вызвана следующим файлом: " + bsodFile.upper()
                text bsodCode.upper()
                text "Если вы впервые видите этот Синий экран останова, перезагрузите компьютер. Если этот экран появился снова, следуйте нижеприведённым шагам:"
                text "Убедитесь, что новое оборудование или ПО установлено корректно. Если оборудование/ПО было установлено впервые, попросите у производителя оборудования/ПО обновления Windows, которые могут вам понадобиться."
                text "Если проблема не была устранена, отключите или удалите любое только что установленное оборудование или ПО. Отключите такие параметры памяти BIOS, как кэширование и теневое копирование. Если для удаления/отключения компонентов вам необходимо воспользоваться Безопасным режимом, перезагрузите компьютер, нажмите F8 для входа в Дополнительные параметры загрузки, а затем выберите Безопасный режим."
                text "Техническая информация:"
                text "*** STOP: 0x00000051 (OXFD69420, 0x00000005, OXFBF92317" + ", 0x00000000)\n"
                text "*** " + bsodFile.upper() + "  -  Address FBF92317 base at FBF102721, Datestamp 3d6dd67c"

        elif osVer < (10, 0, 10240): # Windows 8/8.1

            add Solid("#1273aa")

            style_prefix "bsod_win8"

            vbox:

                xalign 0.5
                yalign 0.4

                text ":(" style "bsod_win8_sad_text"
                text "На вашем ПК возникла проблема, и его необходимо перезагрузить."
                text "Мы лишь собираем некоторые сведения об ошибке, а затем будет"
                add DynamicDisplayable(fakePercent, 8)
                text "При желании вы можете найти в Интернете информацию по этому коду ошибки: " + bsodCode.upper() style "bsod_win8_sub_text"

        else: # Windows 10 (вплоть до 21H1)/Windows 11/Windows 11 (вариант с КЭС)

            if osVer < (10, 0, 22000):

                add Solid("#0078d7")

            else:

                if not rsod:

                    add Solid("#000000")
                    python:
                        blackCol = "#0078d7"

                else:

                    add Solid("#d40e0eff")
                    python:
                        blackCol = "#f00"

            style_prefix "bsod_win10"

            vbox:

                xalign 0.3
                yalign 0.3

                text ":(" style "bsod_win10_sad_text"

                if osVer < (10, 0, 22000):

                    text "На вашем ПК возникла проблема, и его необходимо перезагрузить."
                    text "Мы лишь собираем некоторые сведения об ошибке, а затем будет"
                    text "автоматически выполнена перезагрузка."

                else:

                    text "На вашем устройстве возникла проблема, и его необходимо перезагрузить."
                    text "Мы лишь собираем некоторые сведения об ошибке, а затем будет"
                    text "автоматически выполнена перезагрузка."

                add DynamicDisplayable(fakePercent, 10)

                hbox:

                    if osVer < (10, 0, 22000):

                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/mod_extra_images/bsod_qr_code.png", im.matrix.colorize("#0078d7", "#fff"), ) at bsod_qrcode(100)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text "Дополнительные сведения об этой проблеме и возможных способах её решения см. на странице https://www.windows.com/stopcode" style "bsod_win10_info_text" line_leading 25
                            text "При обращении в службу поддержки предоставьте следующие данные:" style "bsod_win10_sub_text" line_leading 25
                            text "Код остановки: " + bsodCode.upper() style "bsod_win10_sub_text"

                    else:

                        vbox:
                            text "" line_leading -3
                            add im.MatrixColor("mod_assets/mod_extra_images/bsod_qr_code.png", im.matrix.colorize(blackCol, "#fff"), ) at bsod_qrcode(150)
                        vbox:
                            xpos 0.03
                            spacing 4
                            text "Дополнительные сведения об этой проблеме и возможных способах её решения см. на странице" style "bsod_win10_info_text" line_leading 25
                            text "https://www.windows.com/stopcode\n" style "bsod_win10_info_text"
                            text "При обращении в службу поддержки предоставьте следующие данные:" style "bsod_win10_sub_text"
                            text "Код остановки: " + bsodCode.upper() style "bsod_win10_sub_text"

    elif renpy.macintosh:

        add Solid("#222")

        add im.MatrixColor("mod_assets/DDLCModTemplateLogo.png", im.matrix.desaturate() * im.matrix.brightness(-0.36)) at bsod_qrcode(440) xalign 0.5 yalign 0.54
        vbox:

            style_prefix "bsod_mac"
            xalign 0.53
            yalign 0.51

            text "Вам необходимо перезагрузить компьютер. Удерживайте\n"
            text "кнопку Питания, пока он не выключится, затем нажмите эту же\n"
            text "кнопку снова." line_spacing 25
            text "Redémarrez l'ordinateur. Enfoncez le bouton de démarrage\n"
            text "jusqu'à l'extinction, puis appuyez dessus une nouvelle fois." line_spacing 25
            text "Debe reiniciar el o rdenador. Mantenga pulsado el botón de\n"
            text "arranque hasta que se apague y luego vuelva a pulsarlo." line_spacing 25
            text "Sie müssen den Computer neu starten. Halten Sie den\n"
            text "Ein-/Ausschalter gedrückt bis das Gerät ausgeschaltet ist\n"
            text "und drücken Sie ihn dann erneut." line_spacing 25
            text "コンピュータの再起動が必要です。電源が切れるまでパワーボタンを\n"
            text "押し続けてから、もう一度パワーボタンを押します。"
            # text "Devi riavviare il computer. Tieni premuto il pulsante di\n"
            # text "accensione finché non si spegne, quindi premi di nuovo il\n"
            # text "pulsante di accensione."

    else:

        add Solid("#000")

        vbox:
            style_prefix "bsod_linux"

            text "metaverse-pci.c:v[config.version] 9/22/2017 Metaverse Enterprise Solutions\n"
            text "  https://www.metaverse-enterprise.com/network/metaverse-pci.html"
            text "hda0: METAVERSE ENTERPRISE VIRTUAL HARDDISK, ATA DISK drive"
            text "ide0 at 0x1f0 - 0x1f7, 0x3f6 on irq 14"
            text "hdc: METAVERSE ENTERPRISE VIRTUAL CD-ROM, ATAPI CD/DVD-ROM drive"
            text "ide1 at 0x444 - 0x910, 0x211 on irq 15"
            text "fd0: METAVERSE ENTERPRISE VIRTUAL FLOPPY, ATA FLOPPY drive"
            text "ide2 at 0x7363-0x6e6565, 0x4569 on irq 16"
            text "ACPI: PCI Interrupt Link [[LNKC] ebabked at IRQ 10"
            text "ACPI: PCI Interrupt 0000:00:03:.0[[A] -> Link [[LNKC] -> GSI 10 (level, low) -> IRQ 10"
            text "eno1: Metaverse Enterprise LIB-0922 found at 0xc453, IRQ 10, 09:10:21:86:75:30"
            text "hda: max request size: 512KiB"
            text "hda: 2147483648 sectors (1 TB) w/256KiB Cache, CHS=178/255/63, (U)DMA"
            text "hda: hda1"
            text "hdc: ATAPI 4x CD-ROM drive, 512kB Cache, (U)DMA"
            text "Uniform CD-ROM driver Revision: 3.20"
            text "Готово."
            text "Запуск: DDLC.so"
            text "Готово."
            text "DDLC.so[[3352]: Импортирование _renpysteam: ImportError('Нет модуля под именем _renpysteam',)"
            text "DDLC.so[[3352]: nvdrs: Загружен, идёт отключение оптимизации потоков."
            text "DDLC.so[[3352]: nvdrs: Оптимизации потоков отключены."
            text "DDLC.so: УСПЕШНО."
            text "Готово."
            text "Запуск: DDLC.so -> linux-4.12.14"
            text "/init: /init: 151: " + bsodCode.upper() + ": 0xforce=panic"
            text "Паника ядра - невозможность синхронизации: Попытка убить инициализацию!"
            add DynamicDisplayable(constantCursor)

    add Solid("#000000") at bsod_transition

style bsod_win7_text is gui_text
style bsod_win7_text:
    font "C:/Windows/Fonts/lucon.ttf"
    antialias False
    size 13
    line_leading 15
    line_spacing -14
    xsize 1279
    outlines []

style bsod_win8_text is gui_text
style bsod_win8_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 25
    line_spacing 5
    xsize 600
    outlines []

style bsod_win8_sad_text is gui_text
style bsod_win8_sad_text is bsod_win8_text:
    size 128
    xpos -8

style bsod_win8_sub_text is gui_text
style bsod_win8_sub_text is bsod_win8_text:
    size 11

style bsod_win10_text is bsod_win8_text
style bsod_win10_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 24
    line_leading 3
    line_spacing 0
    xsize 800
    outlines []

style bsod_win10_info_text is bsod_win10_text
style bsod_win10_info_text:
    size 16

style bsod_win10_sad_text is bsod_win10_text
style bsod_win10_sad_text:
    size 136
    xpos -8

style bsod_win10_sub_text is bsod_win10_text
style bsod_win10_sub_text:
    size 11

style bsod_mac_text is gui_text
style bsod_mac_text:
    font "gui/font/SourceHanSansJP.otf"
    size 28
    outlines []
    line_spacing -30

style bsod_linux_text is gui_text
style bsod_linux_text:
    font "gui/font/consola.ttf"
    size 15
    outlines []
    line_leading 5

transform bsod_transition:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

transform bsod_qrcode(x):
    size(x,x)