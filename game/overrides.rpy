## Данный файл предназначен для переопределения конкретных объявлений в DDLC
## Используйте его, если хотите изменить пару переменных, но не хотите
## переписывать файлы сценария, которые и так нормально работают.

## Обычные переопределения
## Эти переопределения срабатывают после всех обычных блоков инициализации в сценариях.
## Используйте их, чтобы изменить переменные в экранах, эффектах и прочем.
init 10 python:
    pass

## Ранние переопределения
## Эти переопределения срабатывают до обычных блоков инициализации в сценариях.
## Используйте их в тех редких случаях, когда надо изменить какую-то переменную
## прежде, чем она будет использована в другом блоке инициализации.
## Скорее всего, вам они не понадобятся.
init -10 python:
    pass

## Очень ранние переопределения
## Подобный блок вам понадобится для языка экрана, определённого разработчиком
## Не используйте их, если не уверены в том, что они вам нужны
python early:
    from renpy import config, loadsave
    import renpy.savelocation as savelocation
    import threading

    def savelocation_init_override():
        """
        Запускает **ЛИШЬ НЕКОТОРЫЕ** вещи, запускаемые savelocation.init

        В большинстве своём мы пытаемся сохранить каталог в AppData/эквивалентном
        каталоге ОС для упрощения процесса создания и восстановления резервных копий.

        Единственная разница заключается в том, что мы пропускаем каталог сохранений
        в папке игры (экстра-каталоги же было решено не пропускать, хотя для работы
        синхронизации прогресса они, скорее всего, не нужны - прим. пер.)
        """
        savelocation.quit()
        savelocation.quit_scan_thread = False

        location = savelocation.MultiLocation()
        location.add(savelocation.FileLocation(config.savedir))

        for i in config.extra_savedirs:
            location.add(savelocation.FileLocation(i))

        location.scan()

        loadsave.location = location

        savelocation.scan_thread = threading.Thread(target=savelocation.run_scan_thread)
        savelocation.scan_thread.start()

    savelocation.init = savelocation_init_override
