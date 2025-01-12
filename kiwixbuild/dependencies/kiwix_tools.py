from .base import (
    Dependency,
    GitClone,
    MesonBuilder)

class KiwixTools(Dependency):
    name = "kiwix-tools"
    force_build = True

    class Source(GitClone):
        git_remote = "https://github.com/kiwix/kiwix-tools.git"
        git_dir = "kiwix-tools"

    class Builder(MesonBuilder):
        dependencies = ["libkiwix"]

        @property
        def configure_option(self):
            if self.buildEnv.platformInfo.static:
                return "-Dstatic-linkage=true"
            return ""
