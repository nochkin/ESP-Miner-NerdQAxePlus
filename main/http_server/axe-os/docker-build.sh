#!/bin/sh

docker run --rm -u $(id -u):$(id -g) -v "$(pwd)":/app -w /app node:24-slim sh -c "npm i && npm run build"


