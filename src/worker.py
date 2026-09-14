from PySide6.QtCore import QRunnable, Slot
from multiprocessing import Process, Queue

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

class PWorker():
    def __init__(self, fn, *args, result_queue=None, **kwargs):
        #self.fn = fn
        #self.args = args
        #self.kwargs = kwargs
        self.result_queue = result_queue
        self.process = Process(target=self.target_wrapper,
                               args=(fn, args, kwargs, result_queue)
                               )
        print("Thread start")
        #print(args, kwargs)

    @staticmethod
    def target_wrapper(fn, args, kwargs, result_queue):
        try:
            result = fn(*args, **kwargs)
            print(type(result))
            if result_queue:
                result_queue.put(result)
        except Exception as e:
            result_queue.put(e)


    def start(self):
        self.process.start()


    def join(self):
        self.process.join()