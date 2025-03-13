FROM postgres:latest

# Set environment variables
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=scoredb

# Expose the PostgreSQL port
EXPOSE 5432