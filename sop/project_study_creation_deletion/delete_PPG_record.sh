#!/bin/bash

python create_PPG_proj_study_record.py \
  --cred credentials.json \
  --api https://dev.pvatppgmsu.com \
  --program LTTEST \
  --project_code PPG_0001 \
  --description "Cohort 01 - 24 week Dahl S and SD males" \
  --availability Restricted \
  --projects "PPG_0001" \
  --contact_name "Leah Terrian" \
  --institution "MSU" \
  --email "terrianl@msu.edu" \
  --provenance "Not provided" \
  --organism "Rattus norvegicus" \
  --experiment "in vivo" \
  --study_type "Not provided" \
  --study_description "Cohort 01 - 24 week Dahl S and SD males - Main" \
  --study_design "Not applicable" \
  --study_title "Main" \
  --submitter_id "PPG_0001_Main"