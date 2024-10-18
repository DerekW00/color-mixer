# Color Mixer Project Notes

## Project Overview
This file is used to track development progress and manage the Color Mixer project. The project aims to build a web-based application for assisting users with acrylic paint color mixing using a personalized palette, a color mixing assistant powered by GPT-4, and custom UI.

## To-Do List
- [x] Set up project repository
- [x] Set up Flask backend
- [x] Set up React frontend
- [x] Integrate Flask and React for basic functionality
- [x] Add paint to the user’s palette
- [x] Connect to OpenAI GPT-4 for generating mixing instructions
- [ ] Store user’s palette (max 50 paints) in JSON format
- [ ] Provide mixing guide based on RGB values or images
- [ ] Design UI for displaying and managing user’s paint palette
- [ ] Add unit tests for backend (Flask) and frontend (React)
- [ ] Create comprehensive project documentation
- [ ] Optimize backend and frontend for production deployment
- [ ] Plan for future mobile app development (React Native, Swift)

## Progress Log

### 2024-10-18
- **Task:** Set up Flask backend, React frontend, and integrated them to allow adding paints to the palette.
- **Notes:** Successfully set up basic communication between React and Flask. Flask now handles adding paints to a JSON file. Next step is integrating GPT-4 for color mixing instructions.

### 2024-10-18
- **Task:** Integrated GPT-4 for providing color mixing instructions.
- **Notes:** API integration is functional. Currently retrieving basic instructions from GPT-4 based on a provided color name. Need to store the user’s palette in JSON and improve UI.

### 2024-10-18
- **Task:** Managed API keys securely using `.env` and environment variables.
- **Notes:** Added `python-dotenv` to handle environment variables in Flask. `.env` file added to `.gitignore` to prevent exposure of sensitive information (API keys).

### 2024-10-18
- **Task:** Created MVP with functioning backend (Flask) and frontend (React) integration.
- **Notes:** Basic MVP is working locally with the ability to add paints and request mixing instructions via GPT-4. Need to refine the UI and backend logic, as well as store the user's palette.

## Issues and Resolutions

### Issue: Dependency Conflicts with `hyperframe`
- **Description:** Encountered a conflict with the `hyperframe` package when integrating OpenAI API due to an incompatible version of `hyperframe`.
- **Resolution:** Downgraded `hyperframe` to version 5.2.0 to resolve the issue. Updated `requirements.txt` accordingly.

### Issue: API Key Exposure in Repository
- **Description:** Potential issue of exposing the OpenAI API key in the public repository.
- **Resolution:** Stored API key in a `.env` file and used `python-dotenv` to manage environment variables. Ensured `.env` is added to `.gitignore` and removed any tracked API keys.

## Future Enhancements
- **Feature 1: RGB-Based Mixing Guide**
  - Enable users to upload images or enter RGB values to generate color mixing instructions based on their existing palette.
  
- **Feature 2: Palette Management**
  - Create a detailed UI for users to manage their palette, including options to edit or delete paints.

- **Feature 3: Mobile App Support**
  - Extend the project to support mobile platforms using React Native or Swift, allowing users to mix colors on the go.

- **Feature 4: User Accounts**
  - Add authentication and user accounts to save palettes across sessions and devices.

## References
- [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [OpenAI GPT-4 API](https://platform.openai.com/docs/)
