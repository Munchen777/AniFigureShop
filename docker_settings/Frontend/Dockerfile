FROM node:24-alpine AS build

WORKDIR /app

COPY frontend/package*.json ./

RUN npm install

COPY frontend/ ./

RUN npm run build

FROM nginx:1.27.5-alpine
RUN mkdir -p /app/frontend

COPY --from=build /app/build /usr/share/nginx/html

COPY docker_settings/Frontend/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
