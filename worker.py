from PySide6.QtCore import QRunnable, Slot

class Worker(QRunnable):
    """Worker thread.

    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run code
    """

    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        """Initialise the runner function with passed args, kwargs."""
        print("Thread start")
        print(self.args, self.kwargs)
        self.fn(*self.args, **self.kwargs)
