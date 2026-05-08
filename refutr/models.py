from dataclasses import dataclass
from enum import Enum

class Label(str, Enum):
    SUPPORTED = "supported"
    REFUTED = "refuted"
    UNVERIFIABLE = "unverifiable"
    
class Strategy(str, Enum):
    AST = "ast"
    RAG = "rag"

@dataclass
class Claim:
    text: str
    claim_type: str
    char_span: tuple[int, int]

@dataclass
class Verdict:
    claim: Claim
    label: Label
    confidence: float
    strategy: Strategy
    evidence: str

@dataclass
class VerificationResult:
    hallucination_score: float
    severity: str
    verdicts: list[Verdict] = field(default_factory=list)

@dataclass
class CodeFacts:
    recursive: set[str]
    loops: set[str]
    mutating_functions: set[str]
    identifiers: set[str]
    return_type: dict[str, str]