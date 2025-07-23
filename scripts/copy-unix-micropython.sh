#!/usr/bin/env bash

#  Exit for any reason
set -e

#  Default Values
COPY_METHOD='rsync'
DO_CLEAN=0
MP_LIBRARY_PATH="${HOME}/.micropython/lib"

BASE_DIR="$(realpath ./nspire)"

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
    rsync -avP  ${BASE_DIR}/ ${MP_LIBRARY_PATH}/


#  This should not be this ugly, however I am finding it weird to use the iCloud folder on my Mac
#  which maps to "${HOME}/Library/Mobile Documents/com~apple~CloudDocs".
#  These spaces are making things odd, so I get a little basic with my steps.
elif [ "${COPY_METHOD}" = 'symlink' ]; then

    FLIST=$(find "${BASE_DIR}" -type f )

    while IFS= read -r line; do

        BNAME=$(basename "$line")
        SOURCE_PATH=$(realpath "$line")
        DEST_PATH="${MP_LIBRARY_PATH}/${BNAME}"

        #  Apply symlink
        echo "Copying: ${SOURCE_PATH} -> ${DEST_PATH}"
        ln -snf "${SOURCE_PATH}" "${DEST_PATH}"

    done <<< "$FLIST"

else
    echo "error: Unsupported copy method: ${COPY_METHOD}"
    exit 1
fi
