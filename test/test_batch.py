
import os
import sys
from PIL import Image

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from scripts.generator import generate_images

def test_generate_multiple_images(tmpdir):
    """
    Test that the script can handle multiple text inputs and generate the corresponding number of images.
    """
    texts = ["Text 1", "Text 2", "Text 3"]
    output_dir = str(tmpdir)
    
    generate_images(texts, output_dir)
    
    generated_files = os.listdir(output_dir)
    assert len(generated_files) == len(texts)

def test_image_properties(tmpdir):
    """
    Test that the generated images have the correct dimensions and format.
    """
    texts = ["Test Text"]
    output_dir = str(tmpdir)
    
    generate_images(texts, output_dir)
    
    generated_files = os.listdir(output_dir)
    assert len(generated_files) == 1
    
    image_path = os.path.join(output_dir, generated_files[0])
    with Image.open(image_path) as img:
        assert img.size == (1242, 1660)
        assert img.format == 'PNG'
