from pydantic import BaseModel

class HelpResponse(BaseModel):
    result: str
    description: str
    usage_example: str
    endpoints: dict
    documentation: str
    terms_of_use: str
    supported_currencies: List[str]