from fastapi import APIRouter, Depends, Path, status, Response
from schemas.user import UserProfileResponse
from core.exceptions import UnauthorizedException, ForbiddenException

router = APIRouter()

# Stubs for role check and user info
def get_current_user():
    # Return None if not authenticated
    # Pretend user dict: {"id": 2, "username": "jane", "email": "jane@example.com", "role": "user"}
    # For admin: {"id": 1, "username": "admin", "email": "admin@example.com", "role": "admin"}
    # This would be filled in by actual dependencies
    return None  # Candidate must replace with real user stub

def require_admin(user=Depends(get_current_user)):
    if user is None:
        raise UnauthorizedException("Not authenticated")
    if user.get("role") != "admin":
        raise ForbiddenException("Admin role required")
    return user

# --- Endpoint 1 ---
@router.get("/me", response_model=UserProfileResponse)
def get_me(current_user=Depends(get_current_user)):
    if current_user is None:
        raise UnauthorizedException("Not authenticated")
    return UserProfileResponse(
        id=current_user["id"],
        username=current_user["username"],
        email=current_user["email"],
        role=current_user["role"]
    )

# --- Endpoint 2 ---
@router.get("/{user_id}", response_model=UserProfileResponse)
def get_user_profile(user_id: int = Path(..., gt=0),
                     admin_user=Depends(require_admin)):
    # Just some sample stub users
    stubbed_users = [
        {"id": 1, "username": "admin", "email": "admin@example.com", "role": "admin"},
        {"id": 2, "username": "jane", "email": "jane@example.com", "role": "user"},
        {"id": 3, "username": "bob", "email": "bob@example.com", "role": "user"},
    ]
    user = next((u for u in stubbed_users if u["id"] == user_id), None)
    if not user:
        return Response(content="User not found", status_code=status.HTTP_404_NOT_FOUND)
    return UserProfileResponse(
        id=user["id"],
        username=user["username"],
        email=user["email"],
        role=user["role"]
    )
