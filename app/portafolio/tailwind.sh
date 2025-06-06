#!/bin/sh

npm install -D tailwindcss
npx tailwindcss init
npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
