from models import VerificationResult

def verify(code: str, explanation: str):
    return VerificationResult(
        hallucination_score=0.0,
        severity="none"
    )