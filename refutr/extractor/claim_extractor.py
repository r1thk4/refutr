from models import CodeFacts, Claim
import spacy

model = spacy.load("en_core_web_sm")

def extract_claims(explanation: str, facts: CodeFacts):    
    doc = model(explanation)
    claims = []
    structural = ["recursive", "recursion", "loop", "iterates"]
    behavioral = ["returns", "outputs", "produces", "computes"]
    type_keywords = ["takes", "accepts", "yields", "parameter"]
    complexity = ["O(", "linear", "quadratic", "constant time"]
   
    for sent in doc.sents:
        if any(token.text in facts.identifiers for token in sent):
            lower = sent.text.lower()
            if any(x in lower for x in structural):
                claim_type = "structural"
            elif any(x in lower for x in behavioral):
                claim_type = "behavioral"
            elif any(x in lower for x in type_keywords):
                claim_type = "type"
            elif any(x in lower for x in complexity):
                claim_type = "complexity"
            else:
                claim_type = None
        
            if claim_type:
                claim = Claim(text= sent.text, claim_type= claim_type, char_span= (sent.start_char, sent.end_char))
                claims.append(claim)
            
    return claims   