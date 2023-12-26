# Use the official MySQL image as the base image
FROM mysql:latest

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
#ENV MYSQL_DATABASE=mydb
#ENV MYSQL_USER=clinton
#ENV MYSQL_PASSWORD=root
#ENV SECURE-FILE-PRIV=/var/


# Copy custom MySQL configuration file.
COPY sqlscript.sql /docker-entrypoint-initdb.d/
#RUN chmod -R 777 /docker-entrypoint-initdb.d/ 


EXPOSE 3306 
# Start MySQL server when the container starts

# Optionally, you can include a HEALTHCHECK to ensure the MySQL service is healthy
# HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD mysqladmin ping -h 127.0.0.1
