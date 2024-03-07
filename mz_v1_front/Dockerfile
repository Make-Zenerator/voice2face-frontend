FROM node:20 as build

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./

CMD ["npm", "run", "build"]