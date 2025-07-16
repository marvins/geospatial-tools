#!/usr/bin/env bash

#  Exit for any reason
set -e

#  Default Values
COPY_METHOD='rsync'
DO_CLEAN=0
MP_LIBRARY_PATH="${HOME}/.micropython/lib"


#------------------------------------------------#
#-          Print Usage Instructions            -#
#------------------------------------------------#
function usage()
{
    echo "usage: $0 [optional args]"
    echo
    echo 'optional flags:'
    echo '-h | --help : Print usage instructions and exit.'
    echo
    echo '-s | --symlink : Create links to library path rather than copy.'
    echo
    echo '-c | --clean  : Clean Micropython library folder first.'
    echo
}

#------------------------------------------------#
#-          Parse Command-Line Options          -#
#------------------------------------------------#
while [ $# -gt 0 ]; do
    case $1 in

        -h|--help)
            usage
            exit 0
            ;;

        -s|--symlink)
            COPY_METHOD='symlink'
            ;;

        -c|--clean)
            DO_CLEAN=1
            ;;

        *)
            echo "error: Unsupported flag: ${1}"
            exit 1
            ;;
    esac
    shift
done

#--------------------------------------------#
#-          Clean Library Folder            -#
#--------------------------------------------#
if [ "${DO_CLEAN}" = '1' ]; then

    echo "Cleaning Micropython folder"

    #  I'm lazy.  I'm deleting and rebuilding the folder
    if [ -d "${MP_LIBRARY_PATH}" ]; then
        rm -rvf ${MP_LIBRARY_PATH}
    fi

    mkdir -p ${MP_LIBRARY_PATH}

fi

#--------------------------------------------#
#-        Copy Library Folder Over          -#
#--------------------------------------------#
if [ "${COPY_METHOD}" = 'rsync' ]; then
    rsync -avP  ./nspire/ ${MP_LIBRARY_PATH}/

elif [ "${COPY_METHOD}" = 'symlink' ]; then
    for P in $(find ./nspire/ -type f); do

        SOURCE_PATH="$(realpath ${P})"

        DEST_PATH="${MP_LIBRARY_PATH}/$(basename ${SOURCE_PATH})"
        echo "Copying: ${SOURCE_PATH} -> ${DEST_PATH}"

        ln -snf ${SOURCE_PATH} ${DEST_PATH}
    done

else
    echo "error: Unsupported copy method: ${COPY_METHOD}"
    exit 1
fi
