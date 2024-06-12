FROM python:3.12-alpine3.20
LABEL maintainer="pedrozaccaria@gmail.com"

# This environment variable is used to control if Python should
# record btyecode (.pyc) files in dis. 0 == YES, 1 == NO
ENV PYTHONDONTWRITEBYTECODE 1

# Sets Python output to be displayed immediately to the console or
# other output devices, without being buffered.
# In short, sees Python outputs in real time
ENV PYTHONUNBUFFERED 1

# Copy the "djangoapp" and "scripts" folder into the container
COPY djangoapp /djangoapp
COPY scripts /scripts

# Go to the djangoapp folder in the container
WORKDIR /djangoapp

# Port 8000 will be available for external connections to the container.
# It's the port being used for Django
EXPOSE 8000

# The result of executing the command is stored in the file system 
# image as a new layer.
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media && \
    chmod -R +x /scripts

# Add the scripts and venv/bin folder 
# in the container's $PATH.
ENV PATH="/scripts:/venv/bin:$PATH"

# Changes the user to duser
USER duser

# Executes the file scripts/commands.sh
CMD ["commands.sh"]