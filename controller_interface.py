from typing import Protocol, Optional, List, Dict

class FileSelector(Protocol):
    """ Interface for selecting file path"""
    def select_file(self) -> Optional[str]: ...

class Storage(Protocol):
    """Interface for saving a file to a destination."""
    def save(self, src_path: str, dest_root: str = "archive") -> str: ...

class RecordStore(Protocol):
    """Interface for recording archive operations."""
    def append(self, src_path: str, dest_path: str) -> None: ...
    def read_tail(self, n: int = 20) -> List[Dict[str, str]]: ...