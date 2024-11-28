# Official Node Img
FROM node:16 AS build

# Setting up the working directory
WORKDIR /app

# Copy package.json and package-lock.json for dependency installation
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copying rest of application files
COPY . .

# Build react app
RUN npm run build

# Use an NGINX image to serve the static files
FROM nginx:alpine

# Copy built files to NGINX directory
COPY --from=build /app/build /usr/share/nginx/html

#Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]