from database.connection import sessionlocal
from schemas import UserCreate
from services import create_user, get_user_by_email, verify_password

db = sessionlocal()

try:
    user_data = UserCreate(
        name="Test Physio",
        email="test@example.com",
        password="Test1234",
        role="Physio"
    )

    new_user = create_user(db, user_data)

    print("User created successfully")
    print("ID:", new_user.id)
    print("Name:", new_user.name)
    print("Email:", new_user.email)
    print("Role:", new_user.role)
    print("Stored password hash:", new_user.hashed_password)

    # Check if user exists in DB
    user_from_db = get_user_by_email(db, "test@example.com")
    print("Found user:", user_from_db.email)

    # Check password verification
    is_valid = verify_password("Test1234", user_from_db.hashed_password)
    print("Password valid:", is_valid)

finally:
    db.close()