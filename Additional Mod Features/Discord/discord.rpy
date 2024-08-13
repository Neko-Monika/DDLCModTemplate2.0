# discord.rpy
# Этот файл настраивает Игровую активность Discord под вашу модификацию.
# Для работы обязательно наличие библиотеки pypresence (идёт в комплекте с этим шаблоном).

## ПРОЧИТАЙТЕ НИЖЕПРИВЕДЁННЫЙ ТЕКСТ ПЕРЕД ТЕМ, КАК НАЧАТЬ РАБОТУ.
## Дабы Игровая активность работала, создайте новое приложение на Портале разработчиков Discord
## https://discord.com/developers/applications
## Следуйте комментариям внутри установок по умолчанию (`set_defaults`), чтобы настроить Игровую активность под себя.

## Работает аналогично коду Игровой активности от Lezalith: https://github.com/Lezalith/RenPy-Discord-Presence

default persistent.enable_discord = renpy.variant("pc")

init -950 python in discord:
    from pypresence import Presence, DiscordError, DiscordNotFound, InvalidPipe
    from store import config, NoRollback, persistent
    from copy import deepcopy
    import time

    class DiscordRPC(NoRollback):
        def __init__(self, client_id):
            self.client_id = str(client_id)
            self.start = time.time()
            self.rpc_connected = False

            self.set_defaults()
            self.original_props = self.self_dict()
            self.props = {}
            self.auth()
            self.connect()

        # Простой метод сбросить информацию в Игровой активности на значения по умолчанию.
        def set_defaults(self):
            # Детали, описывающие то, чем игрок сейчас занимается
            # Пример: В главном меню
            self.details = renpy.version()

            # Состояние, отражающее дополнительную информацию в деталях
            # Пример: Просматривает Настройки
            self.state = "Моника следит за тем, что ты пишешь в коде"

            # Определяет большое изображение, которое будет использоваться
            # в Игровой активности в качестве основной иконки.
            self.large_image  = "ddlcmodtemplatelogo"

            # Определяет текст, который будет отображаться при наведении указателя
            # на большую иконку в статусе игрока.
            # Пример: Мод-шаблон DDLC
            self.large_text  = "Воспоминания"  # Используется название модификации, определённое в игре.

            # Определяет маленькое изображение, которое будет использоваться
            # в Игровой активности в качестве дополнительной иконки.
            self.small_image = "test"

            # Определяет текст, который будет отображаться при наведении указателя
            # на маленькую иконку в статусе игрока.
            self.small_text = config.version  # Используется версия модификации.

        def self_dict(self):
            return {
                "state": self.state,
                "details": self.details,
                "large_image": self.large_image,
                "large_text": self.large_text,
                "small_image": self.small_image,
                "small_text": self.small_text,
                "start": self.start,
            }

        def reset_time(self):
            self.start = time.time()

        def auth(self):
            if not persistent.enable_discord: 
                self.rpc = None
                return

            try:
                self.rpc = Presence(self.client_id)
            except (DiscordError, DiscordNotFound):
                self.rpc = None

        def connect(self, reset=False):
            if self.rpc is None: self.auth()
            if self.rpc is None: return
            try:
                self.rpc.connect()
                self.rpc_connected = True
                if reset:
                    if len(self.props) <= 1: self.set(**self.original_props)
                    else: self.set(**self.props)
            except InvalidPipe:
                self.rpc = None

        def close(self):
            if self.rpc is None: return
            self.rpc.close()
            self.rpc_connected = False

        def reset(self):
            self.set(**self.original_props)

        def record_to_rollback(self):
            global rollback_status
            rollback_status = deepcopy(self.props)

        def rollback_check(self):
            global rollback_status

            if self.rpc is None: return
            if self.props != rollback_status:
                self.set(**rollback_status)

        def on_load(self):
            global rollback_status
            self.set(**rollback_status)

        def set(self, **props):
            if self.rpc is None: return
            self.props = deepcopy(props)
            self.props["start"] = self.start

            self.rpc.update(**self.props)
            self.record_to_rollback()

        def update(self, **props):
            if self.rpc is None: return
            for p in props:
                self.props[p] = props[p]
            self.props["start"] = self.start

            self.rpc.update(**self.props)
            self.record_to_rollback()

        def clear(self):
            self.props = {}
            self.record_to_rollback()
            self.rpc.clear()

default discord.rollback_status = {}

init -940 python:
    # Вставьте токен своей Игровой активности Discord внутрь двойных кавычек
    RPC = discord.DiscordRPC("979471077187125248")

    config.quit_callbacks.append(RPC.close)
    config.after_load_callbacks.append(RPC.on_load)
    config.interact_callbacks.append(RPC.rollback_check)
    config.start_callbacks.append(RPC.reset)
