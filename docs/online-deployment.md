# 在线部署方案（无需本地安装 Node/Docker）

## 结论
- 你本地不装 Docker 也能开发（脚本已支持 SQLite 预览模式）。
- 你本地不装 Node 就不能在本机跑前端。
- 如果你只想在线看效果，可以走托管部署：`Vercel(前端) + Render(后端) + Supabase/Neon(PostgreSQL)`。

## 方案 A（推荐，最省事）

### 1) 数据库：Supabase 或 Neon
- 新建 PostgreSQL 实例
- 记下连接串（`postgresql+psycopg://...`）

### 2) 后端：Render
- New Web Service -> 连接 GitHub 仓库
- Root Directory: `apps/api`
- Build Command:
```bash
pip install -e .[dev]
```
- Start Command:
```bash
alembic upgrade head && python -m app.db.seed && uvicorn app.main:app --host 0.0.0.0 --port $PORT
```
- 环境变量：
  - `DATABASE_URL`=你的 PostgreSQL URL
  - `STORAGE_DIR`=`./storage`

### 3) 前端：Vercel
- Import GitHub Project
- Root Directory: `apps/web`
- 环境变量：
  - `NEXT_PUBLIC_API_BASE_URL`=`https://<你的-render-域名>/api/v1`
- Deploy

## 方案 B（单机长期自托管）
- 安装 Docker Desktop
- 用 `infra/docker-compose.yml` 管数据库
- 双击 `Start-MyCards.bat` 本地启动

## 注意
- 在线部署推荐 PostgreSQL，不要用 SQLite。
- 当前 `python -m app.db.seed` 是开发示例数据，生产可按需关闭或改成幂等初始化。
