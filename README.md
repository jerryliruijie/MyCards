# MyCards

MyCards 是一个开源的个人收藏卡片资产库，聚焦于体育卡、TCG 卡及其他收藏卡。

项目定位：
- 个人优先
- 轻量易维护
- 快速迭代
- 便于自托管

## 技术栈

- 前端：Next.js + TypeScript + Tailwind CSS
- 后端：FastAPI + SQLModel
- 数据库：PostgreSQL
- 后台任务：轻量 Python Worker（后续可接调度器）
- 图片存储：开发阶段本地文件系统，后续可切换 S3 兼容存储

## 仓库结构

- `apps/api`：FastAPI 后端
- `apps/web`：Next.js 前端
- `docs`：产品与架构文档
- `.github/workflows`：CI 流水线
- `infra`：本地基础设施配置

## 架构说明

后端采用分层结构：
- `models`：领域模型与关系约束
- `repositories`：数据访问逻辑
- `services`：领域服务与业务编排
- `api/routes`：HTTP 路由层
- `integrations/pricing`：价格提供方适配器接口与实现

核心设计决策：
- `Card` 是收藏对象本体，不绑定单一购买记录或单一价格来源
- 价格快照 `PriceSnapshot` 采用追加写入，不覆盖历史
- `StoragePosition` 支持层级结构
- `ManualValuation` 为一等公民，支持手工估值

## 本地开发快速开始

### 1. 环境准备

- Python 3.12+
- Node.js 20+
- PostgreSQL 15+

### 2. 启动后端

```bash
cd apps/api
python -m venv .venv
. .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -e .[dev]
copy .env.example .env
alembic upgrade head
python -m app.db.seed
uvicorn app.main:app --reload --port 8000
```

### 3. 启动前端

```bash
cd apps/web
npm install
copy .env.example .env.local
npm run dev
```

访问地址：
- 前端：`http://localhost:3000`
- 后端文档：`http://localhost:8000/docs`

## 环境变量

### API（`apps/api/.env`）

- `DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/mycards`
- `STORAGE_DIR=./storage`

### Web（`apps/web/.env.local`）

- `NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api/v1`

## 当前里程碑

- [x] 产品文档 + 数据模型 + 路线图
- [x] 领域模型与迁移脚手架
- [x] 核心库存流程 API 脚手架
- [x] 定价提供方接口 + Mock 实现
- [x] Next.js 前端脚手架 + 强类型 API Client
- [x] UI 线框方案（先评审再做精细化 UI）

## 明确不做（v1）

- 市场交易平台
- 拍卖系统
- 社交功能
- 重型企业级认证与多租户复杂度

## 未来扩展方向

- 当前已保留最小 `User` 模型，为未来多用户迁移做准备
- 定价能力全部经适配器层接入，后续可平滑增加真实价格源
- 认证在 v1 非强制，代码中保留了明确 TODO 标记
