# Models-organizer
Platform for managing and displaying images stored in the Models directory and its subdirectories

Overview:
This web application, built using Streamlit, serves as an interactive platform for managing and displaying images stored in the "loras" directory and its subdirectories. It provides a user-friendly interface for browsing through collections of images, adding associated metadata, and viewing detailed information about each image.


### Use Cases:
Ideal for artists, photographers, and digital asset managers who need an efficient way to catalog and retrieve visual resources.
Useful in settings where quick visual identification and access to image details are required, such as digital libraries, content management systems, or collaborative creative projects.

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
