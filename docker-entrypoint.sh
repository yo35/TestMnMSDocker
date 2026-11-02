#!/bin/sh

set -e

# If no argument (or "--help" or similar) is provided, print usage information and exit.
if [ $# -eq 0 ] || [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
    cat /app/docker-entrypoint-usage.txt
    exit 0
fi

# Otherwise, depending on the first argument...
case "$1" in

    # For a JSON file, run the MnMS CLI launcher.
    *.[jJ][sS][oO][nN])
        exec python /app/script/running/run.py "$@"
        ;;

    # For a Python file (more advanced usage), run it directly.
    *.[pP][yY])
        exec python "$@"
        ;;

    # Other file types are not supported.
    *)
        echo "Error: unsupported argument '$1' (expected a .json or .py file)." >&2
        echo "" >&2
        cat /app/docker-entrypoint-usage.txt >&2
        exit 2
        ;;

esac
