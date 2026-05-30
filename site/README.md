# QuietBabyGear Site

Astro static site for `quietbabygear.com`.

## Local development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## Cloudflare Pages

Recommended settings:

- Framework preset: Astro
- Root directory: `site`
- Build command: `npm run build`
- Build output directory: `dist`
- Environment variable: none required for the static launch

See `DEPLOY_CLOUDFLARE.md` for the full GitHub -> Cloudflare Pages checklist.

## Launch order

1. Deploy static shell to Cloudflare Pages.
2. Connect `quietbabygear.com`.
3. Replace email form action with Beehiiv/Brevo/ConvertKit embed endpoint.
4. Add first original product photos.
5. Publish the first completed test article after data is collected.
