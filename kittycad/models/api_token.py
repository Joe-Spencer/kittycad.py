import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from ..models.api_token_uuid import ApiTokenUuid
from ..models.uuid import Uuid


class ApiToken(BaseModel):
    """An API token.

    These are used to authenticate users with Bearer authentication."""

    created_at: datetime.datetime

    id: Uuid

    is_valid: bool

    label: Optional[str] = None

    token: ApiTokenUuid

    updated_at: datetime.datetime

    user_id: Uuid

    model_config = ConfigDict(protected_namespaces=())
