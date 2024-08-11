import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    rollupOptions: {
      external: [
        fileURLToPath(new URL('/resources/invito_bg.jpg', import.meta.url)),
      ]
    }
  },
  plugins: [vue({
    template: {
      transformAssetUrls: {
        includeAbsolute: false
      }
    }
  })],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
