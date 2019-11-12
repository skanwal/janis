from janis_core import *

class SampleSheetCheck(CommandTool):
    @staticmethod
    def tool():
        return "sampelSheetCheck"

    def env_vars(self):
        return {"DEPLOY_ENV": "prod"}

    @staticmethod
    def base_command():
        return ["python", "/scripts/samplesheet-check.py"]

    def inputs(self):
        return [
            ToolInput(
                "samplesheet",
                File,
                position=1,
                localise_file=True,
                doc="The input samplesheet with sample details",
            ),
            ToolInput(
                "config",
                Directory,
                position=2,
                doc="The config file directory for googlespread sheets"
            )

        ]

    def outputs(self):
        return [
            ToolOutput(
                "split_samplesheets",
                Array(File),
                glob=WildcardSelector("*[!.csv]"),
                )
            ]

    @staticmethod
    def container():
        return "umccr/pipeline"

    @staticmethod
    def version():
        return "v1"

if __name__ == "__main__":
    print(SampleSheetCheck().translate("cwl"))
