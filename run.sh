#!/bin/bash
IMG="python-graphic"
OUTPUT="$(pwd)/output"
docker build -t $IMG .
docker run -v $OUTPUT:/output $IMG
