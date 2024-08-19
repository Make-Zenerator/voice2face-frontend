FROM node:18 as build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install -g pm2
RUN npm install dotenv

COPY . ./
RUN npm run build

CMD ["pm2-runtime", "start", "pm2.config.js", "--env", "production"]
