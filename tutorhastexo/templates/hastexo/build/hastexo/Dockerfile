FROM {{ HASTEXO_BASE_IMAGE }}
ENV PYTHONUNBUFFERED 1
ARG HASTEXO_XBLOCK_GIT_REPOSITORY=https://github.com/cleura/hastexo-xblock.git
ARG HASTEXO_XBLOCK_VERSION={{ HASTEXO_XBLOCK_VERSION }}
RUN git clone $HASTEXO_XBLOCK_GIT_REPOSITORY -b $HASTEXO_XBLOCK_VERSION ./hastexo-xblock
WORKDIR ./hastexo-xblock
RUN pip install --upgrade pip && \
    pip install -r requirements/base.txt --exists-action w .
EXPOSE 8095
CMD daphne -b 0.0.0.0 -p 8095 hastexo_guacamole_client.asgi:application
