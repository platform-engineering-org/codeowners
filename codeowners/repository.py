class Repository:
    path: str
    codeowners_file_exists: bool

    def __init__(self, path, **kwargs):
        self.path = path
        self.codeowners_file_exists = kwargs.get(
            "codeowners_file_exists", False
        )

    def __str__(self) -> str:
        return ", ".join(
            [
                f"{self.path}, {self.codeowners_file_exists}",
            ]
        )
