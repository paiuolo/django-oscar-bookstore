#!/bin/bash

# check argomenti e set variabili
# set remote host
HOST_REMOTO=$1
[ -z "$HOST_REMOTO" ] && echo "Specificare url o IP dell'host" && exit 1
# set remote user
NOME_UTENTE=$2
[ -z "$NOME_UTENTE" ] && echo "Specificare l'utente dell'host" && exit 1
# set project name
PROJECT_NAME=$3
[ -z "$PROJECT_NAME" ] && echo "Specificare il nome del progetto" && exit 1
# exit if no action specified
ACTION=$4
[ -z "$ACTION" ] && echo "Specificare azione" && exit 1

REPO_NAME="django-oscar-bookstore"
REPO_URL="https://github.com/paiuolo/${REPO_NAME}.git"

PROJECT_DIR="/home/${NOME_UTENTE}/${PROJECT_NAME}/"
REPOSITORY_DIR="${PROJECT_DIR}${REPO_NAME}/"

DEPS="build-essential python3 python3-dev python3-venv libjpeg-dev libfreetype6-dev zlib1g-dev node-less redis-server git"

printf "Password: "
read -s USER_PASS

# ACTIONS

case "$ACTION" in
"load")
	fab -u $NOME_UTENTE -H $HOST_REMOTO install_deps:"$DEPS" -p $USER_PASS || exit 1
	fab -u $NOME_UTENTE -H $HOST_REMOTO create_dir:$PROJECT_NAME -p $USER_PASS || exit 1
	fab -u $NOME_UTENTE -H $HOST_REMOTO create_digital_files_dir:$REPO_NAME -p $USER_PASS || exit 1
	fab -u $NOME_UTENTE -H $HOST_REMOTO create_virtualenv:$PROJECT_NAME -p $USER_PASS || exit 1
	fab -u $NOME_UTENTE -H $HOST_REMOTO install_python_deps:$PROJECT_NAME -p $USER_PASS || exit 1
	fab -u $NOME_UTENTE -H $HOST_REMOTO clone_repo:$PROJECT_NAME,$REPO_URL -p $USER_PASS || exit 1
	exit 0
	;;
"setup")
    fab -u $NOME_UTENTE -H $HOST_REMOTO init_repo:$PROJECT_NAME,$REPO_NAME -p $USER_PASS || exit 1
    exit 0
    ;;
"check")
	fab -u $NOME_UTENTE -H $HOST_REMOTO run_tests:$PROJECT_NAME,$REPO_NAME -p $USER_PASS || exit 1
	exit 0
	;;
*)
    echo "Azione non prevista"
	sleep 0
	exit 1
	;;
esac

exit 0
