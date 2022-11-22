FROM node:latest

# Define working directory
WORKDIR /app

# Get app package data
COPY package*.json /app/

# Install packages
RUN npm install npm
RUN npm install

# Copy source files
COPY . /app/

# Build app
RUN npm run build

# Expose 3000
EXPOSE 3000

# Run app
CMD "npm" "run" "start" 



