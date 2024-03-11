FROM node:18 as build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./
RUN npm run build

CMD ["pm2", "start", "./build/index.js"]