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

FROM node:22-alpine3.21 AS runner

WORKDIR /app

RUN npm install -g serve

COPY --from=build /app/package*.json ./
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/dist ./

RUN addgroup -g 1234 dataverity-group && \
  adduser -D -u 1234 -G dataverity-group dataverity-user

USER dataverity-user:dataverity-group

CMD [ "serve", "-s", "-l", "5173", "." ]