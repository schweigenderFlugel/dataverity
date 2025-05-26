#!/bin/sh

echo "🔧 Inyectando variables de entorno..."
envsubst < /usr/share/nginx/html/env.template.js > /usr/share/nginx/html/env.js

echo "🚀 Iniciando Nginx..."
exec nginx -g 'daemon off;'