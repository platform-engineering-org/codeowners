import os

import dotenv
import gitlab


def codeowners_enabled(project):
    try:
        codeowners_filelist = [
            f
            for f in project.repository_tree(recursive=True, all=True)
            if f["name"] == "CODEOWNERS"
        ]
        return len(codeowners_filelist) != 0
    except gitlab.exceptions.GitlabGetError:
        return True


def extract():
    dotenv.load_dotenv()

    gl = gitlab.Gitlab(
        url=os.getenv("GITLAB_URL"), private_token=os.getenv("TOKEN")
    )

    group = gl.groups.get(id=os.getenv("GROUP_ID"))
    for p in group.projects.list(
        include_subgroups=True, archived=False, get_all=True
    ):
        project = gl.projects.get(p.id, lazy=True)
        yield {
            "path": p.path_with_namespace,
            "name": p.name,
            "codeowners_file_exists": codeowners_enabled(project),
        }
