from lib.check.models import Check, Check_Report
from providers.aws.services.efs.efs_client import efs_client


class efs_have_backup_enabled(Check):
    def execute(self):
        findings = []
        for fs in efs_client.filesystems:
            report = Check_Report(self.metadata())
            report.region = fs.region
            report.resource_id = fs.id
            report.resource_arn = ""
            report.status = "PASS"
            report.status_extended = f"EFS {fs.id} has backup enabled"
            if fs.backup_policy == "DISABLED" or fs.backup_policy == "DISABLING":
                report.status = "FAIL"
                report.status_extended = f"EFS {fs.id} does not have backup enabled"

            findings.append(report)

        return findings