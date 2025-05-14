#!/usr/bin/env bash
############################# INTELLECTUAL PROPERTY RIGHTS #############################
##                                                                                    ##
##                   Copyright (c) 2025 Terminus LLC                                  ##
##                                All Rights Reserved.                                ##
##                                                                                    ##
##          Use of this source code is governed by LICENSE in the repo root.          ##
##                                                                                    ##
############################# INTELLECTUAL PROPERTY RIGHTS #############################
#
#    File:    build-wheel.sh
#    Author:  Marvin Smith
#    Date:    5/14/2025
#
#    Purpose:  Construct virtual environment for building.
#
set -e

#  Python Version
if [ -z ${PYTHON_EXE+x} ]; then
    PYTHON_EXE='python3'
fi

#  Path to venv
VENV_PATH='./venv'

#------------------------------------------------#
#-      Check the current python version        -#
#------------------------------------------------#
function check_python_version()
{
    log_debug "checking python version [${PYTHON_EXE}]"

    VERSION_FULL="$(${PYTHON_EXE} --version | awk '{ print $2 }' )"

    VERSION_MAJOR="$(echo ${VERSION_FULL} | sed 's/\./ /g' | awk '{ print $1 }' )"
    VERSION_MINOR="$(echo ${VERSION_FULL} | sed 's/\./ /g' | awk '{ print $2 }' )"

    if [ "${VERSION_MAJOR}" -lt '3' ]; then
        echo "Python major version cannot be less than 3. Actual version: ${VERSION_FULL}"
        exit 1
    fi
    if [ "${VERSION_MINOR}" -lt '11' ]; then
        echo "Python version cannot be less than 11. Actual version: ${VERSION_FULL}"
        exit 1
    fi
}

#----------------------------#
#-      Print help menu     -#
#----------------------------#
function usage() {
    echo "usage: $(basename $0) <optional-flags>"
    echo
    echo '-h|--help     : Print this message and exit.'
    echo
    echo '-v|--verbose  : Use verbose logging'
    echo '--no-color    : Disable colors in log.bash.'
    echo 
    echo '--python <path/cmd> : Python executable to use.'
    echo '             * Note:  Default is to check ${PYTHON_EXE}, which defaults to python3'
    echo '             * Note:  You can manually set PYTHON_EXE variable to skip this flag as well.'
    echo
    echo '-p <venv_path> : Where to put the virtual environment'
    echo '             * Default is "./venv"'
    echo
}

#  Parse the command-line options
while [ $# -gt 0 ]; do
    case $1 in 

        -h|--help)
            usage
            exit 0
            ;;
            
        -v|--verbose)
            OVERTURE_VERBOSE='true'
            UNIT_VERB='-v'
            ;;
        
        --no-color)
            OVERTURE_NO_COLOR='true'
            ;;
        
        --python)
            shift
            PYTHON_EXE="$1"
            ;;

        -p)
            shift
            VENV_PATH="$1"
            ;;
        
        *)
            echo "error: Unsupported argument: $1"
            exit 1
    esac
    shift
done

#  Initialize logging
. ./scripts/utils/log.bash
log_debug 'Logging initialized'


#  Check python
check_python_version

#  Check if venv already exists
log_debug "Checking if ${VENV_PATH} already exists."
if [ -d "${VENV_PATH}" ]; then
    echo "warning: Virtual-Environment already exists at ${VENV_PATH}"
    exit 1
fi

#  Create environment
log_debug "Creating venv at ${VENV_PATH}"
${PYTHON_EXE} -m venv ${VENV_PATH}

#  Activate environment
. ${VENV_PATH}/bin/activate

#  Install updates
pip3 install --upgrade pip
