import gitlab
import dotenv
import os

import repository


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
        yield (
            repository.Repository(
                path=p.path_with_namespace,
                codeowners_file_exists=codeowners_enabled(project),
            )
        )
