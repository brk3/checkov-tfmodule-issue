from checkov.terraform.checks.module.base_module_check import BaseModuleCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class ModuleSourceDomainCheck(BaseModuleCheck):
    def __init__(self) -> None:
        name = "I will never run with a tfplan :("
        id = "FOO"
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories)

    def scan_module_conf(self, conf):
        return CheckResult.FAILED

check = ModuleSourceDomainCheck()
