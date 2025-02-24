labwc: CACHE_DIR=.cache/labwc
labwc: REPO_NAME=labwc
labwc: REPO_URL=https://github.org/labwc/labwc.git
labwc: REPO_DIRS=src/ include/
labwc: FOOTPRINT_REFS=0.8.3 0.8.2 0.8.0 0.7.0 0.6.0 0.5.0 0.4.0 0.3.0

wlroots: CACHE_DIR=.cache/wlroots
wlroots: REPO_NAME=wlroots
wlroots: REPO_URL=https://gitlab.freedesktop.org/wlroots/wlroots.git
wlroots: REPO_DIRS=.
wlroots: FOOTPRINT_REFS=0.18.0 0.17.0 0.16.0 0.15.0 0.14.0 0.13.0 0.12.0 0.11.0 0.10.0

export CACHE_DIR
export REPO_NAME
export REPO_URL
export REPO_DIRS
export FOOTPRINT_REFS

all: labwc

labwc:
	@./count.sh
	@./plot.py --tags "$(FOOTPRINT_REFS)"

wlroots:
	echo $(CACHE_DIR)
	@./count.sh
	@./plot.py --tags "$(FOOTPRINT_REFS)"

.PHONY: labwc wlroots
