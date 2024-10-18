# Acrylic Color Mixing Assistant

## Overview
This project is a personalized acrylic color mixing assistant powered by GPT-4. It helps users mix acrylic paints by offering detailed instructions based on their existing paint palette, color names, or RGB values. The assistant allows users to store up to 50 paints from different brands, retrieve color mixing instructions, and learn color theory. Users can input target colors by name or RGB, and the assistant will generate a mixing guide using the available paints in the palette.

## Features
- **Store up to 50 paints**: Track and manage your personal palette of acrylic paints, including brand name, color name, pigment code, and RGB values.
- **Determine target colors**: Input a color name (e.g., "Teal"), and the assistant will suggest a mixing guide based on your existing paints.
- **RGB-based color matching**: Input RGB values (e.g., grabbed from photos or design tools), and the assistant will find the closest mix using your stored paints.
- **Powered by GPT-4**: Utilizes GPT-4 to generate mixing instructions and color theory explanations, ensuring the guidance is tailored to your paint collection.

## Technology Stack
- **Python**: For backend logic and GPT-4 integration.
- **GPT-4 API**: Handles the color mixing and color theory guidance.
- **Flask (optional)**: For a simple web interface.
- **SQLite/JSON**: To store user palette data.
- **HTML/CSS/JavaScript**: For the front-end interface.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/DerekW00/color-mixer.git
    cd color-mixer
    ```

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up OpenAI API**:
   - Sign up for an API key from OpenAI (if you haven’t already).
   - Create a `.env` file in the root directory and add your API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

1. **Run the application**:
   - If using a web app with Flask:
     ```bash
     flask run
     ```
   - If using a command-line interface:
     ```bash
     python src/app.py
     ```

2. **Palette Management**:
   - Add new paints to your palette by specifying the brand, paint name, pigment code, and RGB values.
   - Example:  
     ```python
     add_paint("Liquitex", "Cadmium Red", "PR108", [227, 29, 29])
     ```

3. **Mixing Instructions**:
   - Input a target color name (e.g., “Teal”), and the assistant will provide a guide to mix that color from your palette.
   - Alternatively, input an RGB value for more precise color matching:
     ```python
     generate_mixing_prompt([64, 224, 208])
     ```

## Planned Features
- **Image upload for color recognition**: Allow users to upload images to extract RGB values automatically.
- **Advanced color theory lessons**: Provide interactive learning modules on color mixing principles.
- **Palette visualization**: Show users a visual representation of their palette with the ability to simulate mixing digitally.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Powered by [OpenAI GPT-4](https://openai.com/api/).
- Thanks to all open-source libraries and contributors.