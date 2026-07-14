#!/bin/bash

python create_gen3_proj_study_PPG.py \
  --cred credentials.json \
  --api https://dev.pvatppgmsu.com \
  --program LTTEST \
  --project_code LTTEST0001 \
  --availability Restricted \
  --projects "LTTEST0001" \
  --contact_name "Leah Terrian" \
  --institution "MSU" \
  --email "terrianl@msu.edu" \
  --provenance "Not provided" \
  --organism "Rattus norvegicus" \
  --description "Test Project" \
  --experiment "Not provided" \
  --study_type "Not provided" \
  --study_description "Nuclei Isolation of WAT" \
  --study_design "Not provided" \
  --study_title "Nuclei Isolation of WAT" \
  --submitter_id "Nuclei_Isolation"