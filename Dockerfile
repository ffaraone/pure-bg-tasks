FROM cloudblueconnect/connect-extension-runner:28.14

COPY pyproject.toml poetry.* package*.json /extension/
WORKDIR /extension
RUN poetry update && poetry install --no-root
RUN if [ -f "/extension/package.json" ]; then npm install; fi
