# Day 2：Cloudflare + WordPress 建站执行

当前已完成：

- 主域名：`quietbabygear.com`
- DNS 管理：Cloudflare

## 今天目标

让 `quietbabygear.com` 具备上线 WordPress 的条件。

完成标准：

- 主机方案确认
- WordPress 站点创建
- Cloudflare DNS 指向主机
- SSL 可用
- 基础页面结构创建
- 不追求设计完美，先让站点骨架跑起来

## 你需要做

### 1. 选择主机

二选一即可：

| 方案 | 建议 | 备注 |
|---|---|---|
| Cloudways | 更适合长期项目 | 推荐 DigitalOcean 1GB 起步 |
| Hostinger | 更便宜更省事 | 初期也够用 |

我的建议：

如果预算允许，用 Cloudways。QuietBabyGear 未来靠页面速度、结构清晰和长期内容资产，Cloudways 更稳。

### 2. 创建 WordPress 站点

站点名称：

`QuietBabyGear`

管理员邮箱：

优先使用：

- `hello@quietbabygear.com`
- `research@quietbabygear.com`

如果域名邮箱还没开，用临时 Gmail。

### 3. 给我确认 4 个信息

你建好主机后，告诉我：

1. 用的是 Cloudways 还是 Hostinger？
2. WordPress 是否已经安装？
3. Cloudflare DNS 是否已经拿到主机 IP 或 CNAME？
4. 项目邮箱准备用哪个？

## Cloudflare 基础设置建议

### DNS

常见设置：

| Type | Name | Content |
|---|---|---|
| A | `@` | 主机 IP |
| CNAME | `www` | `quietbabygear.com` |

### SSL/TLS

建议：

- SSL/TLS mode：Full
- Always Use HTTPS：On
- Automatic HTTPS Rewrites：On

如果主机已经有有效 SSL，可以用 Full strict。

### Speed

先开启：

- Brotli：On
- Auto Minify HTML/CSS/JS：暂时 Off，等 WordPress 缓存插件配置后再决定

### Caching

先保持默认即可。WordPress 端后面用 LiteSpeed Cache 或主机自带缓存。

## 我来准备

### 1. WordPress 页面文案

我会准备：

- Home
- Testing Methodology
- Lab Notes
- About
- Affiliate Disclosure
- Privacy Policy 初稿结构

### 2. 首页模块

首页先做成 Research Hub：

1. Hero
2. Latest Testing Results
3. Testing Database Metrics
4. Latest Lab Notes
5. 3AM Checklist Email Capture

### 3. 第一篇文章草稿

文章：

`Easiest Baby Nasal Aspirator to Clean at 3AM`

先搭骨架，真实数据等产品到货后填入。

## 今天不做

- 不买复杂付费主题
- 不装 Elementor
- 不追求 Logo 完美
- 不急着申请广告
- 不急着发 Reddit 链接

