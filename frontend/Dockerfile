FROM node:18-alpine

WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install --legacy-peer-deps

# Copia os arquivos de configuração do TailwindCSS
COPY tailwind.config.js ./
COPY postcss.config.js ./

# Copia o arquivo .env para o contêiner
COPY . .

CMD ["npm", "start"]
