#!/bin/sh

: ${CACHE_DIR=".cache"}
: ${REPO_NAME="labwc"}
: ${REPO_URL="https://github.com/labwc/labwc.git"}
: ${REPO_DIRS=src/ include/}

blame () {
	git ls-files ${REPO_DIRS} | while read -r filename; do
		git blame -w -C -C -C --line-porcelain "$filename"
	done | grep '^author ' | sort | uniq -c
}

create_cache () {
	printf '%b\n' "Creating cache for ${*}"
	[ -e "${REPO_NAME}" ] || git clone "${REPO_URL}"
	cd "${REPO_NAME}" || { print '%b\n' "fatal: no repo"; exit 1; }
	git checkout master >/dev/null 2>&1
	git checkout "${*}"
	blame > "../${CACHE_DIR}/${*}"
}

mkdir -p "${CACHE_DIR}"
for t in $FOOTPRINT_REFS; do
	[ -e  "${CACHE_DIR}/${t}" ] && continue
	( create_cache "${t}" )
done

