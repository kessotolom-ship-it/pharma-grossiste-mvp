import { loadEnv, defineConfig } from '@medusajs/framework/utils'

loadEnv(process.env.NODE_ENV || 'development', process.cwd())

module.exports = defineConfig({
  projectConfig: {
    databaseUrl: process.env.DATABASE_URL,
    http: {
      // Utilise la variable du fichier .env, ou l'URL en dur si le .env est vide
      storeCors: process.env.STORE_CORS || 'https://xxxx-8000.app.github.dev',
      adminCors: process.env.ADMIN_CORS || '',
      authCors: process.env.AUTH_CORS || '',
      jwtSecret: process.env.JWT_SECRET || 'supersecret-jwt-key-change-in-prod',
      cookieSecret: process.env.COOKIE_SECRET || 'supersecret-cookie-key-change-in-prod',
    },
  },
  admin: {
    path: '/app',
  },
  modules: [], // On laisse vide car la v2 gère le currency nativement
})