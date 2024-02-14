#!/usr/bin/env bash

BASE="/media/notalinux/sdb3/Programation/TypeScript/nextdex/static/"
rsync -av --exclude={"js/data","js/index.js","js/data_version.js","js/settings.js","index.html"} ${BASE} ./front/
