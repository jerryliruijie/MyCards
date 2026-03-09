"use client";

import { ChangeEvent, useMemo, useState } from "react";

import { api } from "@/lib/api-client";
import { resolveImageUrl } from "@/lib/media-url";
import { CardImage } from "@/types/api";

type Props = {
  cardId: string;
  initialImages: CardImage[];
};

export function CardImageManager({ cardId, initialImages }: Props) {
  const [images, setImages] = useState<CardImage[]>(
    [...initialImages].sort((a, b) => Number(b.is_primary) - Number(a.is_primary) || a.sort_order - b.sort_order),
  );
  const [busyId, setBusyId] = useState<string | null>(null);
  const [busyUpload, setBusyUpload] = useState(false);
  const [draggingId, setDraggingId] = useState<string | null>(null);
  const [dropTargetId, setDropTargetId] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const primary = useMemo(() => images.find((img) => img.is_primary) ?? images[0] ?? null, [images]);

  async function refreshImages() {
    const latest = await api.listCardImages(cardId);
    setImages(
      [...latest].sort(
        (a, b) => Number(b.is_primary) - Number(a.is_primary) || a.sort_order - b.sort_order,
      ),
    );
  }

  async function onUploadFiles(event: ChangeEvent<HTMLInputElement>) {
    const files = Array.from(event.target.files ?? []);
    if (!files.length) return;

    setBusyUpload(true);
    setError(null);

    try {
      let nextSortOrder = images.length;
      for (const file of files) {
        const isPrimary = images.length === 0 && nextSortOrder === 0;
        await api.uploadCardImage(cardId, file, { isPrimary, sortOrder: nextSortOrder });
        nextSortOrder += 1;
      }
      await refreshImages();
    } catch (err) {
      setError(err instanceof Error ? err.message : "上传失败");
    } finally {
      setBusyUpload(false);
      event.target.value = "";
    }
  }

  async function onSetPrimary(imageId: string) {
    setBusyId(imageId);
    setError(null);
    try {
      await api.setCardImagePrimary(imageId);
      await refreshImages();
    } catch (err) {
      setError(err instanceof Error ? err.message : "设置主图失败");
    } finally {
      setBusyId(null);
    }
  }

  async function onDelete(imageId: string) {
    setBusyId(imageId);
    setError(null);
    try {
      await api.deleteCardImage(imageId);
      await refreshImages();
    } catch (err) {
      setError(err instanceof Error ? err.message : "删除失败");
    } finally {
      setBusyId(null);
    }
  }

  async function onMove(imageId: string, direction: -1 | 1) {
    const sorted = [...images].sort((a, b) => a.sort_order - b.sort_order);
    const idx = sorted.findIndex((item) => item.id === imageId);
    const target = idx + direction;
    if (idx < 0 || target < 0 || target >= sorted.length) return;

    const next = [...sorted];
    [next[idx], next[target]] = [next[target], next[idx]];

    setBusyId(imageId);
    setError(null);
    try {
      await api.reorderCardImages(
        cardId,
        next.map((img) => img.id),
      );
      await refreshImages();
    } catch (err) {
      setError(err instanceof Error ? err.message : "排序失败");
    } finally {
      setBusyId(null);
    }
  }

  async function onDropReorder(targetImageId: string) {
    if (!draggingId || draggingId === targetImageId) {
      setDraggingId(null);
      setDropTargetId(null);
      return;
    }

    const sorted = [...images].sort((a, b) => a.sort_order - b.sort_order);
    const dragIndex = sorted.findIndex((item) => item.id === draggingId);
    const dropIndex = sorted.findIndex((item) => item.id === targetImageId);
    if (dragIndex < 0 || dropIndex < 0) {
      setDraggingId(null);
      setDropTargetId(null);
      return;
    }

    const next = [...sorted];
    const [draggingItem] = next.splice(dragIndex, 1);
    next.splice(dropIndex, 0, draggingItem);

    setBusyId(draggingId);
    setError(null);
    try {
      await api.reorderCardImages(
        cardId,
        next.map((img) => img.id),
      );
      await refreshImages();
    } catch (err) {
      setError(err instanceof Error ? err.message : "拖拽排序失败");
    } finally {
      setBusyId(null);
      setDraggingId(null);
      setDropTargetId(null);
    }
  }

  return (
    <section className="panel space-y-3">
      <div className="flex items-center justify-between gap-3">
        <h3 className="font-semibold">图片管理</h3>
        <label className="rounded bg-slate-800 px-3 py-2 text-sm text-white hover:bg-slate-700">
          {busyUpload ? "上传中..." : "上传图片"}
          <input
            type="file"
            accept="image/*"
            multiple
            className="hidden"
            onChange={onUploadFiles}
            disabled={busyUpload}
          />
        </label>
      </div>

      <div className="text-xs text-slate-500">支持拖拽排序，或使用“上移/下移”按钮微调。</div>

      <div className="grid gap-3 md:grid-cols-[220px_1fr]">
        <div className="h-56 rounded border bg-white p-2">
          {primary ? (
            <img
              src={resolveImageUrl(primary.storage_key) ?? ""}
              alt="主图"
              className="h-full w-full rounded object-cover"
            />
          ) : (
            <div className="flex h-full items-center justify-center text-sm text-slate-500">暂无图片</div>
          )}
        </div>

        <div className="grid grid-cols-2 gap-2 md:grid-cols-3">
          {images.map((image) => {
            const preview = resolveImageUrl(image.storage_key);
            return (
              <div
                key={image.id}
                className={`rounded border bg-white p-2 transition ${
                  dropTargetId === image.id ? "ring-2 ring-blue-300" : ""
                }`}
                draggable={busyId === null}
                onDragStart={() => setDraggingId(image.id)}
                onDragEnd={() => {
                  setDraggingId(null);
                  setDropTargetId(null);
                }}
                onDragOver={(e) => {
                  e.preventDefault();
                  if (draggingId && draggingId !== image.id) {
                    setDropTargetId(image.id);
                  }
                }}
                onDrop={(e) => {
                  e.preventDefault();
                  void onDropReorder(image.id);
                }}
              >
                <div className="mb-2 h-28 rounded bg-slate-100">
                  {preview ? (
                    <img src={preview} alt="卡图" className="h-full w-full rounded object-cover" />
                  ) : (
                    <div className="flex h-full items-center justify-center text-xs text-slate-500">无预览</div>
                  )}
                </div>
                <div className="mb-2 text-xs text-slate-500">{image.is_primary ? "主图" : "可拖拽"}</div>
                <div className="flex flex-wrap gap-1">
                  <button
                    type="button"
                    className="rounded border px-2 py-1 text-xs"
                    onClick={() => onSetPrimary(image.id)}
                    disabled={busyId === image.id || image.is_primary}
                  >
                    {image.is_primary ? "主图" : "设主图"}
                  </button>
                  <button
                    type="button"
                    className="rounded border px-2 py-1 text-xs"
                    onClick={() => onMove(image.id, -1)}
                    disabled={busyId === image.id}
                  >
                    上移
                  </button>
                  <button
                    type="button"
                    className="rounded border px-2 py-1 text-xs"
                    onClick={() => onMove(image.id, 1)}
                    disabled={busyId === image.id}
                  >
                    下移
                  </button>
                  <button
                    type="button"
                    className="rounded border px-2 py-1 text-xs text-red-700"
                    onClick={() => onDelete(image.id)}
                    disabled={busyId === image.id}
                  >
                    删除
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {error && <div className="text-sm text-red-700">{error}</div>}
    </section>
  );
}