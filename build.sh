#!/usr/bin/env bash

apt-get update && apt-get install -y \
  libcairo2 \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  libgdk-pixbuf2.0-0 \
  libffi-dev \
  libjpeg-dev \
  libxml2 \
  libxslt1.1 \
  zlib1g
