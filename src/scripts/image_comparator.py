
from PIL import Image, ImageChops, ImageStat
import os

def compare_images(image_one_path, image_two_path):
    """
    Compares two images and returns a similarity percentage.
    """
    try:
        image_one = Image.open(image_one_path).convert('RGB')
        image_two = Image.open(image_two_path).convert('RGB')
        
        if image_one.size != image_two.size:
            return 0.0

        diff = ImageChops.difference(image_one, image_two)
        
        stat = ImageStat.Stat(diff)
        diff_ratio = sum(stat.mean) / (len(stat.mean) * 255)

        return (1 - diff_ratio) * 100
    except FileNotFoundError:
        return 0.0

def create_diff_report(report_path, reference_dir, output_dir, similarity_threshold):
    """
    Generates a diff report comparing images from two directories.
    """
    reference_images = sorted(os.listdir(reference_dir))
    generated_images = sorted(os.listdir(output_dir))

    with open(report_path, 'w') as f:
        f.write("| Reference Image | Generated Image | Similarity | Status |\n")
        f.write("|---|---|---|---|")

        for ref_img_name in reference_images:
            if ref_img_name not in generated_images:
                f.write(f"| {ref_img_name} | N/A | 0% | Missing |\n")
                continue

            ref_path = os.path.join(reference_dir, ref_img_name)
            gen_path = os.path.join(output_dir, ref_img_name)

            similarity = compare_images(ref_path, gen_path)
            status = "Passed" if similarity >= similarity_threshold else "Failed"

            f.write(f"| {ref_img_name} | {ref_img_name} | {similarity:.2f}% | {status} |\n")
