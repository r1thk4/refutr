from dataclasses import dataclass

@dataclass
class CodeFacts:
    recursive: set[str]
    loops: set[str]
    mutating_functions: set[str]
    identifiers: set[str]
    return_type: dict[str, str]