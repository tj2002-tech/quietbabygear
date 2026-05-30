# Launch Decision Log

这个文件用来记录关键决策，防止项目执行中反复摇摆。

## 决策模板

### YYYY-MM-DD：决策标题

决定：

原因：

不选择的方案：

复盘日期：

## 已确认决策

### 2026-05-26：域名确定为 quietbabygear.com

决定：

使用 `quietbabygear.com` 作为 QuietBabyGear 的主域名，并已放在 Cloudflare 上管理。

原因：

域名与品牌名完全一致，简短、清晰、适合英文用户，也不会把项目限制在单一产品线。它能承载未来的 baby gear testing database 定位。

下一步：

选择主机方案，将 Cloudflare DNS 指向 WordPress 主机，并开启基础安全和性能设置。

### 2026-05-30：技术路线优先采用 Cloudflare-first

决定：

QuietBabyGear 第一阶段不强制使用 WordPress 服务器，优先采用 Cloudflare-first 静态/边缘架构。

原因：

项目所有者已有多个网站发布经验，不需要为了省学习成本绑定 WordPress。QuietBabyGear 的内容形态以测试数据、Lab Notes、长文、图片和邮箱收集为主，更适合轻量、快速、低成本、HTML 干净的静态或边缘架构。

推荐组合：

Astro + Markdown/MDX + Cloudflare Pages + R2 + Beehiiv。

复盘条件：

如果后续需要多人后台编辑、复杂插件生态、会员或评论系统，再重新评估 WordPress。

### 2026-05-25：QuietBabyGear 不做传统 SEO affiliate 站

决定：

QuietBabyGear 定位为微型消费实验室，核心资产是第一方测试数据库。

原因：

AI 搜索时代，普通 best list 和参数整理越来越容易被替代。真实实验、连续观察、原始素材和测试方法更有长期价值。

不选择的方案：

- 批量 AI 文章站
- Amazon-only affiliate 站
- 单纯导购博客
