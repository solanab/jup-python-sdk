from typing import Optional

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class UltraOrderRequest(BaseModel):
    input_mint: str
    output_mint: str
    amount: int
    taker: Optional[str] = None

    def to_dict(self):
        params = self.model_dump(exclude_none=True)

        camel_case_params = {to_camel(key): value for key, value in params.items()}

        return camel_case_params
