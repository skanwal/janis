from janis_core import (
    ToolInput,
    ToolOutput,
    Directory,
    File,
    CommandTool,
    Stdout,
)
from janis_core import *


class RunFolderCheck(CommandTool):
    @staticmethod
    def tool():
        return "runFolderCheck"

    def env_vars(self):
        return {"DEPLOY_ENV": "prod"}

    @staticmethod
    def base_command():
        return ["bash", "/scripts/runfolder-check.sh"]

    def inputs(self):
        return [
            ToolInput(
                "input_folder",
                Directory,
                position=1,
                doc="The input folder with bcls and associated metadata",
            )
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                File,
                glob=WildcardSelector("*"),
                )
            ]

    @staticmethod
    def container():
        return "umccr/pipeline"

    @staticmethod
    def version():
        return "v1"

if __name__ == "__main__":
    print(RunFolderCheck().translate("cwl"))
