#!/bin/bash

# Regenerate Suger Python SDK from OpenAPI specification
# This script uses the same command that was used to generate the current codebase

# Default version
DEFAULT_VERSION="v3.128.220"

# Parse command line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --version)
      VERSION="$2"
      shift 2
      ;;
    *)
      echo "Unknown parameter: $1"
      echo "Usage: $0 [--version VERSION]"
      exit 1
      ;;
  esac
done

# Use provided version or default
VERSION=${VERSION:-$DEFAULT_VERSION}

echo "Regenerating Suger Python SDK from OpenAPI specification..."
echo "Using version: $VERSION"

# Make sure we have openapi-generator installed
if ! command -v openapi-generator &> /dev/null; then
    echo "Error: openapi-generator is not installed."
    echo "Install it with: npm install @openapitools/openapi-generator-cli -g"
    echo "Or use: brew install openapi-generator"
    exit 1
fi


# Run the OpenAPI generator
echo "Running OpenAPI generator..."
openapi-generator generate \
  -i api/openapi.yaml \
  -g python \
  -o ./ \
  --package-name suger_sdk_python \
  --git-repo-id suger-sdk-python \
  --git-user-id sugerio \
  --additional-properties=packageVersion="$VERSION"

echo "Code regeneration complete!"