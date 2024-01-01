FROM python:3.10.10
# FROM postgres:15.3
ENV PYTHONUNBUFFERED=1
# ---------- PostgreSQL Intializtion ----------
# Install PostgreSQL client
RUN apt-get update && apt-get install -y postgresql-client

# Install OpenSSL and sudo
RUN apt-get install -y openssl sudo

# Allow the postgres user to execute certain commands as root without a password
RUN echo "postgres ALL=(root) NOPASSWD: /usr/bin/mkdir, /bin/chown" > /etc/sudoers.d/postgres

# Add init scripts
COPY init-ssl.sh /docker-entrypoint-initdb.d/
COPY wrapper.sh /usr/local/bin/wrapper.sh
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# Set permissions
RUN chmod +x /docker-entrypoint-initdb.d/init-ssl.sh
RUN chmod +x /usr/local/bin/wrapper.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# ENTRYPOINT ["wrapper.sh"]

# # ---------- Python Intializtion ----------
# Set the working directory
WORKDIR /app

# Copy application files
COPY . .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the Gunicorn port
EXPOSE 8000

# Set the entrypoint to wrapper.sh

ENTRYPOINT ["wrapper.sh"]

# Run the default command (e.g., Gunicorn)
CMD ["gunicorn", "core.wsgi:application"]


