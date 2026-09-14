from PySide6.QtCore import Qt

class WindowManager():
    @staticmethod
    def open_or_focus_window(parent_window, window_name, window_class, action):
        window = getattr(parent_window, window_name, None)
        print(window)
        if window is None:
            action.setChecked(True)
            window = window_class(parent=parent_window)
            window.setAttribute(Qt.WA_DeleteOnClose)
            window.destroyed.connect(lambda: WindowManager.on_window_closed(parent_window,window_name, action))
            window.show()
            setattr(parent_window, window_name, window)
        else:
            window.raise_()
            window.activateWindow()

    @staticmethod
    def on_window_closed(parent_window, window_name, action):
        setattr(parent_window, window_name, None)
        action.setChecked(False)