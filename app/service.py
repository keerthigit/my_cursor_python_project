from app.models import Claim

# ClaimService class to manage claims.
class ClaimService:
    def __init__(self):
        self._claims = {}
        self._next_id = 1
    
    def create_claim(self, claim_type, amount, status, created_at):
        """
        Create a new claim and store it.
        
        Args:
            claim_type: Type of the claim
            amount: Amount of the claim
            status: Status of the claim
            created_at: Creation timestamp
            
        Returns:
            Claim: The created claim object
        """
        claim_id = self._next_id
        self._next_id += 1
        
        claim = Claim(
            id=claim_id,
            claim_type=claim_type,
            amount=amount,
            status=status,
            created_at=created_at
        )
        
        self._claims[claim_id] = claim
        return claim
    
    def get_claim(self, claim_id):
        """
        Retrieve a claim by its ID.
        
        Args:
            claim_id: The ID of the claim to retrieve
            
        Returns:
            Claim: The claim object if found, None otherwise
        """
        return self._claims.get(claim_id)
    
    def get_all_claims(self):
        """
        Retrieve all claims.
        
        Returns:
            list: A list of all claim objects
        """
        return list(self._claims.values())

