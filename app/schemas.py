from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ClaimCreate(BaseModel):
    """Schema for creating a new claim."""
    claim_type: str = Field(..., description="Type of the claim")
    amount: float = Field(..., gt=0, description="Amount of the claim")
    status: str = Field(..., description="Status of the claim")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")


class ClaimResponse(BaseModel):
    """Schema for claim response."""
    id: int
    claim_type: str
    amount: float
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class ClaimUpdate(BaseModel):
    """Schema for updating a claim."""
    claim_type: Optional[str] = None
    amount: Optional[float] = Field(None, gt=0)
    status: Optional[str] = None

