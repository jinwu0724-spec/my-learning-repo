# 学习路线梳理及日志记录（完整版）

> **更新时间**：2026.7.12  
> **目标**：从零基础到全栈 + AI 实战，周期约 4-6 个月（每天 2-4 小时）  
> **核心原则**：工具提效 → 语言打底 → 前端入门 → 后端 + 数据库 → 项目部署 → AI 深度整合  
> **AI 先行**：Claude Code / Codex / Trae / Hermes Agent 从第 1 天就用，写代码、查错、解释概念效率翻倍！

---

## 0. 路线总览

```
阶段 0                阶段 1                阶段 2                阶段 3                阶段 4                阶段 5
环境 + 工具 ──────► 编程语言基础 ──────► 前端开发 ──────► 后端 + 数据库 ──────► 项目实战 + 部署 ──────► AI 深度整合
 (1 周)              (2-3 周)             (3-4 周)           (4-5 周)             (3-4 周)             (持续 1-2 月)
    │                   │                    │                   │                    │                    │
    ▼                   ▼                    ▼                   ▼                    ▼                    ▼
 Git/GitHub          Python 核心          HTML/CSS/JS         FastAPI              Docker Compose       高级 AI 用法
 VS Code/Trae        JavaScript 基础      Vue3 或 React       SQL + PostgreSQL     Nginx + HTTPS        CI/CD
 Docker 初体验        AI 编程工作流         响应式 + 部署         Redis + ORM          个人网站上线           个人品牌建设
```

### 技术栈总览

| 方向 | 必修（⭐） | 选修（了解即可） |
|------|-----------|----------------|
| **AI / 智能开发** | Claude Code、Codex、Trae | Hermes Agent 进阶 |
| **前端** | HTML/CSS/JS、**Vue 3 或 React（二选一深入）** | 另一个框架快速过 |
| **后端** | **Python + FastAPI** | Node.js、Java（后期） |
| **数据库** | SQL、**PostgreSQL**（或 MySQL） | Redis（缓存） |
| **DevOps** | Git + GitHub、Docker、Linux 基础命令 | K8s、Prometheus |
| **部署** | GitHub Pages / Vercel（前端）、Docker Compose（后端） | 云服务器、CI/CD |

### 学习资源优先级

| 优先级 | 资源 | 用途 |
|--------|------|------|
| 🥇 | [菜鸟教程](https://www.runoob.com/) | 快速查阅、入门 |
| 🥈 | 官方文档（Vue / React / FastAPI / Docker） | 权威参考 |
| 🥉 | B站免费课（黑马 / 尚硅谷 / 鱼皮） | 系统跟学 |
| 辅助 | AI 工具生成个性化教程 | 按需定制 |

---

## 1. 阶段详解

---

### 阶段 0：环境搭建 + 工具入门

| 项目 | 内容 |
|------|------|
| **周期** | 第 1 周（3-7 天） |
| **目标** | 开发环境跑通，用 AI 写出第一行代码 |
| **前置条件** | 无（零基础起步） |

#### 学习清单

| # | 内容 | 必修/选修 | 建议用时 | 资源 |
|---|------|----------|---------|------|
| 1 | 安装 VS Code 或 Trae（推荐 Trae，中文友好 + AI 原生） | ⭐ 必修 | 0.5 天 | [Trae 官网](https://www.trae.ai/) |
| 2 | 注册 GitHub，安装 Git | ⭐ 必修 | 0.5 天 | [Git 菜鸟教程](https://www.runoob.com/git/git-tutorial.html) |
| 3 | Git 基础命令：`clone` `add` `commit` `push` `pull` `branch` | ⭐ 必修 | 1 天 | 同上 |
| 4 | 安装 Python 3.11+ | ⭐ 必修 | 0.5 天 | [python.org](https://www.python.org/downloads/) |
| 5 | 安装 Node.js LTS | ⭐ 必修 | 0.5 天 | [nodejs.org](https://nodejs.org/) |
| 6 | 安装 Docker Desktop | ⭐ 必修 | 0.5 天 | [Docker 官网](https://www.docker.com/products/docker-desktop/) |
| 7 | AI 工具初体验：用自然语言让它写 "Hello World" + 解释代码 | ⭐ 必修 | 1 天 | Claude Code / Codex / Trae 内置 AI |
| 8 | 浏览器开发者工具（F12）：Console、Elements、Network 面板 | ⭐ 必修 | 0.5 天 | [Chrome DevTools](https://developer.chrome.com/docs/devtools/) |

#### 可验证目标

- [x] 用 Git 推送一个仓库到 GitHub（含 README.md）
- [x] 在 VS Code / Trae 中用 AI 写一个 Python 脚本并成功运行
- [x] 用 Docker 成功运行 `docker run hello-world`
- [x] 创建 `my-learning-repo`，README 写清本学习计划链接

#### ⚠️ 常见坑

- Docker Desktop 在 Windows 需要开启 Hyper-V 或 WSL2
- Git 安装后务必配置 `user.name` 和 `user.email`
- Node.js 选 LTS 版本，不要选最新版

---

### 阶段 1：编程语言基础 + AI 编程习惯

| 项目 | 内容 |
|------|------|
| **周期** | 第 2-4 周（2-3 周） |
| **目标** | 掌握 Python 主力语言，形成「AI 辅助编程」工作流 |
| **前置条件** | 阶段 0 完成 |

> **主力语言选 Python**：语法简单、AI 生态强、后端/脚本都适用。JavaScript 只学基础语法，为前端阶段做准备。

#### 学习清单

| # | 内容 | 必修/选修 | 建议用时 | 资源 |
|---|------|----------|---------|------|
| **第 1 周：Python 核心语法** |
| 1 | Python 变量、数据类型、运算符 | ⭐ 必修 | 1 天 | [Python3 菜鸟教程](https://www.runoob.com/python3/python3-tutorial.html) |
| 2 | 条件判断（if/elif/else）、循环（for/while） | ⭐ 必修 | 1 天 | 同上 |
| 3 | 函数定义、参数、返回值、lambda | ⭐ 必修 | 1 天 | 同上 |
| 4 | 列表、元组、字典、集合 | ⭐ 必修 | 1 天 | 同上 |
| 5 | 字符串操作、文件读写 | ⭐ 必修 | 0.5 天 | 同上 |
| **第 2 周：Python 进阶 + JS 基础** |
| 6 | 面向对象：类、继承、多态 | ⭐ 必修 | 1 天 | 同上 |
| 7 | 异常处理（try/except/finally） | ⭐ 必修 | 0.5 天 | 同上 |
| 8 | 模块与包、虚拟环境（venv）、pip | ⭐ 必修 | 0.5 天 | 同上 |
| 9 | 常用库实战：`requests`（HTTP）、`json`、`os`、`sys` | ⭐ 必修 | 1 天 | [requests 文档](https://docs.python-requests.org/) |
| 10 | JavaScript 基础：变量、函数、DOM 操作、async/await | ⭐ 必修 | 2 天 | [JS 菜鸟教程](https://www.runoob.com/js/js-tutorial.html) |
| **第 3 周：AI 工具深度使用 + 项目实战** |
| 11 | AI 工具深度：写完整小程序、重构代码、生成测试 | ⭐ 必修 | 1 天 | Claude Code / Codex 实操 |
| 12 | 提示词工程基础：如何写好 prompt | ⭐ 必修 | 0.5 天 | [Prompt Engineering Guide](https://www.promptingguide.ai/zh) |
| 13 | Linux 命令进阶：文件操作（ls/cp/mv/find）、权限（chmod）、进程（ps/top） | ⭐ 必修 | 1 天 | [Linux 菜鸟教程](https://www.runoob.com/linux/linux-tutorial.html) |
| 14 | Git 进阶：分支、合并、PR（Pull Request）流程 | ⭐ 必修 | 0.5 天 | [Git 分支管理](https://www.runoob.com/git/git-branch.html) |

#### 可验证目标

- [ ] 手写 10+ 个 Python 练习（计算器、猜数字、文件读写、简单爬虫、待办 CLI）
- [ ] 用 AI 工具从 0 生成并调试一个完整小项目（如：命令行待办事项管理器）
- [ ] 完成一次完整的 Git 分支操作：`branch → commit → push → PR → merge`
- [ ] 写一篇笔记「我如何用 Claude Code 写代码」（Markdown，推到 GitHub）
- [ ] 能用 `requests` 抓取一个网页并解析 JSON 数据

#### ⚠️ 常见坑

- 虚拟环境务必每个项目独立创建，不要全局装包
- JavaScript 的 `var`/`let`/`const` 区别要搞清（推荐只用 `let` 和 `const`）
- AI 生成的代码一定要读懂，不要盲目复制

---

### 阶段 2：前端开发

| 项目 | 内容 |
|------|------|
| **周期** | 第 5-8 周（3-4 周） |
| **目标** | 独立做出美观、可交互的网页，能调用后端接口 |
| **前置条件** | 阶段 1 完成（JS 基础必须过关） |

> **框架选择**：Vue 3 对新手更友好（模板语法直观）；React 生态更大（就业市场广）。**选一个深入，另一个花 1-2 天了解即可。**

#### 学习清单

| # | 内容 | 必修/选修 | 建议用时 | 资源 |
|---|------|----------|---------|------|
| **第 1 周：HTML + CSS 基础** |
| 1 | HTML5 语义化标签：header/nav/main/section/article/footer/form | ⭐ 必修 | 1 天 | [HTML 菜鸟教程](https://www.runoob.com/html/html-tutorial.html) |
| 2 | CSS3 核心：选择器、盒模型、定位（relative/absolute/fixed）、层叠 | ⭐ 必修 | 2 天 | [CSS 菜鸟教程](https://www.runoob.com/css/css-tutorial.html) |
| 3 | Flexbox 弹性布局（完整掌握） | ⭐ 必修 | 1 天 | [Flexbox 图解](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) |
| 4 | CSS Grid 网格布局（掌握基础） | ⭐ 必修 | 1 天 | [Grid 图解](https://css-tricks.com/snippets/css/complete-guide-grid/) |
| **第 2 周：响应式 + JS 进阶** |
| 5 | 响应式设计：媒体查询、rem/vw、移动优先 | ⭐ 必修 | 1 天 | [响应式设计](https://www.runoob.com/css/css-rwd-intro.html) |
| 6 | JavaScript ES6+：解构、展开运算符、箭头函数、模板字符串、Promise | ⭐ 必修 | 2 天 | [ES6 菜鸟教程](https://www.runoob.com/js/js-es6.html) |
| 7 | JS 模块化：import/export | ⭐ 必修 | 1 天 | 同上 |
| 8 | 浏览器 DevTools 深入：Network（请求分析）、Application（存储）、Performance | ⭐ 必修 | 0.5 天 | [DevTools 文档](https://developer.chrome.com/docs/devtools/) |
| **第 3-4 周：框架深入（Vue 3 或 React 二选一）** |
| **▶ 选 Vue 3 路线** |
| 9a | Vue 3 核心：响应式（ref/reactive）、模板语法、计算属性、侦听器 | ⭐ 必修 | 2 天 | [Vue 3 官方文档](https://cn.vuejs.org/) |
| 10a | 组件基础：props、emits、插槽（slot） | ⭐ 必修 | 1 天 | 同上 |
| 11a | Vue Router（路由）、Pinia（状态管理） | ⭐ 必修 | 2 天 | [Vue Router](https://router.vuejs.org/zh/) / [Pinia](https://pinia.vuejs.org/zh/) |
| 12a | Axios 封装、API 调用、拦截器 | ⭐ 必修 | 1 天 | [Axios 文档](https://www.axios-http.cn/) |
| 13a | 用 AI 工具生成组件 / 调试样式 | ⭐ 必修 | 持续 | Claude Code / Codex |
| **▶ 选 React 路线** |
| 9b | React 核心：JSX、组件、Props、State、useState/useEffect | ⭐ 必修 | 2 天 | [React 官方文档](https://zh-hans.react.dev/) |
| 10b | React Hooks 进阶：useContext、useReducer、useRef、自定义 Hook | ⭐ 必修 | 1 天 | 同上 |
| 11b | React Router（路由）、Zustand 或 Redux（状态管理） | ⭐ 必修 | 2 天 | [React Router](https://reactrouter.com/) |
| 12b | Axios 封装、API 调用、拦截器 | ⭐ 必修 | 1 天 | [Axios 文档](https://www.axios-http.cn/) |
| 13b | 用 AI 工具生成组件 / 调试样式 | ⭐ 必修 | 持续 | Claude Code / Codex |
| **收尾** |
| 14 | 快速了解另一个框架（1-2 天，知道核心概念即可） | 选修 | 1 天 | 同上 |

#### 可验证目标

- [ ] 手写一个响应式个人主页（纯 HTML/CSS/JS，手机+桌面双端适配）
- [ ] 用选定的框架做一个 CRUD 小应用（如待办列表，支持增删改查 + 本地存储）
- [ ] 调用一个免费 mock API 展示数据列表（如 [JSONPlaceholder](https://jsonplaceholder.typicode.com/)）
- [ ] 部署静态站点到 GitHub Pages 或 Vercel（有可访问的公网 URL）

#### ⚠️ 常见坑

- 先吃透 Flexbox，Grid 作为补充——不要两个都半懂
- 学框架前确保 JS 的 Promise/async-await 已经理解，否则会卡住
- 不要把时间花在「选 Vue 还是 React」上——选一个开始写，另一个以后再看

---

### 阶段 3：后端开发 + 数据库

| 项目 | 内容 |
|------|------|
| **周期** | 第 9-13 周（4-5 周） |
| **目标** | 能写 RESTful API、设计数据库、处理业务逻辑 |
| **前置条件** | 阶段 1 完成（Python 基础扎实） |

> **后端框架选 FastAPI**：Python 生态、自动生成 API 文档、异步支持、学习曲线平缓。

#### 学习清单

| # | 内容 | 必修/选修 | 建议用时 | 资源 |
|---|------|----------|---------|------|
| **第 1 周：API 基础** |
| 1 | HTTP 协议基础：请求方法（GET/POST/PUT/DELETE）、状态码、请求/响应头 | ⭐ 必修 | 0.5 天 | [HTTP 菜鸟教程](https://www.runoob.com/http/http-tutorial.html) |
| 2 | RESTful API 设计规范：资源命名、路径设计、统一响应格式 | ⭐ 必修 | 0.5 天 | [REST API 指南](https://www.runoob.com/w3cnote/restful-architecture.html) |
| 3 | FastAPI 入门：路由、路径参数、查询参数、请求体 | ⭐ 必修 | 2 天 | [FastAPI 官方文档](https://fastapi.tiangolo.com/zh/) |
| 4 | FastAPI 进阶：Pydantic 数据验证、依赖注入、中间件 | ⭐ 必修 | 2 天 | 同上 |
| **第 2 周：数据库** |
| 5 | SQL 基础：SELECT/INSERT/UPDATE/DELETE、WHERE、ORDER BY、GROUP BY | ⭐ 必修 | 2 天 | [SQL 菜鸟教程](https://www.runoob.com/sql/sql-tutorial.html) |
| 6 | PostgreSQL 安装与使用（或 MySQL，二选一） | ⭐ 必修 | 1 天 | [PostgreSQL 菜鸟教程](https://www.runoob.com/postgresql/postgresql-tutorial.html) |
| 7 | 数据库设计：ER 图、主键/外键、范式（1NF/2NF/3NF）、索引 | ⭐ 必修 | 2 天 | 同上 |
| **第 3 周：ORM + 联调** |
| 8 | SQLAlchemy ORM：模型定义、关系（一对多/多对多）、会话管理 | ⭐ 必修 | 2 天 | [SQLAlchemy 文档](https://docs.sqlalchemy.org/) |
| 9 | 前后端联调：前端 Axios 调用 FastAPI → 数据库 CRUD（打通全链路） | ⭐ 必修 | 2 天 | 综合实战 |
| 10 | CORS 跨域问题处理（FastAPI 中间件配置） | ⭐ 必修 | 0.5 天 | FastAPI CORS 文档 |
| **第 4 周：缓存 + 容器化 + 可选扩展** |
| 11 | Redis 基础：字符串/哈希、缓存策略、会话存储 | ⭐ 必修 | 1 天 | [Redis 菜鸟教程](https://www.runoob.com/redis/redis-tutorial.html) |
| 12 | Docker 实战：写 Dockerfile、docker-compose.yml（FastAPI + PostgreSQL + Redis） | ⭐ 必修 | 2 天 | [Docker 菜鸟教程](https://www.runoob.com/docker/docker-tutorial.html) |
| 13 | 用 AI 生成 API 文档和单元测试 | ⭐ 必修 | 1 天 | Claude Code / Codex |
| 14 | Java 基础 + Spring Boot 入门（如果目标大厂后端） | 选修 | — | [Java 菜鸟教程](https://www.runoob.com/java/java-tutorial.html) |

#### 可验证目标

- [ ] 用 FastAPI 写一套完整 CRUD API（如：用户管理 / 文章管理 / 商品管理）
- [ ] 数据库设计 ER 图 + 至少 3 张关联表，实现增删改查 + 联表查询
- [ ] API 自带 Swagger 文档，可直接交互式调试
- [ ] 前后端联调成功（前端调用真实后端，数据持久化到数据库）
- [ ] 用 Docker Compose 一键启动「后端 + 数据库 + Redis」三个服务
- [ ] 用 AI 工具生成至少 5 个 API 测试用例

#### ⚠️ 常见坑

- 数据库密码等敏感信息用环境变量（`.env`），不要硬编码
- SQLAlchemy session 管理注意线程安全（FastAPI 用 `Depends` 注入）
- CORS 配置不要在生产环境用 `allow_origins=["*"]`

---

### 阶段 4：全栈项目实战 + 部署 + 个人网站

| 项目 | 内容 |
|------|------|
| **周期** | 第 14-17 周（3-4 周） |
| **目标** | 从 0 到 1 上线一个真实项目 + 个人网站正式发布 |
| **前置条件** | 阶段 2 + 3 完成，有可运行的全栈项目 |

#### 学习清单

| # | 内容 | 必修/选修 | 建议用时 | 资源 |
|---|------|----------|---------|------|
| **第 1 周：项目规划 + 鉴权** |
| 1 | 完整项目开发流程：需求分析 → 功能拆解 → 技术选型 → 原型设计 | ⭐ 必修 | 1 天 | — |
| 2 | 用户鉴权（JWT）：注册、登录、token 刷新、权限中间件 | ⭐ 必修 | 3 天 | [FastAPI JWT 教程](https://fastapi.tiangolo.com/zh/tutorial/security/oauth2-jwt/) |
| 3 | Git 工作流规范：feature 分支、commit message 规范、Code Review | ⭐ 必修 | 1 天 | [Conventional Commits](https://www.conventionalcommits.org/zh-hans/) |
| **第 2 周：部署 + DevOps 基础** |
| 4 | Docker Compose 多服务编排（前端 + 后端 + 数据库 + Nginx） | ⭐ 必修 | 2 天 | [Docker Compose 文档](https://docs.docker.com/compose/) |
| 5 | Nginx 反向代理配置、HTTPS（Let's Encrypt 免费证书） | ⭐ 必修 | 1 天 | [Nginx 菜鸟教程](https://www.runoob.com/nginx/nginx-tutorial.html) |
| 6 | 部署平台（选一个）：Railway / Render / 阿里云轻量服务器 | ⭐ 必修 | 1 天 | 平台官方文档 |
| 7 | 域名购买 + DNS 解析配置 | ⭐ 必修 | 0.5 天 | 阿里云 / Cloudflare |
| **第 3 周：网站品质 + CI/CD** |
| 8 | SEO 基础：meta 标签、语义化 HTML、sitemap、结构化数据 | ⭐ 必修 | 1 天 | [SEO 入门指南](https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=zh-cn) |
| 9 | 前端性能优化：图片压缩、懒加载、代码分割、CDN | ⭐ 必修 | 1 天 | Lighthouse 工具实操 |
| 10 | GitHub Actions 自动部署：push → build → deploy | ⭐ 必修 | 1 天 | [GitHub Actions 文档](https://docs.github.com/zh/actions) |
| 11 | 编写项目 README 和部署文档（让别人能照着跑起来） | ⭐ 必修 | 1 天 | — |
| **第 4 周：个人网站完善** |
| 12 | 个人网站 UI 打磨 + 响应式适配 | ⭐ 必修 | 2 天 | — |
| 13 | 添加项目展示页、关于我、联系方式 | ⭐ 必修 | 1 天 | — |

#### 推荐实战项目（从中选 1-2 个）

| 项目 | 涉及技术点 | 难度 |
|------|-----------|------|
| 📝 个人博客系统 | Markdown 渲染、分类标签、评论 | ⭐⭐ |
| ✅ 待办/笔记管理系统 | CRUD、用户鉴权、分类筛选 | ⭐⭐ |
| 🛒 简易电商/图书管理 | 商品管理、购物车、订单流程 | ⭐⭐⭐ |
| 🤖 AI 聊天机器人前端 | SSE 流式响应、对话管理、调用 Claude/OpenAI API | ⭐⭐⭐ |

#### 可验证目标

- [ ] 完整项目上线，有公网可访问地址
- [ ] 个人网站正式上线（自定义域名 + HTTPS）
- [ ] GitHub Actions 跑通：push 代码 → 自动部署
- [ ] 项目 README 含架构图、本地运行步骤、API 文档链接
- [ ] 用 Claude Code / Codex 辅助完成至少 50% 的代码编写

#### ⚠️ 常见坑

- 部署前一定检查 `.env` 是否加入 `.gitignore`
- 云服务器记得配置防火墙规则（只开放 80/443 和 SSH 端口）
- HTTPS 证书用 Let's Encrypt + Certbot 免费自动续期

---

### 阶段 5：AI 深度整合 + 进阶扩展

| 项目 | 内容 |
|------|------|
| **周期** | 第 18 周起（持续 1-2 个月） |
| **目标** | AI 成为生产力核心，具备生产级工程能力，建立个人品牌 |
| **前置条件** | 阶段 4 完成 |

#### 学习清单

| # | 内容 | 必修/选修 | 建议用时 | 资源 |
|---|------|----------|---------|------|
| **AI 编程进阶** |
| 1 | Claude Code / Codex 高级用法：多文件重构、批量生成测试、架构设计辅助 | ⭐ 必修 | 1 周 | 官方文档 + 实操 |
| 2 | Hermes Agent 自定义 Skills、多 Agent 协作任务 | 选修 | 3 天 | Codex 文档 |
| 3 | 提示词工程进阶：Chain-of-Thought、Few-shot、System Prompt 设计 | ⭐ 必修 | 3 天 | 同上 |
| 4 | RAG（检索增强生成）简单实现：向量数据库（Chroma）+ Embedding + LLM 调用 | 选修 | 1 周 | LangChain / LlamaIndex 文档 |
| **DevOps 进阶** |
| 5 | Docker 多阶段构建、镜像优化、Docker Compose 生产配置 | ⭐ 必修 | 3 天 | Docker 官方文档 |
| 6 | CI/CD 实战：自动化测试 → 构建 → 部署（GitHub Actions 完整流水线） | ⭐ 必修 | 1 周 | GitHub Actions 文档 |
| 7 | 日志与监控：Docker logs、简单 Prometheus + Grafana（了解即可） | 选修 | 3 天 | — |
| 8 | Kubernetes 基础概念：Pod、Service、Deployment（了解即可） | 选修 | 1 周 | [K8s 官方教程](https://kubernetes.io/zh-cn/docs/tutorials/) |
| **个人品牌建设** |
| 9 | 持续优化个人网站：添加博客、AI 互动功能（如智能客服） | ⭐ 必修 | 持续 | — |
| 10 | 整理完整学习笔记 + 发布技术博客系列（至少 5 篇） | ⭐ 必修 | 持续 | GitHub Issues / 掘金 / 个人博客 |
| 11 | 参与开源项目：提 PR、修 issue（从 good first issue 开始） | 选修 | 持续 | GitHub Explore |
| **可选扩展方向** |
| 12 | Java + Spring Boot 入门（目标后端岗） | 选修 | — | [Spring Boot 教程](https://spring.io/guides) |
| 13 | 微服务基础概念：服务拆分、API 网关、消息队列 | 选修 | — | — |
| 14 | React Native / Flutter 移动端入门 | 选修 | — | — |

#### 可验证目标

- [ ] 用 AI Agent 独立完成一个完整功能模块（需求 → 设计 → 开发 → 测试 → 部署）
- [ ] 个人项目 CI/CD 完整跑通（push 代码自动测试 + 部署）
- [ ] 个人网站拥有至少 1 个 AI 互动功能
- [ ] 发布至少 5 篇技术博客（Medium / 掘金 / 个人博客）
- [ ] GitHub 年度贡献图保持活跃（每周至少 3 次 commit）

---

## 2. 时间规划总表

| 阶段 | 周次 | 时间 | 累计 | 核心产出 | 里程碑检查 |
|------|------|------|------|----------|-----------|
| 0. 环境+工具 | 第 1 周 | 1 周 | 1 周 | GitHub 仓库 + 开发环境 | ✅ 能写能跑 |
| 1. 语言基础 | 第 2-4 周 | 2-3 周 | 3-4 周 | Python 熟练 + AI 工作流 | ✅ 10+ 练习 + 1 个小项目 |
| 2. 前端开发 | 第 5-8 周 | 3-4 周 | 6-8 周 | 个人主页 + 框架小应用 | ✅ 静态站点上线 |
| 3. 后端+DB | 第 9-13 周 | 4-5 周 | 10-13 周 | 全栈 CRUD API + Docker | ✅ 前后端联调通过 |
| 4. 项目+部署 | 第 14-17 周 | 3-4 周 | 13-17 周 | 个人网站上线 + 1-2 个项目 | ✅ 公网可访问 |
| 5. AI 进阶+扩展 | 第 18 周起 | 持续 | 4-6 个月 | 生产级能力 + 作品集 | ✅ 技术博客 + 自动部署 |

### 每周节奏建议

| 时段 | 周一至周五（每天 2-4h） | 周末（每天 4-6h） |
|------|------------------------|-------------------|
| 上午/白天 | — | 项目实战（大块时间写代码） |
| 晚上 | 学新知识点 + 小练习 | 复盘本周 + 写笔记 + 补充学习 |
| 日常 | 碎片时间用 AI 工具提问/查错 | — |

> **关键习惯**：每天至少用 AI 工具 1 小时——让它帮你写代码、解释报错、生成注释、重构旧代码。

---

## 3. 学习方法与原则

### 核心原则

| # | 原则 | 说明 |
|---|------|------|
| 1 | **项目驱动，不做题家** | 每学完一个知识点，立刻在项目中用上。不要等到「学完」才开始写。 |
| 2 | **AI 优先** | 遇到问题先问 Claude / Codex / Trae，再查文档。学会「如何描述问题」比背语法重要 10 倍。 |
| 3 | **输出倒逼输入** | 每周写 1 篇笔记/博客，用 Markdown 记录。GitHub 就是你的学习证据。 |
| 4 | **先深后广** | 前端一个框架学透；后端 Python 先深入；数据库一个就够了。 |
| 5 | **可演示 > 学完了** | 每个阶段结束必须有一个「能给别人看的东西」——链接、截图、演示视频。 |
| 6 | **20 分钟法则** | 一个问题卡住超过 20 分钟，立刻问 AI 或跳过，不要死磕。 |

### 资源使用策略

```
遇到新概念时：
  1. 先用 AI 工具问「XXX 是什么，给我一个简单例子」（30 秒）
  2. 再查菜鸟教程快速过一遍语法/API（10 分钟）
  3. 需要深入时看官方文档（30 分钟+）
  4. 需要系统学习时看 B站免费课（2-4 小时）
```

### 每日检查项

- [ ] 今天写了代码吗？（哪怕 10 行）
- [ ] 今天用 AI 工具了吗？
- [ ] 今天 commit 了吗？
- [ ] 今天遇到的新知识点记下来了吗？

---

*最后更新：2026.7.12 · 持续迭代中*
