from janis import *

class Bcl2Fastq(CommandTool):
    
    def tool(self):
        return "bcl2Fastq

    def env_vars(self):
        return {"DEPLOY_ENV": "prod"}

    def base_command(self):
        return []

    def inputs(self):
        return [
            ToolInput(
                "bcls",
                Directory,
                position=1,
                prefix="-R",
                doc="Folder that contains bcl data and related files"
            ),
            ToolOutput(
                "output_folder",
                Directory,
                position=3,
                prefix="-o",
                localise_file=True,
                doc="The output directory",
            ),
            samplesheet(
                "samplesheet_bcl2fastq",
                File,
                prefix="--sample-sheet",
                doc="The samplesheet with sample information"
            )

        ]

    def outputs(self):
        return [
            ToolOutput(
                "samplesheets_fastq",
                Array(File),
                glob=WildcardSelector("*"),
                )
            ]

    def container(self):
        return "umccr/bcl2fastq"

    def version(self):
        return "v1"

if __name__ == "__main__":
    print(Bcl2Fastq().translate("cwl"))
