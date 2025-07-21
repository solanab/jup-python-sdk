from typing import Any

from pydantic import BaseModel
from pydantic.alias_generators import to_camel


class UltraExecuteRequest(BaseModel):
    signed_transaction: str
    request_id: str

    def to_dict(self) -> dict[str, Any]:
        params = self.model_dump(exclude_none=True)

        camel_case_params = {to_camel(key): value for key, value in params.items()}

        return camel_case_params
