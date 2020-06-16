import json
from lighttag_to_adm import save_lighttag_job_to_adm
from configuration import ConfigurationUtil


if __name__ == "__main__":

    config = ConfigurationUtil.get_configuration()

    data = json.load(open('/tmp/english-persons-corrected_annotations.json'))
    save_lighttag_job_to_adm(data,
                             out_path="/tmp/nadav12",  # Where to save it
                             allow_overwrite=True,  # A llow overwriting a job
                             reviewed_only=False,  # Only use reviewed annotations
                             exclude_attributes=False)
