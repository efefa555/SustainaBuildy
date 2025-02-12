# Use the official Node.js image to build the frontend assets
FROM node:14 as frontend-builder

WORKDIR /usr/src/app/frontend

COPY frontend/package*.json ./
RUN npm install

COPY frontend/ ./
RUN npm run build

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY backend/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt

# Copy the rest of the application code into the container
COPY backend/ .

# Copy the built frontend assets into the container
COPY --from=frontend-builder /usr/src/app/frontend/dist ./frontend/dist

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]