# Advanced Password Generator

A modern desktop application for generating secure and customizable passwords with a user-friendly interface.

## Features

### Password Generation
- Adjustable password length (4-100 characters)
- Customizable character sets:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!@#$%^&*)
- Option to exclude similar characters (1,l,I,0,O)
- Minimum requirements settings:
  - Set minimum number of digits
  - Set minimum number of special characters

### User Interface
- Clean and intuitive tabbed interface
- Real-time password length adjustment via slider or text input
- One-click copy to clipboard functionality
- Password history tracking
- Error handling with informative messages

### Password History
- Saves generated passwords with timestamps
- Persistent storage between sessions
- View complete history in a dedicated tab
- Organized table view with password and generation date

## Getting Started

### Prerequisites
- Python 3.12 or later
- Windows 10/11

### Installation Methods

#### Method 1: Run Python Script
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python password_generator.py
   ```

#### Method 2: Build Executable
1. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

2. Optional: Create application icon
   ```bash
   python create_icon.py
   ```

3. Build executable
   ```bash
   python build.py
   ```

4. Find the executable in `dist/Password_Generator.exe`

## Usage Guide

### Generating Passwords
1. Set password length using slider or input box
2. Select desired character types
3. Configure minimum requirements (optional)
4. Click "Generate Password"

### Managing Passwords
- Click "Copy to Clipboard" to copy password
- Click "Save Password" to add to history
- View saved passwords in History tab

## Project Structure

## Technical Details

### Built With
- Python 3.12
- tkinter for GUI
- JSON for data persistence
- PyInstaller for executable creation

### Security Features
- Cryptographically secure random generation
- Configurable complexity requirements
- Local-only storage
- No plain text password storage

## Privacy & Security
- All data stored locally
- No internet connection required
- No data collection or transmission
- No external dependencies for core functionality

## Development

### Setting Up Development Environment
1. Fork the repository
2. Create feature branch
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make changes
4. Submit pull request

### File Guidelines
Files to include in repository:
- ✅ password_generator.py
- ✅ build.py
- ✅ create_icon.py
- ✅ requirements.txt
- ✅ README.md
- ✅ LICENSE
- ✅ .gitignore

Do not commit:
- ❌ dist/ directory
- ❌ build/ directory
- ❌ __pycache__/
- ❌ .spec files
- ❌ password_history.json

## Support
For issues, questions, or suggestions:
1. Check existing GitHub issues
2. Create new issue if needed
3. Include detailed description and steps to reproduce

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with security and usability in mind
- Designed for both novice and advanced users
- Community contributions welcome 
