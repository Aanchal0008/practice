# Login & Sign Up System

A full-stack web application with a responsive frontend and FastAPI backend for user authentication.

## Features

- **User Login** - Authenticate with User ID and password
- **User Registration** - Create new accounts with email and password
- **Responsive Design** - Mobile-friendly layout with gradient background
- **CORS Enabled** - Frontend and backend communication support
- **MySQL Database** - Secure user data storage
- **Client-side Validation** - Password confirmation and field validation
- **Error Handling** - User-friendly error messages
- **Password Matching** - Signup validates password confirmation

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript (Fetch API for HTTP requests)

### Backend
- Python 3
- FastAPI
- Uvicorn (ASGI server)
- MySQL Connector
- Pydantic (data validation)

### Database
- MySQL
- Database: `project`
- Table: `loginData` (userID, email, password)

## Files Included

- `index.html` - Login page
- `signup.html` - User registration page
- `main.py` - FastAPI backend with login/signup endpoints
- `data.py` - Database models and functions
- `.gitignore` - Git ignore file
- `README.md` - This file

## Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server running locally
- pip (Python package manager)

### 1. Install Dependencies
```bash
pip install fastapi uvicorn mysql-connector-python pydantic
```

### 2. Database Setup
The database is automatically created on first run with:
- Database: `project`
- Table: `loginData` with columns (userID, email, password)
- MySQL user: `root` with password: `root`

Update credentials in `data.py` if different.

### 3. Start Backend Server
```bash
uvicorn main:app --reload
```
Backend runs on `http://localhost:8000`

### 4. Serve Frontend
```bash
python -m http.server 8080
```
Frontend runs on `http://localhost:8080`

## API Endpoints

### POST /login
Login with existing account
```json
{
  "userID": "Ashu1023",
  "password": "password123"
}
```

### POST /signup
Create new account
```json
{
  "userID": "Ashu1023",
  "email": "user@example.com",
  "password": "password123"
}
```

## How to Use

1. Start the backend: `uvicorn main:app --reload`
2. Start the frontend: `python -m http.server 8080`
3. Open `http://localhost:8080` in your browser
4. New users: Click "Sign Up here" to create an account
5. Existing users: Enter credentials and click Login

## Project Structure

```
github/
├── main.py          # FastAPI application
├── data.py          # Database models and functions
├── index.html       # Login page
├── signup.html      # Registration page
├── .gitignore       # Git ignore file
└── README.md        # Documentation
```

## Future Enhancements

- Password reset functionality
- Email verification
- Remember me option
- Social media login integration
- JWT token authentication
- Password hashing (bcrypt)
- Input sanitization for SQL injection prevention
- User profile page
- Admin dashboard
- Rate limiting

## Security Notes

⚠️ **Current Implementation** - For development only
- Passwords stored in plain text (use bcrypt in production)
- No SQL injection protection (use parameterized queries)
- No input sanitization
- Credentials hardcoded (use environment variables)

**Production Recommendations:**
- Use hashed passwords (bcrypt/argon2)
- Implement prepared statements to prevent SQL injection
- Use environment variables for credentials
- Add HTTPS/SSL
- Implement JWT tokens
- Add input validation and sanitization
- Rate limiting on endpoints

## Author

Created on January 16, 2026

---

Feel free to customize and enhance this project!