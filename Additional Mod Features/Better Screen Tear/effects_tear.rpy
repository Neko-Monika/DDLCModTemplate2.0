init 10 python:
    import io

    class TearDisplayable(object):
        """
        Для использования в качестве трансформации.
        ```
        show sayori turned at TearDisplayable()
        ```

        `number`: int
            Количество фрагментов.

        `offsetRange`: tuple[int | float, int | float]
            Минимум и максимум смещения.

        `chroma`: bool
            Применять хроматическую аберрацию к фрагментам?

        `key`: Any | None
            Если не `None`, все объекты `TearDisplayable`, которые имеют этот ключ, будут использовать тот же эффект разрыва (`tear`).

        `render_child`: bool
            Если истинно, дочерние объекты будут обрабатываться под фрагментами.
        """
        def __init__(self, number=10, offtimeMult=1, ontimeMult=1, offsetRange=(0, 50), chroma=False, key=None, render_child=True):
            self.number = number
            self.offtimeMult = offtimeMult
            self.ontimeMult = ontimeMult
            self.offsetRange = offsetRange
            self.chroma = chroma
            self.key = key
            self.render_child = render_child

        def __call__(self, child):
            rv = _TearDisplayable(child, self.number, self.offtimeMult, self.ontimeMult, self.offsetRange, self.chroma, self.render_child)
            if self.key is not None: rv.tear = _TearCore._cache.setdefault(self.key, rv.tear)
            return rv

    class TearSurface(_BaseTear):
        """
        `srf`: Render | Surface | GL2Model | None
            Используемая поверхность. Если передано `None`, делает снимок экрана и использует его как поверхность
            (размер скриншота не будет аналогичным размеру экрана, будьте с этим осторожны).
        """
        def __init__(self, number=10, offtimeMult=1, ontimeMult=1, offsetRange=(0, 50), chroma=False, render_child=True, srf=None):
            super(TearSurface, self).__init__(number, offtimeMult, ontimeMult, offsetRange, chroma, render_child)
            srf = srf or screenshot_srf()

            with io.BytesIO() as sio:
                renpy.display.module.save_png(srf, sio, 0)
                self.data = sio.getvalue()

        def render(self, w, h, st, at):
            return self._srf_render(renpy.display.pgrender.load_image(io.BytesIO(self.data), "TearSurface.png"), w, h, st, at)

    def Tear(number=10, offtimeMult=1, ontimeMult=1, offsetMin=0, offsetMax=50, srf=None, chroma=False):
        return TearSurface(number, offtimeMult, ontimeMult, (offsetMin, offsetMax), chroma, srf)

    class GlicthedDisplayable(object):
        """
        Принимает определённое число кортежей, в которых должно быть 8 элементов; последние являются следующим:

        `center`: tuple[position, position]
            Центр созданного из фрагментов прямоугольника.

        `cols`: int
            Количество фрагментов по горизонтали.

        `rows`: int
            Количество рядов в каждом столбце (`cols`).

        `size`: tuple[position | position]
            Размер фрагментов (относительно коробки).

        `box`: tuple[position | position | position | position]
            Фрагменты будут взяты из субповерхности, созданной путём обрезки поверхности до коробки (`box`).
            Работает так же, как и свойство трансформации `crop`.

        `offtimeMult`: int | float
            Аналогично `TearDisplayable`.

        `ontimeMult`: int | float
            Аналогично `TearDisplayable`.

        `d`: renpy.Displayable | None
            Отображаемый объект, из которого будут браться фрагменты. Если `None`, будет использован дочерний элемент.

        Вместо конструктора можно также использовать метод `add_glitch`, если вам так проще.

        ```
        show sayori turned at GlicthedDisplayable(((0.5, 0.1), 7, 3, (40, 40), 1, 1), ((0.5, 0.7), 10, 1, (30, 50), 1, 1, "bg residential_day"))
        ```
        и
        ```
        show sayori turned at GlicthedDisplayable().add_glitch((0.5, 0.1), 7, 3, (40, 40), 1, 1).add_glitch(center=(0.5, 0.7), cols=10, rows=1, size=(30, 50), offtimeMult=1, ontimeMult=1, d="bg residential_day")
        ```
        работают одинаково.
        """
        def __init__(self, *args):
            self.glitches = [ ]
            for glitch in args: self.add_glitch(*glitch)

        def add_glitch(self, center=(0.5, 0.5), cols=5, rows=5, size=(50, 50), box=(0.0, 0.0, 1.0, 1.0), offtimeMult=1, ontimeMult=1, d=None):
            self.glitches.append((center, max(cols, 1), max(rows, 1), size, box, offtimeMult, ontimeMult, d))
            return self

        def __call__(self, child):
            if not self.glitches: raise ValueError("Не дано: glitch")
            return _GlicthedDisplayable(child, *self.glitches)  

init python:
    @renpy.pure
    def position(x, size):
        """
        Поведение аналогично 7.4.9.
        Значение плавающего (`float`) типа означает относительное размещение: значение будет умножено на размер (`size`).
        """
        if type(x) is float: return x * size
        return x

    class _TearPiece(object):
        def __init__(self, startY, endY, offtimeMult, ontimeMult, range):
            self.y = max(0, startY)
            self.height = max(0, endY - startY)

            self.onTime  = random.uniform(0.0, 0.24) * ontimeMult
            self.offTime = random.uniform(0.0, 0.24) * offtimeMult

            self.xoffset = 0
            self.xoffsetMin, self.xoffsetMax = range

        def update(self, st):
            st %= self.offTime + self.onTime
            if st > self.offTime and self.xoffset == 0:
                self.xoffset = random.randint(self.xoffsetMin, self.xoffsetMax) * random.choice((1, -1))
            elif st <= self.offTime and self.xoffset != 0:
                self.xoffset = 0

    class _TearCore(object):
        _cache = { }

        def __init__(self, number, offtimeMult, ontimeMult, offsetRange, chroma, render_child):
            self.chroma = bool(chroma) and getattr(renpy.display.render, "models", False)

            tearpoints = [0.0, 1.0]
            for _ in range(number):
                tearpoints.append(random.random())
            tearpoints.sort()

            self.pieces = [
                _TearPiece(tearpoints[i], tearpoints[i + 1], offtimeMult, ontimeMult, offsetRange)
                for i in range(number + 1)
            ]
            self.render_child = render_child

        def render(self, srf, w, h, st, at):
            width, height = srf.get_size()
            render = renpy.Render(width, height)

            # Положение по вертикали (ypos) относительно объекта, где будут отображаться фрагменты
            # Из-за того, что Render.subsurface конвертирует значения в целочисленный тип (int), во время отображения могут появляться "дыры".
            # Чтобы исправить это, мы используем сумму высоты предыдущих субповерхностей (которые являются целыми числами) в качестве положения по вертикали.
            ypos = 0

            for piece in self.pieces:
                piece.update(st)

                subsrf = srf.subsurface((0, piece.y * height, width, piece.height * height))
                piece_width, piece_height = subsrf.get_size()

                if self.chroma:
                    piece_render = renpy.Render(piece_width, piece_height)

                    for color_mask in (
                        (False, False, True, True),
                        (False, True, False, True),
                        (True, False, False, True),
                    ):
                        mask_render = renpy.Render(piece_width, piece_height)
                        mask_render.blit(subsrf, (0, 0), main=False)
                        mask_render.add_property("gl_color_mask", color_mask)
                        xzoom = 1.0 + random.uniform(-piece.xoffset, piece.xoffset) / piece_width
                        mask_render.zoom(xzoom, 1.0)

                        piece_render.blit(mask_render, (0, 0), main=False)

                    subsrf = piece_render

                render.subpixel_blit(subsrf, (piece.xoffset, ypos), main=False)
                ypos += piece_height

            return render

    class _BaseTear(renpy.Displayable):
        def __init__(self, number, offtimeMult, ontimeMult, offsetRange, chroma, render_child):
            super(_BaseTear, self).__init__()
            self.tear = _TearCore(number, offtimeMult, ontimeMult, offsetRange, chroma, render_child)

        def _srf_render(self, srf, w, h, st, at):
            tr = self.tear.render(srf, w, h, st, at)
            renpy.redraw(self, 0)

            if self.tear.render_child:
                rv = renpy.Render(*srf.get_size())
                rv.blit(srf, (0, 0))
                rv.blit(tr, (0, 0), main=False)
                return rv

            return tr

    class _TearDisplayable(_BaseTear):
        def __init__(self, child, number, offtimeMult, ontimeMult, offsetRange, chroma, render_child):
            super(_TearDisplayable, self).__init__(number, offtimeMult, ontimeMult, offsetRange, chroma, render_child)
            self.child = renpy.displayable(child)

        def render(self, w, h, st, at):
            return self._srf_render(renpy.render(self.child, w, h, st, at), w, h, st, at)

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [self.child]

        def predict_one(self):
            renpy.display.predict.displayable(self.child)

    class _GlicthedDisplayablePiece(object):
        def __init__(self, col, row, offtimeMult, ontimeMult):
            self.col = col
            self.row = row

            self.onTime = random.uniform(0.0, 0.24) * ontimeMult
            self.offTime = random.uniform(0.0, 0.24) * offtimeMult

            self.pos = None

        def update(self, st):
            st %= self.offTime + self.onTime
            if st > self.offTime and self.pos is None:
                self.pos = (random.random(), random.random())
            elif st <= self.offTime and self.pos is not None:
                self.pos = None

    class _GlicthedDisplayableCore(object):
        def __init__(self, center, cols, rows, size, box, offtimeMult, ontimeMult, d):
            self.pieces = [
                _GlicthedDisplayablePiece(col, row, offtimeMult, ontimeMult)
                for col in range(cols)
                for row in range(rows)
            ]

            self.center = center
            self.cols = cols
            self.rows = rows
            self.size = size
            self.box = box
            self.d = renpy.easy.displayable_or_none(d)

        def render(self, srf, width, height, st, at):
            """
            `srf`: Render | Surface | GL2Model
                Поверхность, с которой будут срисовываться фрагменты.
            
            `width`: int | float
                Ширина дочернего рендера.
            
            `height`: int | float
                Высота дочернего рендера.
            """
            rv = renpy.Render(width, height)

            w, h = srf.get_size()
            box_x, box_y, box_w, box_h = self.box
            box_x = position(box_x, w)
            box_y = position(box_y, h)
            box_w = position(box_w, w)
            box_h = position(box_h, h)

            box = srf.subsurface((box_x, box_y, box_w, box_h))
            box_width, box_height = box.get_size()

            rect_xsize, rect_ysize = self.size
            rect_xsize = position(rect_xsize, box_width)
            rect_ysize = position(rect_ysize, box_height)

            xrange = box_width - rect_xsize
            yrange = box_height - rect_ysize

            if xrange < 0 or yrange < 0:
                raise ValueError(f"""\
Не удалось вырезать прямоугольник.
Площадь обрезки: ({xrange}, {yrange})
Прямоугольник: ({rect_xsize}, {rect_ysize})""")

            sw = self.cols * rect_xsize
            sh = self.rows * rect_ysize
            rect_render = renpy.Render(sw, sh)

            for piece in self.pieces:
                piece.update(st)

                if piece.pos is None: continue

                piece_x, piece_y = piece.pos
                rect = box.subsurface((piece_x * xrange, piece_y * yrange, rect_xsize, rect_ysize))
                rect_render.subpixel_blit(rect, (piece.col * rect_xsize, piece.row * rect_ysize), main=False)

            center_x, center_y = self.center
            center_x = position(center_x, width)
            center_y = position(center_y, height)

            rv.subpixel_blit(rect_render, (center_x - (sw / 2.0), center_y - (sh / 2.0)), main=False)
            return rv

    class _BaseGlicthedDisplayable(renpy.Displayable):
        def __init__(self, *args):
            super(_BaseGlicthedDisplayable, self).__init__()
            self.cores = [
                _GlicthedDisplayableCore(*glitch)
                for glitch in args
            ]

        def glitch_render(self, cr, w, h, st, at):
            rv = renpy.Render(w, h)
            cr_w, cr_h = cr.get_size()
            for core in self.cores:
                if core.d is not None:
                    rect = core.render(
                        renpy.render(core.d, w, h, st, at), cr_w, cr_h, st, at
                    )
                else:
                    rect = core.render(cr, cr_w, cr_h, st, at)
                rv.blit(rect, (0, 0), main=False)
            return rv

    class _GlicthedDisplayable(_BaseGlicthedDisplayable):
        def __init__(self, child, *args):
            super(_GlicthedDisplayable, self).__init__(*args)
            self.child = renpy.displayable(child)

        def render(self, w, h, st, at):
            rv = renpy.render(self.child, w, h, st, at)
            glitch = self.glitch_render(rv, w, h, st, at)
            rv.blit(glitch, (0, 0), main=False)
            renpy.redraw(self, 0.0)
            return rv

        def event(self, ev, x, y, st):
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [self.child]

        def predict_one(self):
            renpy.display.predict.displayable(self.child)
