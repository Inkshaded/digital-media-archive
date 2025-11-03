from typing import Protocol, Optional

class FileSelector(Protocol):
    """ Interface for selecting file path"""
    def select_file(self) -> Optional[str]: ...

class Storage(Protocol):
    """Interface for saving a file to a destination."""
    def save(self, src_path: str, dest_root: str = "archive") -> str: ...