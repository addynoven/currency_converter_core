from typing import Any, Dict, List
from pydantic import BaseModel

class HelpResponse(BaseModel):
    result: str
    description: str
    usage_example: str
    endpoints: Dict[str, Any]
    documentation: str
    terms_of_use: str
    supported_currencies: List[str]