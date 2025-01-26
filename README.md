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

## Installation

1. Download the latest release from the releases section
2. Run the Password_Generator.exe file
3. No installation required - the application runs as a standalone executable

## Usage

1. **Generate a Password**:
   - Set desired password length using slider or text input
   - Select character types to include
   - Set minimum requirements if needed
   - Click "Generate Password"

2. **Copy Password**:
   - Click "Copy to Clipboard" to copy the generated password
   - Paste anywhere you need the password

3. **Save Password**:
   - Click "Save Password" to store it in history
   - View saved passwords in the History tab

## Security Features

- Cryptographically secure random number generation
- Option to enforce minimum complexity requirements
- Configurable character set exclusions
- No password storage in plain text

## Technical Details

Built with:
- Python 3.12
- tkinter for GUI
- JSON for data persistence
- PyInstaller for executable creation

## Requirements

- Windows 10/11
- No additional software required
- Approximately 15MB disk space

## Privacy

- All data is stored locally
- No internet connection required
- No data collection or transmission

## Support

For issues, questions, or suggestions, please create an issue in the repository or contact the developer.

## License

MIT License - Feel free to use, modify, and distribute as needed.

## Developer Notes

This application was designed with both security and usability in mind, providing a balance between generating secure passwords and maintaining a user-friendly interface. 
