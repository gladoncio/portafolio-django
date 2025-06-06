#!/bin/sh

dos2unix /app/app/portafolio/tailwind.sh
./app/core/tailwind.sh

# # Migrar la base de datos
python ./app/manage.py makemigrations
python ./app/manage.py migrate core
python ./app/manage.py migrate

# Ejecutar el servidor
exec python ./app/manage.py runserver 0.0.0.0:8000


# # Mantener el contenedor corriendo
# tail -f /dev/null