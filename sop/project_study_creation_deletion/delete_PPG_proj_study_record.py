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

def delete_project(submission, program, project):
    print(f"[INFO] Deleting project {project} under program {program}")
    data = submission.delete_project(program=program, project=project)
    print(f"[SUCCESS] Project deleted:\n{data}")

def delete_record(submission, program, project, uuid):
    print(f"[INFO] Deleting record {uuid} under project {project}")
    data = submission.delete_record(program=program, project=project, uuid=uuid)
    print(f"[SUCCESS] Record deleted:\n{data}")

def main():
    parser = argparse.ArgumentParser(description="Delete Gen3 Project and Study Records")

    parser.add_argument("--cred", required=True,
                        help="Path to Gen3 credentials JSON")

    parser.add_argument("--api", required=True,
                        help="Gen3 API URL (e.g., https://dev.toxdatacommons.com)")

    parser.add_argument("--program", required=True,
                        help="Program name")
    
    parser.add_argument("--project", required=True,
                        help="Project name")

    parser.add_argument("--uuid", required=False,
                        help="Record UUID")

    args = parser.parse_args()


    # Authenticate
    print("[INFO] Authenticating...")
    auth = Gen3Auth(args.api, refresh_file=args.cred)
    sub = Gen3Submission(args.api, auth)

    # Project deletion
    delete_project(sub, args.program, args.project)

    if args.uuid:
        # Record deletion
        delete_record(sub, args.program, args.project, args.uuid)

if __name__ == "__main__":
    main()

