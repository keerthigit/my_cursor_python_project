from app.models import Claim
from typing import Dict, Optional, List


class ClaimRepository:
    """Repository class for managing claim data persistence."""
    
    def __init__(self):
        self._claims: Dict[int, Claim] = {}
        self._next_id = 1
    
    def create(self, claim: Claim) -> Claim:
        """
        Save a claim to the repository.
        
        Args:
            claim: The claim object to save
            
        Returns:
            Claim: The saved claim object
        """
        self._claims[claim.id] = claim
        return claim
    
    def get_by_id(self, claim_id: int) -> Optional[Claim]:
        """
        Retrieve a claim by its ID.
        
        Args:
            claim_id: The ID of the claim to retrieve
            
        Returns:
            Claim: The claim object if found, None otherwise
        """
        return self._claims.get(claim_id)
    
    def get_all(self) -> List[Claim]:
        """
        Retrieve all claims.
        
        Returns:
            List[Claim]: A list of all claim objects
        """
        return list(self._claims.values())
    
    def update(self, claim_id: int, claim: Claim) -> Optional[Claim]:
        """
        Update an existing claim.
        
        Args:
            claim_id: The ID of the claim to update
            claim: The updated claim object
            
        Returns:
            Claim: The updated claim object if found, None otherwise
        """
        if claim_id in self._claims:
            self._claims[claim_id] = claim
            return claim
        return None
    
    def delete(self, claim_id: int) -> bool:
        """
        Delete a claim by its ID.
        
        Args:
            claim_id: The ID of the claim to delete
            
        Returns:
            bool: True if the claim was deleted, False otherwise
        """
        if claim_id in self._claims:
            del self._claims[claim_id]
            return True
        return False
    
    def get_next_id(self) -> int:
        """
        Get the next available ID for a new claim.
        
        Returns:
            int: The next available ID
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id

