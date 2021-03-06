# Stubs for galaxy.tools.deps.requirements (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Dict, List, Optional

DEFAULT_REQUIREMENT_TYPE = ...  # type: str
DEFAULT_REQUIREMENT_VERSION = ...  # type: Any

class ToolRequirement:
    name = ...  # type: Any
    type = ...  # type: Any
    version = ...  # type: Any
    specs = ...  # type: Any
    def __init__(self, name: Optional[Any] = ..., type: Optional[Any] = ..., version: Optional[Any] = ..., specs: Any = ...) -> None: ...
    def to_dict(self) -> Dict[str, Any]: ...
    def copy(self): ...
    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> ToolRequirement: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class RequirementSpecification:
    uri = ...  # type: Any
    version = ...  # type: Any
    def __init__(self, uri, version: Optional[Any] = ...) -> None: ...
    @property
    def specifies_version(self): ...
    @property
    def short_name(self): ...
    def to_dict(self): ...
    @staticmethod
    def from_dict(dict: Dict[str, Any]) -> ToolRequirements: ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

class ToolRequirements:
    tool_requirements = ...  # type: Any
    def __init__(self, tool_requirements: Optional[Any] = ...) -> None: ...
    @staticmethod
    def from_list(requirements: List[ToolRequirement]) -> ToolRequirements: ...
    @property
    def resolvable(self): ...
    @property
    def packages(self): ...
    def to_list(self) -> List[ToolRequirement]: ...
    def append(self, requirement): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __iter__(self): ...
    def __getitem__(self, ii): ...
    def __len__(self): ...
    def __hash__(self): ...

class ToolRequirementsException(Exception): ...

DEFAULT_CONTAINER_TYPE = ...  # type: str
DEFAULT_CONTAINER_RESOLVE_DEPENDENCIES = ...  # type: bool
DEFAULT_CONTAINER_SHELL = ...  # type: str

class ContainerDescription:
    identifier = ...  # type: Any
    type = ...  # type: Any
    resolve_dependencies = ...  # type: Any
    shell = ...  # type: Any
    def __init__(self, identifier: Optional[Any] = ..., type: Any = ..., resolve_dependencies: Any = ..., shell: Any = ...) -> None: ...
    def to_dict(self): ...
    @staticmethod
    def from_dict(dict): ...

def parse_requirements_from_dict(root_dict): ...
def parse_requirements_from_xml(xml_root): ...
def container_from_element(container_elem): ...
