FROM node:latest AS build

WORKDIR /usr/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 9000

RUN npm run build

FROM nginx:alpine

COPY --from=build /usr/app/dist /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
