import { test, expect } from '@playwright/test';

test('hello word page loads', async ({ page }) => {
  await page.goto('http://localhost:8080/');
  await expect(page).toHaveTitle(/hello word/i);
  const content = await page.textContent('body');
  expect(content).toContain('hello word');
});