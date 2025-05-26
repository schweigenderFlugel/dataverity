FROM node:22-alpine3.21 AS deps

USER root

WORKDIR /app

COPY package*.json ./

RUN npm ci --ignore-scripts

FROM node:22-alpine3.21 AS build

USER root

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules
COPY --from=deps /app/package*.json ./
COPY tsconfig*.json ./
COPY vite.config.ts ./
COPY index.html ./
COPY src ./src

RUN npm run build

RUN npm prune --production

FROM nginx:1.28-alpine3.21 AS runner

RUN apk add --no-cache gettext

COPY --from=build /app/dist /usr/share/nginx/html
COPY env.template.js /usr/share/nginx/html/env.template.js
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY scripts/entrypoint-docker.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 80

CMD ["sh", "entrypoint.sh"]