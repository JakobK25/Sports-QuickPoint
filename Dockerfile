FROM postgres:latest

# Expose the PostgreSQL port
EXPOSE 5432

# Copy initialization SQL script
COPY ./init.sql /docker-entrypoint-initdb.d/