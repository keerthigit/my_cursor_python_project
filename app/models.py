class Claim:
    def __init__(self, id, claim_type, amount, status, created_at):
        self.id = id
        self.claim_type = claim_type
        self.amount = amount
        self.status = status
        self.created_at = created_at
