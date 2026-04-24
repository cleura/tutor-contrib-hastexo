FROM {{ STACKAMOLE_BASE_IMAGE }}
ENV PYTHONUNBUFFERED=1
ARG STACKAMOLE_XBLOCK_GIT_REPOSITORY=https://github.com/mrtmm/stackamole-xblock.git
ARG STACKAMOLE_XBLOCK_VERSION={{ STACKAMOLE_XBLOCK_VERSION }}
RUN git clone $STACKAMOLE_XBLOCK_GIT_REPOSITORY -b $STACKAMOLE_XBLOCK_VERSION ./stackamole-xblock
WORKDIR ./stackamole-xblock
RUN pip install --upgrade pip && \
    pip install -r requirements/base.txt --exists-action w .
EXPOSE 8095
CMD daphne -b 0.0.0.0 -p 8095 stackamole_guacamole_client.asgi:application
