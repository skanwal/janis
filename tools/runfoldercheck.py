from janis_core import *

class RunFolderCheck(CommandTool):
    def tool(self):
        return "runFolderCheck"

    def env_vars(self):
        return {"DEPLOY_ENV": "prod"}

    def base_command(self):
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

    def container(self):
        return "umccr/pipeline"

    def version(self):
        return "v1"

if __name__ == "__main__":
    print(RunFolderCheck().translate("cwl"))
