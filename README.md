# Notination - FastAPI Notes App

A simple and elegant note-taking web application built with FastAPI and MongoDB. Create, store, and manage your notes with priority levels.

## Features

- ✅ Create notes with title and description
- ✅ Mark notes as high priority
- ✅ View all your notes on a beautiful dashboard
- ✅ MongoDB integration for persistent storage
- ✅ Responsive Bootstrap UI
- ✅ Environment variables for secure credential management

## Tech Stack

- **Backend**: FastAPI
- **Database**: MongoDB
- **Frontend**: Jinja2 Templates + Bootstrap 5
- **Package Manager**: pip
- **Python Version**: 3.8+

## Prerequisites

- Python 3.8 or higher
- MongoDB Atlas account (or local MongoDB instance)
- pip (Python package manager)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-app
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   **On Windows:**
   ```bash
   .\venv\Scripts\activate
   ```
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup environment variables**
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Update `.env` with your MongoDB connection URL
   ```
   MONGODB_URL=mongodb+srv://your-username:your-password@your-cluster.mongodb.net/notes
   ```

## Running the Application

Start the FastAPI development server:

```bash
uvicorn index:app --reload
```

Or use the Python executable from virtual environment:

```bash
.\venv\Scripts\python.exe -m uvicorn index:app --reload
```

The app will be available at `http://127.0.0.1:8000/`

## Project Structure

```
fastapi-app/
├── main.py                 # Main application entry point
├── index.py               # Alternative entry point
├── config/
│   └── db.py              # Database configuration
├── models/
│   └── note.py            # Note data model
├── routes/
│   └── note.py            # API routes for notes
├── schemas/
│   └── note.py            # Data schemas and validators
├── templates/
│   └── index.html         # Main HTML template
├── static/
│   └── style.css          # CSS styles
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (git ignored)
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## API Endpoints

### GET `/`
Displays the home page with all notes and the note creation form.

### POST `/`
Creates a new note with the provided title, description, and priority level.

## Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGODB_URL` | MongoDB connection string | `mongodb+srv://user:pass@cluster.mongodb.net/notes` |

## Database Schema

Each note document in MongoDB contains:
```json
{
  "_id": "ObjectId",
  "title": "string",
  "description": "string",
  "highpriority": "boolean"
}
```

## Development

### Adding a New Route

1. Create or modify files in the `routes/` directory
2. Update `config/db.py` if needed for database queries
3. Update `main.py` or `index.py` to include the new router

### Dependencies

All dependencies are listed in `requirements.txt`. To add a new dependency:
```bash
pip install package-name
pip freeze > requirements.txt
```

## Troubleshooting

### `ModuleNotFoundError: No module named 'dotenv'`
- Make sure you've activated the virtual environment
- Install dependencies: `pip install -r requirements.txt`

### MongoDB Connection Error
- Check that your `MONGODB_URL` in `.env` is correct
- Ensure your MongoDB cluster allows connections from your IP address
- Test the connection string in MongoDB Atlas

## Security

- Never commit `.env` file to version control
- Keep your MongoDB credentials secure
- Use strong passwords for MongoDB accounts
- Consider using VPN/whitelist for MongoDB IP access

## License

This project is open source and available under the MIT License.

## Support

For issues or questions, please open an issue on the repository.

---

Happy note-taking! 📝✨
