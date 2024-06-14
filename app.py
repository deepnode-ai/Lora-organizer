import os
from PIL import Image
import streamlit as st
from streamlit_navigation_bar import st_navbar
from streamlit_modal import Modal

def get_subfolders(directory):
    """Return a list of subdirectories in the given directory, excluding specified folders."""
    exclude_folders = ["IPA - LCM", "Example Folder"]  # Add more folder names to exclude as needed
    return [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d)) and d not in exclude_folders]

# Determine the directory of the currently executing script
script_dir = os.path.dirname(os.path.realpath(__file__))
loras_path = os.path.join(script_dir, 'loras')
subfolders = get_subfolders(loras_path)

# Navigation setup
subfolders = get_subfolders(loras_path)
page = st_navbar(subfolders)
st.write(f"You selected: {page}")

def load_images(directory):
    images = []
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return images
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".jpeg"):
                image_path = os.path.join(root, filename)
                images.append((filename, image_path))
    return images

def display_images(images):
    target_size = (300, 400)  # Set the target size of each image
    cols_per_row = 4
    cols = st.columns(cols_per_row)
    for idx, (filename, image_path) in enumerate(images):
        with cols[idx % cols_per_row]:
            image = Image.open(image_path)
            image.thumbnail(target_size, Image.LANCZOS)
            image = image.crop((0, 0, target_size[0], target_size[1]))
            st.image(image, use_column_width=True)

            # Button to open the expander (acts like a popup)
            modal = Modal(key=f"modal_{idx}", title="Lora Details")
            open_modal = st.button(label='Add lora', key=f"button_{idx}")
            if open_modal:
                with modal.container():

                   # Extract relative path from the loras_path and remove the file extension
                    relative_path = os.path.relpath(image_path, start=loras_path)
                    display_name = os.path.splitext(relative_path)[0]  # Remove file extension
                    lora_display_name = f"`<lora:{display_name}:1.0>`"
                    st.markdown(f"**WildcardEncode:** {lora_display_name}")
                    st.session_state['lora_display_name'] = lora_display_name
                    st.session_state['show_details'] = True


# Now handle the display based on `page`
if page:
    st.header(f'{page} Files')
    folder_path = os.path.join(loras_path, page)
    images = load_images(folder_path)
    display_images(images)
    st.write(f'Manage your Lora in {page}.')

# Display lora file name in popup
if 'show_details' in st.session_state and st.session_state.show_details:
    with st.expander("Lora File Details", expanded=True):
        st.write(st.session_state.lora_display_name)
        if st.button("Close Details"):
            st.session_state.show_details = False
