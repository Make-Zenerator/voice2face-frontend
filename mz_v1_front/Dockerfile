FROM node:18 as build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install -g pm2

COPY . ./
RUN npm run build --port 80

<<<<<<< HEAD
CMD ["pm2-runtime", "start", "./build/index.js", "--env", "production", "--port", "80"]
=======
CMD ["pm2-runtime", "start", "./build/index.js", "--env", "production"]
>>>>>>> 5116ec56b70f1c9d0192064ab4606ed4fdc07d6f
