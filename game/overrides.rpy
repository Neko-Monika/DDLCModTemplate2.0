python early:
    from renpy import config, loadsave
    import renpy.savelocation as savelocation
    import threading

    def savelocation_init_override():
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
