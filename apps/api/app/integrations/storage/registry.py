from app.core.config import get_settings
from app.integrations.storage.local import LocalStorageBackend, StorageBackend


def get_storage_backend() -> StorageBackend:
    settings = get_settings()
    # TODO: 后续可在这里切换到 S3 兼容存储实现。
    return LocalStorageBackend(settings.storage_dir)
