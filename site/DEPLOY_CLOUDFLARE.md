# Deploy QuietBabyGear to Cloudflare Pages

This project is designed for the GitHub -> Cloudflare Pages route.

## Cloudflare Pages settings

- Project name: `quietbabygear`
- Production branch: `main`
- Framework preset: `Astro`
- Root directory: `site`
- Build command: `npm run build`
- Build output directory: `dist`
- Node.js version: `22` or latest Cloudflare-supported LTS

## Created project

- Project name: `quietbabygear`
- Pages subdomain: `quietbabygear.pages.dev`
- GitHub repo: `tj2002-tech/quietbabygear`

## Custom domain

Add:

- `quietbabygear.com`
- `www.quietbabygear.com`

Cloudflare should create the required DNS records automatically when the domain is already in the same Cloudflare account.

## First deploy checklist

- [ ] Push repo to GitHub
- [ ] Create Cloudflare Pages project
- [ ] Connect GitHub repo
- [ ] Set root directory to `site`
- [ ] Deploy
- [ ] Add custom domain
- [ ] Confirm HTTPS
- [ ] Confirm `/`, `/methodology/`, `/lab-notes/`, and `/tests/` load

## After deployment

Replace the placeholder email forms in:

- `src/pages/index.astro`
- `src/pages/checklist.astro`

with Beehiiv, Brevo, ConvertKit, or another email provider endpoint.

## Local note

If local `npm install` is slow or blocked, Cloudflare Pages can still install dependencies in its build environment after the project is pushed to GitHub.
