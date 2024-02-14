#!/usr/bin/env bash

BASE="/media/notalinux/sdb3/Programation/TypeScript/nextdex/static/"
echo --exclude={"${BASE}js/data/*","${BASE}js/index.js","${BASE}js/data_version.js","${BASE}sprites/*"} ${BASE} ./front/

exit
rsync -av --exclude={"${BASE}js/data/*","${BASE}js/index.js","${BASE}js/data_version.js","${BASE}sprites/*"} ${BASE} ./front/