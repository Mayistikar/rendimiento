from fastapi import APIRouter, HTTPException
from application.RawDataService import IRawDataService
from domain.RawData import RawData
from datetime import datetime

class Routes:
    def __init__(self, raw_data_service: IRawDataService):
        self.router = APIRouter()
        self.router.add_api_route("/raw-data/", self.send_raw_data, methods=["POST"], response_model=dict)
        self.raw_data_service = raw_data_service

    async def send_raw_data(self):
        try:
            raw_data = RawData(
                image="image",
                diagnosis="diagnosis",
                report="report",
                body_part="body_part",
                modality="modality",
                age="age",
                sex="sex",
                ethnicity="ethnicity",
                symptoms="symptoms",
                clinical_history="clinical_history",
                findings="findings",
                impression="impression",
                recommendation="recommendation",
                indication="indication",
                comparison="comparison",
                technique="technique",
                no_finding="no_finding",
                normal="normal",
                abnormal="abnormal",
                uncertain="uncertain",
                other="other",
                unknown="unknown",
                code="code",
                diagnosis_date=datetime.now()
            )

            return self.raw_data_service.send_raw_data(raw_data)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")
