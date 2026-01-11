def policy_check(role, resource):
    policies = {
        "admin": ["admin", "dashboard", "guest"],
        "employee": ["dashboard", "guest"],
        "guest": ["guest"]
    }
    return resource in policies.get(role, [])
