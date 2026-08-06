# SOP: Create New Project / Study

## Purpose

Describe the steps to create a new project or study record for the PVAT PPG Data Commons, assign user access, and notify the requestor.


## Files & links

- Project request form: https://docs.google.com/spreadsheets/d/1YfblTd1D4TcTnaanERUdWzvLSf3gD_SIfWa9iDpEJ-g/edit?usp=drive_link
- Creation script: `project_study_creation_deletion/create_PPG_record.sh`
- Access SOP: `Data_Commons/gen3-gitops/sop/user-access-permissions-update.md`
- Notification template: "PVAT PPG Data Commons New Project/Study Created!"


## Procedure

1. Review the project/study request
	- Open the project request form (link above) and confirm the submitter's details and required fields.

2. Create the project/study record
	- Edit the `project_study_creation_deletion/create_PPG_record_active.sh` script so the variables match the form responses.
	- Run the script. Example:

```bash
cd msu-gen3-dictionaries/sop/project_study_creation_deletion
bash ./create_PPG_record_active.sh
```

3. Assign user access
	- Follow the access SOP: `Data_Commons/gen3-gitops/sop/user-access-permissions-update.md`.
	- Edit the appropriate `fence.yaml` for the namespace, commit the change, push to the repo, run the `update-useryaml` job in Rancher, and redeploy the fence-related deployments as described in that SOP.

4. Notify the requestor
	- Edit and send the "PVAT PPG Data Commons New Project/Study Created!" template email to the submitter. Include the namespace, program/project identifiers, any access granted, and any next steps.