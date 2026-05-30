# API and Service Requirements

QuietBabyGear can launch the first static version without any API keys.

## Required for first public launch

None.

The first version can deploy to Cloudflare Pages with static pages only.

## Needed soon

### Email capture

Choose one provider:

- Beehiiv
- Brevo
- ConvertKit
- Buttondown

Needed from you:

- Signup form embed code or form action URL
- Publication/list ID if the provider uses one
- API key only if we use a custom form instead of embed

Where it will be used:

- `src/pages/index.astro`
- `src/pages/checklist.astro`

### Analytics

Choose one:

- Cloudflare Web Analytics
- Microsoft Clarity
- Plausible

Needed from you:

- Tracking script or site token

Recommended first:

Cloudflare Web Analytics + Microsoft Clarity.

## Optional later

### Cloudflare R2

Use when original product photos and short videos start growing.

Needed:

- R2 bucket name
- Public bucket URL or custom media domain
- Access key only if we automate uploads

Suggested bucket:

`quietbabygear-media`

### Cloudflare Turnstile

Use when forms are custom instead of provider embeds.

Needed:

- Site key
- Secret key, only for server-side validation

### Cloudflare D1

Use later if we want a queryable testing database instead of static CSV/JSON.

Needed:

- Database name
- Binding name

Suggested:

- Database: `quietbabygear`
- Binding: `DB`

### Search

Not needed at launch.

Options later:

- Pagefind for static local search
- Algolia if content grows large

## Current recommendation

Launch sequence:

1. Deploy static Astro site with no API keys.
2. Add Cloudflare Web Analytics.
3. Add Beehiiv or Brevo email form.
4. Add Microsoft Clarity.
5. Add R2 only after real test media starts accumulating.

