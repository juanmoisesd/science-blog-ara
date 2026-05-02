import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://science-blog-ara.pages.dev',
  integrations: [sitemap()],
});
