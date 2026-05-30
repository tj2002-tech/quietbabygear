# 技术架构决策：Cloudflare-first，而不是 WordPress-first

## 结论

QuietBabyGear 第一阶段建议使用 Cloudflare 全家桶做轻量内容站，而不是购买 WordPress 服务器。

推荐架构：

- Cloudflare DNS
- Cloudflare Pages 或 Workers Static Assets
- Astro / Next.js static export / Hugo 任选其一
- Markdown / MDX 管理文章和 Lab Notes
- R2 存放原始测试图片和视频
- Turnstile 防垃圾表单
- Beehiiv / ConvertKit / Brevo 处理邮箱
- GitHub 作为内容和代码仓库

## 为什么适合 QuietBabyGear

QuietBabyGear 的核心不是会员系统、复杂评论区或电商后台，而是：

- 测试数据表
- 长文内容
- Lab Notes
- 原创图片
- 邮箱收集
- 联盟链接
- 跨平台引用

这些都非常适合静态站或边缘渲染站。

## 相比 WordPress 的优势

- 成本更低
- 页面更快
- HTML 更干净
- 安全面更小
- 不需要维护 PHP、数据库和插件
- 更适合结构化内容和 AI 抓取
- 内容可版本化，方便维护测试数据

## 代价

- 没有 WordPress 后台编辑器
- 插件生态不能直接用
- 内容发布需要 Git 或轻量 CMS
- 表单、搜索、图片管理需要自己组合服务

## 推荐实现方式

第一阶段最推荐：

`Astro + Markdown/MDX + Cloudflare Pages + R2 + Beehiiv`

原因：

- 内容站体验好
- 静态输出快
- Markdown 非常适合 Lab Notes
- 后续能加 React 组件做测试表格
- 部署到 Cloudflare 成本低

## 不建议第一阶段做

- WordPress 静态导出到 Cloudflare Pages
- 自建 CMS
- 自建邮件系统
- 自建图片处理系统
- 上来就用复杂数据库

## 什么时候才考虑 WordPress

只有出现以下情况再考虑：

- 需要非技术成员频繁后台编辑
- 需要大量插件工作流
- 需要复杂评论、会员或权限
- 你明确想用 WordPress 生态变现

## 第一阶段技术目标

30 天内只需要做到：

- 首页上线
- Testing Methodology 上线
- Lab Notes 栏目上线
- 第一篇测试文章可发布
- Email 表单可用
- 图片素材可通过 R2 或本地优化流程管理

