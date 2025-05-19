_context_store = {}

def store_context(user_id: str, context: dict):
    _context_store[user_id] = context

def get_context(user_id: str):
    return _context_store.get(user_id, {})
