
# Use an official Node.js runtime as the base image
FROM node:14-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY /react/react-app/package*.json ./

# Install project dependencies
RUN npm install

# Copy the entire project directory to the container
COPY /react/react-app .

# Build the React app
RUN npm run build

# Expose the port on which the React app will run
EXPOSE 3000

# Set the command to run when the container starts
CMD ["npm", "start"]
