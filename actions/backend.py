
from streamcontroller_plugin_tools import BackendBase
from pathlib import Path


class Backend(BackendBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


backend = Backend()
