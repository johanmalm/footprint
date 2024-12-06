#!/bin/sh

: ${CACHE_DIR=".cache"}

blame () {
	git ls-files src/ include/ | while read -r filename; do
		git blame -w -C -C -C --line-porcelain "$filename"
	done | grep '^author ' | sort | uniq -c
}

create_cache () {
	printf '%b\n' "Creating cache for ${*}"
	[ -e labwc/ ] || git clone https://github.com/labwc/labwc.git
	cd labwc || { print '%b\n' "fatal: no repo"; exit 1; }
	git checkout master >/dev/null 2>&1
	git checkout "${*}"
	blame > "../${CACHE_DIR}/${*}"
}

mkdir -p "${CACHE_DIR}"
for t in $FOOTPRINT_REFS; do
	[ -e  "${CACHE_DIR}/${t}" ] && continue
	( create_cache "${t}" )
done

