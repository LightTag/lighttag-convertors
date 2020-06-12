import json
from lighttag_to_adm import save_lighttag_job_to_adm
#Load your LightTag data
data = json.load(open('/tmp/mixed_sample1_annotations.json'))
save_lighttag_job_to_adm(data,
                         out_path="/tmp/nadav11", #Where to save it
                         allow_overwrite=True, #Allow overwriting a job
                         reviewed_only=False, # Only use reviewed annotations
                         exclude_attributes=False
                        )