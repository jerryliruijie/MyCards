# Progress

## 截止到 2026-03-08 的进展

### 已完成（基础与可用版本）
- 完成 monorepo 基础结构：`apps/api`、`apps/web`、`docs`、`infra`
- 完成核心文档：产品规格、数据模型、路线图、技术决策、线框方案
- 完成 FastAPI 分层架构：`models / repositories / services / routes / integrations`
- 完成核心实体与初始迁移（Alembic）
- 完成核心 API：
  - cards CRUD
  - card images
  - purchase lots
  - storage positions / assignments
  - price snapshots / manual snapshots
  - tags
  - portfolio summary
- 完成价格适配器边界与 mock provider
- 完成种子数据
- 完成 Next.js 前端脚手架与中文化
- 完成核心卡片信息流程（标题、图片、买入价、市场价）
- 默认价格币种调整为人民币：`CNY`（前端展示为 `RMB/¥`）
- 完成本地图片真实上传（开发环境）：
  - 上传接口：`POST /api/v1/cards/{card_id}/images/upload`
  - 本地落盘：`apps/api/storage`
  - 静态访问：`/media/*`
- 完成一键启动脚本与无 Docker 预览模式
- 完成 GitHub Actions 基础 CI 并修复多轮配置问题

### 当前状态
- 项目已从“纯脚手架”进入“可录入、可查看、可维护”的可用阶段
- 前端仍以线框/实用优先为主，尚未进行精细交互与视觉打磨

## 下一步任务（按优先级）
1. 图片管理增强：多图管理、主图切换、删除与排序
2. 卡片列表增强：筛选、排序、分页（按价格、盈亏、更新时间）
3. 详情页增强：价格历史时间线与手动改价记录
4. 存储管理增强：树结构交互、拖拽/移动分配
5. 定价能力增强：引入第一个真实 provider（保留手动价优先/兜底）
6. 数据运营能力：CSV 导入导出、备份恢复脚本
