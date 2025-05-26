from typing import Dict, Any # No need for 'cast' if you trust the input or refine the type

def calculate_conversion(rates: Dict[str, float], from_currency: str, to_currency: str, amount: float) -> Dict[str, Any]:
    if from_currency not in rates or to_currency not in rates:
        return {"result": "error", "message": "Unsupported currency code."}
    
    from_rate = rates[from_currency] 
    to_rate = rates[to_currency] 

    conversion_rate = to_rate / from_rate
    conversion_result = amount * conversion_rate

    return {
        "base_code": from_currency,
        "target_code": to_currency,
        "conversion_rate": conversion_rate,
        "conversion_result": conversion_result
    }