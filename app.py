import streamlit as st
import os
from PIL import Image

# Function to recursively load images from "loras" and its subdirectories
def load_images(directory):
    images = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".jpeg"):  # Target specific image file extensions
                base_name = os.path.splitext(filename)[0]  # Get the base name without extension
                lora_file = base_name + '.safetensors'  # Assume the lora file has the same base name
                image_path = os.path.join(root, filename)
                lora_path = os.path.join(root, lora_file)
                images.append((filename, image_path, lora_path))
    return images

# Function to display images in a grid
def display_images(images):
    cols_per_row = 4  # Number of images per row
    cols = st.columns(cols_per_row)
    for idx, (filename, image_path, lora_path) in enumerate(images):
        with cols[idx % cols_per_row]:
            image = Image.open(image_path)
            st.image(image, caption=filename, use_column_width=True)
            if st.button(f"Add lora", key=filename):
                # Strip '.safetensors' from the lora_path and format the display name
                display_name = os.path.splitext(lora_path)[0]
                lora_display_name = f"<{display_name}:1.0>"
                st.session_state['lora_display_name'] = lora_display_name
                st.session_state['show_details'] = True


# Navigation setup
st.sidebar.title('Navigation')
choice = st.sidebar.radio('Go to', ['Home', 'Lora', 'Checkpoint'])

if choice == 'Home':
    st.header('Home')
    st.write('Welcome to the Home Page!')
elif choice == 'Lora':
    st.header('Lora Files')
    images = load_images('loras')
    display_images(images)
    st.write('Manage your Lora here.')
elif choice == 'Checkpoint':
    st.header('Checkpoint')
    images = load_images('checkpoints')
    display_images(images)
    st.write('Manage your checkpoints here.')

# Display lora file name in popup
if 'show_details' in st.session_state and st.session_state.show_details:
    with st.expander("Lora File Details", expanded=True):
        st.write(st.session_state.lora_display_name)
        if st.button("Close Details"):
            st.session_state.show_details = False

