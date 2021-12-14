import os
import threading
import types
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Iterator, Optional, Set, Tuple, Union

from django.apps.registry import Apps
from django.dispatch import Signal

_PathCompatible = Union[os.PathLike, str, bytes]

autoreload_started: Signal
file_changed: Signal
DJANGO_AUTORELOAD_ENV: str

def is_django_module(module: types.ModuleType): ...
def is_django_path(path): ...
def check_errors(fn): ...
def raise_last_exception() -> None: ...
def ensure_echo_on() -> None: ...
def iter_all_python_module_files() -> Set[Path]: ...
def iter_modules_and_files(
    modules: Iterable[types.ModuleType], extra_files: Iterable[_PathCompatible]
) -> Set[Path]: ...
def common_roots(paths: Iterable[_PathCompatible]) -> Iterator[Path]: ...
def sys_path_directories() -> Iterator[Path]: ...
def get_child_arguments(): ...
def trigger_reload(filename) -> None: ...
def restart_with_reloader() -> int: ...

class BaseReloader:
    extra_files: Set[Path]
    directory_globs: Dict[Path, Set[str]]
    def __init__(self) -> None: ...
    def watch_dir(self, path: _PathCompatible, glob: str) -> None: ...
    def watch_file(self, path: _PathCompatible) -> None: ...
    def watched_files(self, include_globs: bool = ...) -> Iterator[Path]: ...
    def wait_for_apps_ready(self, app_reg: Apps, django_main_thread: threading.Thread) -> bool: ...
    def run(self, django_main_thread: threading.Thread) -> None: ...
    def run_loop(self) -> None: ...
    def tick(self) -> Iterator[None]: ...
    @classmethod
    def check_availability(cls) -> bool: ...
    def notify_file_changed(self, path: _PathCompatible) -> None: ...
    @property
    def should_stop(self) -> bool: ...
    def stop(self) -> None: ...

class StatReloader(BaseReloader):
    SLEEP_TIME: int
    def tick(self) -> None: ...
    def snapshot_files(self) -> Iterator[Tuple[Path, int]]: ...
    @classmethod
    def check_availability(cls): ...

class WatchmanUnavailable(RuntimeError): ...

class WatchmanReloader(BaseReloader):
    roots: Any
    processed_request: Any
    client_timeout: Any
    def __init__(self) -> None: ...
    @property
    def client(self) -> Any: ...
    def watched_roots(self, watched_files: Iterable[Path]) -> Set[Path]: ...
    def update_watches(self) -> None: ...
    def request_processed(self, **kwargs: Any) -> None: ...
    def tick(self) -> None: ...
    def stop(self) -> None: ...
    def check_server_status(self, inner_ex: Optional[BaseException] = ...) -> bool: ...
    @classmethod
    def check_availability(cls) -> None: ...

def get_reloader() -> BaseReloader: ...
def start_django(reloader: BaseReloader, main_func: Callable, *args: Any, **kwargs: Any) -> None: ...
def run_with_reloader(main_func: Callable, *args: Any, **kwargs: Any) -> None: ...
