#!/usr/bin/env python3

import gitlab
import dotenv
import os


def codeowners_enabled(project):
    try:
        codeowners_filelist = [
            f for f in project.repository_tree(get_all=True) if f["name"] == "CODEOWNERS"
        ]
        return len(codeowners_filelist) != 0
    except gitlab.exceptions.GitlabGetError:
        return True



def main():
    dotenv.load_dotenv()

    gl = gitlab.Gitlab(url=os.getenv("GITLAB_URL"), private_token=os.getenv("TOKEN"))

    group = gl.groups.get(id=os.getenv("GROUP_ID"))
    for p in group.projects.list(include_subgroups=True, get_all=True):
        project = gl.projects.get(p.id, lazy=True)
        if not codeowners_enabled(project):
            print(
                f"{p.namespace['full_path']}/{p.name}"
            )


if __name__ == "__main__":
    main()
