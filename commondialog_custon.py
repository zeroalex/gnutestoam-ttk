# base class for tk common dialogues
#
# this module provides a base class for accessing the common
# dialogues available in Tk 4.2 and newer.  use filedialog,
# colorchooser, and messagebox to access the individual
# dialogs.
#
# written by Fredrik Lundh, May 1997
#

__all__ = ["Dialog"]

from tkinter import Frame, Label


class Dialog:

    command = None

    def __init__(self, master=None, **options):
        if not master:
            master = options.get('parent')
        self.master = master
        self.options = options

    def _fixoptions(self):
        pass # hook

    def _fixresult(self, widget, result):
        return result # hook

    def show(self, **options):

        for k, v in options.items():
            self.options[k] = v

        self._fixoptions()

        master = self.master
        if master is None:
            master = _get_temp_root()
        try:
            self._test_callback(master)  # The function below is replaced for some tests.
            s = master.tk.call(self.command, *master._options(self.options))
            s = self._fixresult(master, s)
        finally:
            _destroy_temp_root(master)

        print(s)
        return s
