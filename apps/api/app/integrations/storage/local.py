from pathlib import Path
from uuid import UUID

from fastapi import UploadFile


class StorageBackend:
    async def save_card_image(self, card_id: UUID, file: UploadFile) -> str:
        raise NotImplementedError


class LocalStorageBackend(StorageBackend):
    def __init__(self, root_dir: str) -> None:
        self.root_dir = Path(root_dir)
        self.root_dir.mkdir(parents=True, exist_ok=True)

    async def save_card_image(self, card_id: UUID, file: UploadFile) -> str:
        from uuid import uuid4

        suffix = Path(file.filename or "").suffix.lower()
        if not suffix:
            suffix = ".bin"

        rel_path = Path("cards") / str(card_id) / f"{uuid4().hex}{suffix}"
        abs_path = self.root_dir / rel_path
        abs_path.parent.mkdir(parents=True, exist_ok=True)

        data = await file.read()
        abs_path.write_bytes(data)

        return f"/media/{rel_path.as_posix()}"
