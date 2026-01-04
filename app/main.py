from fastapi import FastAPI, HTTPException, status
from app.schemas import ClaimCreate, ClaimResponse, ClaimUpdate
from app.service import ClaimService
from app.repository import ClaimRepository
from datetime import datetime

app = FastAPI(
    title="Insurance Claims API",
    description="A FastAPI project to process insurance claims",
    version="0.1.0"
)

# Initialize repository and service
repository = ClaimRepository()
service = ClaimService()


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Welcome to Insurance Claims API"}


@app.post("/claims", response_model=ClaimResponse, status_code=status.HTTP_201_CREATED)
async def create_claim(claim_data: ClaimCreate):
    """
    Create a new insurance claim.
    
    Args:
        claim_data: The claim data from the request body
        
    Returns:
        ClaimResponse: The created claim
    """
    try:
        claim = service.create_claim(
            claim_type=claim_data.claim_type,
            amount=claim_data.amount,
            status=claim_data.status,
            created_at=claim_data.created_at,
            created_by=claim_data.created_by
        )
        repository.create(claim)
        return ClaimResponse(
            id=claim.id,
            claim_type=claim.claim_type,
            amount=claim.amount,
            status=claim.status,
            created_at=claim.created_at,
            created_by=claim.created_by
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create claim: {str(e)}"
        )


@app.get("/claims", response_model=list[ClaimResponse])
async def get_all_claims():
    """
    Retrieve all insurance claims.
    
    Returns:
        List[ClaimResponse]: A list of all claims
    """
    claims = service.get_all_claims()
    return [
        ClaimResponse(
            id=claim.id,
            claim_type=claim.claim_type,
            amount=claim.amount,
            status=claim.status,
            created_at=claim.created_at,
            created_by=claim.created_by
        )
        for claim in claims
    ]


@app.get("/claims/{claim_id}", response_model=ClaimResponse)
async def get_claim(claim_id: int):
    """
    Retrieve a specific claim by its ID.
    
    Args:
        claim_id: The ID of the claim to retrieve
        
    Returns:
        ClaimResponse: The claim object
        
    Raises:
        HTTPException: If the claim is not found
    """
    claim = service.get_claim(claim_id)
    if not claim:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Claim with ID {claim_id} not found"
        )
    return ClaimResponse(
        id=claim.id,
        claim_type=claim.claim_type,
        amount=claim.amount,
        status=claim.status,
        created_at=claim.created_at,
        created_by=claim.created_by
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

