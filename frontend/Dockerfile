FROM nginx:alpine

# Копируем наш кастомный конфиг Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Копируем собранные файлы в nginx
COPY index.html /usr/share/nginx/html/index.html

# Папка для статических изображений
RUN mkdir -p /usr/share/nginx/html/static

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]