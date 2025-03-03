from dataclasses import dataclass
from datetime import datetime

@dataclass
class RawData:
    image: str
    diagnosis: str
    report: str
    body_part: str
    modality: str
    age: str
    sex: str
    ethnicity: str
    symptoms: str
    clinical_history: str
    findings: str
    impression: str
    recommendation: str
    indication: str
    comparison: str
    technique: str
    no_finding: str
    normal: str
    abnormal: str
    uncertain: str
    other: str
    unknown: str
    code: str
    diagnosis_date: datetime