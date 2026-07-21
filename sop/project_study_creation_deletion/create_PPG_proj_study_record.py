#!/usr/bin/env python3

import argparse
import json
import sys
from gen3.submission import Gen3Submission
from gen3.auth import Gen3Auth
from gen3.index import Gen3Index
from gen3.query import Gen3Query
from gen3.metadata import Gen3Metadata
from gen3.file import Gen3File

def create_program(submission, program_name):
    prog_txt = f"""
    {{
        "dbgap_accession_number": "{program_name}",
        "type": "program",
        "name": "{program_name}"
    }}
    """
    prog_json = json.loads(prog_txt)
    print(f"[INFO] Creating program: {program_name}")
    data = submission.create_program(json=prog_json)
    print(f"[SUCCESS] Program created:\n{data}")


def create_project(submission, program_name, project_code, description, contact_name, institution, email, availability="Restricted"):
    proj_txt = f"""
    {{
        "availability_type": "{availability}",
        "code": "{project_code}",
        "dbgap_accession_number": "{project_code}",
        "type": "project",
        "contact_name": "{contact_name}",
        "institution": "{institution}",
        "description": "{description}",
        "email_address": "{email}",
        "telephone_number": ""
    }}
    """
    proj_json = json.loads(proj_txt)
    print(f"[INFO] Creating project {project_code} under program {program_name}")
    data = submission.create_project(program=program_name, json=proj_json)
    print(f"[SUCCESS] Project created:\n{data}")

    """
    Automatically create a core_metadata_collection record.

    Defaults:
      title := project_code   (if not provided)
      submitter_id := project_code  (if not provided)
    """
    cmc_txt = f"""
    {{
        "creator": "{contact_name}",
        "description": "{description}",
        "submitter_id": "{project_code}",
        "title": "{project_code}",
        "project_id": "{program_name}-{project_code}",
        "type": "core_metadata_collection",
        "projects": [{{"code": "{project_code}"}}]
    }}
    """
    cmc_json = json.loads(cmc_txt)
    print(f"[INFO] Creating CMC for {program_name}-{project_code}")
    data = submission.submit_record(program=program_name, project=project_code, json=cmc_json)
    print(f"[SUCCESS] CMC created:\n{data}")


def create_study(
    submission,
    program_name,
    project_code,
    experiment,
    organism,
    projects,
    provenance,
    study_description,
    study_design,
    study_title,
    study_type,
    submitter_id,
    node_type="study"
):
    study_txt = f"""
    {{
        "experimental_setting": "{experiment}",
        "organism": "{organism}",
        "projects": [{{"code": "{projects}"}}],        
        "study_description": "{study_description}",
        "study_design": "{study_design}",
        "study_title": "{study_title}",
        "study_type": "{study_type}",
        "submitter_id": "{submitter_id}",
        "type": "{node_type}"
    }}
    """
    study_json = json.loads(study_txt)

    print(f"[INFO] Creating study {submitter_id} under project {project_code}")

    data = submission.submit_record(
        program=program_name,
        project=project_code,
        json=study_json
    )

    print(f"[SUCCESS] Study created:\n{data}")

def main():
    parser = argparse.ArgumentParser(description="Create Gen3 Records")

    parser.add_argument("--cred", required=True,
                        help="Path to Gen3 credentials JSON")

    parser.add_argument("--api", required=True,
                        help="Gen3 API URL (e.g., https://dev.toxdatacommons.com)")

    parser.add_argument("--program", required=True,
                        help="Program name")

    parser.add_argument("--project_code", required=True,
                        help="Project code (e.g., TDC0002)")

    parser.add_argument("--description", required=True,
                        help="Project description")

    parser.add_argument("--contact_name", required=True,
                        help="Project contact name")

    parser.add_argument("--institution", required=True,
                        help="Institution")

    parser.add_argument("--email", required=True,
                        help="Contact email")

    parser.add_argument("--experiment", required=True,
                        help="Experiment")

    parser.add_argument("--organism", required=True,
                        help="Organism")

    parser.add_argument("--projects", required=True,
                        help="Projects")

    parser.add_argument("--provenance", required=True,
                        help="Provenance")

    parser.add_argument("--study_description", required=True,
                        help="Study description")

    parser.add_argument("--study_design", required=True,
                        help="Study design")

    parser.add_argument("--study_title", required=True,
                        help="Study title")

    parser.add_argument("--study_type", required=True,
                        help="Study type")

    parser.add_argument("--submitter_id", required=True,
                        help="Study submitter ID")

    parser.add_argument("--availability", default="Restricted",
                        help="Availability type (default: Restricted)")

    args = parser.parse_args()


    # Authenticate
    print("[INFO] Authenticating...")
    auth = Gen3Auth(args.api, refresh_file=args.cred)
    sub = Gen3Submission(args.api, auth)

    # Program creation
    create_program(sub, args.program)

    # Project creation
    create_project(
        sub,
        args.program,
        args.project_code,
        args.description,
        args.contact_name,
        args.institution,
        args.email,
        args.availability
    )

    create_study(
       sub,
       args.program,
       args.project_code,
       args.experiment,
       args.organism,
       args.projects,
       args.provenance,
       args.study_description,
       args.study_design,
       args.study_title,
       args.study_type,
       args.submitter_id
   )

if __name__ == "__main__":
    main()

