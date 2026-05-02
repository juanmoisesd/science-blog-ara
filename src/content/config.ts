import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    category: z.string(),
    author: z.string(),
    date: z.string(),
  }),
});

export const collections = {
  'psychology': blogCollection,
  'neuroscience': blogCollection,
};
