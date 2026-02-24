#!/bin/bash
# FORMAT: backups-YYYY/MM-DD/HH.mm
NEW_BACKUP_PATH="backup/backups-$(date -u "+%Y/%m-%d/%H.%M")"

cd "$(dirname $0)/.."
mkdir -p $NEW_BACKUP_PATH
cp db/csv/*.csv $NEW_BACKUP_PATH