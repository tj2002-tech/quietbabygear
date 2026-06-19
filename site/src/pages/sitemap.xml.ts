const pages = [
  ["/", "2026-06-19", "weekly", "1.0"],
  ["/tests/", "2026-06-19", "weekly", "0.9"],
  ["/tests/nosefrida-vs-grownsy-at-3am/", "2026-06-19", "monthly", "0.9"],
  ["/tests/easiest-baby-nasal-aspirator-to-clean-at-3am/", "2026-06-04", "monthly", "0.6"],
  ["/methodology/", "2026-06-19", "monthly", "0.8"],
  ["/methodology/3am-cleaning-test/", "2026-06-19", "monthly", "0.8"],
  ["/lab-notes/", "2026-06-19", "weekly", "0.8"],
  ["/lab-notes/nosefrida-grownsy-first-reset-notes/", "2026-06-19", "monthly", "0.7"],
  ["/about/", "2026-06-04", "monthly", "0.6"],
  ["/affiliate-disclosure/", "2026-06-04", "yearly", "0.3"],
  ["/privacy/", "2026-06-04", "yearly", "0.3"],
  ["/checklist/", "2026-06-04", "monthly", "0.5"]
] as const;

export function GET() {
  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${pages
  .map(([path, lastmod, changefreq, priority]) => `  <url>
    <loc>https://quietbabygear.com${path}</loc>
    <lastmod>${lastmod}</lastmod>
    <changefreq>${changefreq}</changefreq>
    <priority>${priority}</priority>
  </url>`)
  .join("\n")}
</urlset>`;

  return new Response(body, {
    headers: {
      "Content-Type": "application/xml"
    }
  });
}

