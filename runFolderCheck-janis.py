from janis_core import (
    ToolInput,
    ToolOutput,
    String,
    InputSelector,
    Filename,
    ToolMetadata,
    CaptureType
)

class runFolderCheckBase():
    def env_vars(self):
        return {
            "DEPLOY_ENV": "prod"
        }

    def base_command():
        return ["bash", "/scripts/runfolder-check.sh"]

    def inputs(self):
        return [
            ToolInput("input_folder", InputFolder, position=1, doc="The input folder with bcls and associated metadata"),
        ]

    def outputs(self):
        return [
            ToolOutput("out", LogOut),
        ]