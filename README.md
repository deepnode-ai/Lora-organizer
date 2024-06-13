# Models-organizer
Platform for managing and displaying images stored in the Models directory and its subdirectories

Overview:
This web application, built using Streamlit, serves as an interactive platform for managing and displaying images stored in the "loras" directory and its subdirectories. It provides a user-friendly interface for browsing through collections of images, adding associated metadata, and viewing detailed information about each image.


### Use Cases:

- Developers and AI Artists: Tailored for professionals who need a streamlined way to manage and visually navigate AI models and digital assets within the ComfyUI platform.

#### Key Benefits:

- Visual Model Management: Provides a visual interface to quickly identify and access various types of models like Lora files and checkpoints.
- Ease of Navigation: Simplifies the process of locating and selecting models, enhancing productivity and efficiency in development and creative tasks.
- Seamless Integration: Integrates smoothly with the ComfyUI environment, making it an essential tool for existing users.
  
### Technical Stack:
Frontend: Streamlit
Image Processing: PIL (Python Imaging Library)
Data Management: Python (os, sys libraries for directory and file management)
Styling: External CSS for layout and responsive design adjustments.

#### This application not only simplifies the process of image management but also enhances accessibility and interaction through its user-centric design.

## Preparing the Application
### Structure:
Ensure your project directory is structured as follows:
```
ComfyUI/
├── models/
│   └── app.py        # Your Streamlit application
|   └── style.css         # CSS file for styling (if you have external CSS)
└── ...               # Other directories and files as needed
```

### Launch Streamlit:
Run the Streamlit application by navigating to the models folder and running app.py.
```
streamlit run app.py
```
